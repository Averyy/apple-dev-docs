---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.tokenizer_helpers.read_trie_from_vocab.html
---

# mlx.data.tokenizer_helpers.read_trie_from_vocab

```python
class mlx.data.tokenizer_helpers.read_trie_from_vocab(vocab_file)
```

Read an [mlx.data.core.CharTrie](mlx.data.core.CharTrie.md#mlx.data.core.CharTrie) from a file with one token per line.

**Parameters:**
: **vocab_file** (*path* *or* *file like*) – The text file containing one token per line.

**Returns:**
: containing the the vocabulary from `vocab_file`.

**Return type:**
: [mlx.data.core.CharTrie](mlx.data.core.CharTrie.md#mlx.data.core.CharTrie)
