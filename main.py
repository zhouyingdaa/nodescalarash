"""calculator_c125e3 - Collection operations."""
from collections import Counter, defaultdict
import json, string
ALGO_ID = "calculator_c125e3"
def frequency_analysis(text: str) -> dict:
    counts = Counter(c for c in text.lower() if c in string.ascii_lowercase)
    return dict(counts.most_common(10))
def group_by_length(words: list) -> dict:
    groups = defaultdict(list)
    for w in words: groups[len(w)].append(w)
    return {k: v for k, v in sorted(groups.items())}
def main():
    text = "The quick brown fox jumps over the lazy dog near the river bank"
    freq = frequency_analysis(text)
    groups = group_by_length(text.split())
    print(f"[{ALGO_ID}] Frequency: {json.dumps(freq)}")
    print(f"[{ALGO_ID}] Groups: {json.dumps(groups, indent=2)}")
if __name__ == "__main__":
    main()
