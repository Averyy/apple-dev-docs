---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.tokenizer_helpers.read_trie_from_spm.html
---

# mlx.data.tokenizer_helpers.read_trie_from_spm

**

- [.rst](../../_sources/python/_autosummary/mlx.data.tokenizer_helpers.read_trie_from_spm.rst)
- **

.pdf

**

# mlx.data.tokenizer_helpers.read_trie_from_spm

 Table of contents 

## Contents

# mlx.data.tokenizer_helpers.read_trie_from_spm

***class *mlx.data.tokenizer_helpers.read_trie_from_spm(*spm_file*)**
: Read an [mlx.data.core.CharTrie](mlx.data.core.CharTrie.html#mlx.data.core.CharTrie) from a sentencepiece file.
Reading directly from a model file requires installing sentencepiece,
however if the vocabulary and the scores are exported the file can be read
without installing sentencepiece.

Note
Sentencepiece models are almost always BPE models with scores being the
associated log likelihood of from a unigram language model. Using the
[mlx.data.core.CharTrie](mlx.data.core.CharTrie.html#mlx.data.core.CharTrie) and the loaded scores will provide the
shortest possible tokenization with the highest possible log likelihood
but it can be slightly different than the BPE one.
Use `read_bpe_from_spm()` to load the model to be used with a
`mlx.data.core.BPETokenizer`.

Parameters:
**spm_file** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Either a sentencepiece model file or a vocab file
extracted from a sentencepiece model.

Returns:
The trie and the
corresponding weights from the SPM mdoel.

Return type:
tuple[[mlx.data.core.CharTrie](mlx.data.core.CharTrie.html#mlx.data.core.CharTrie), list[float]]

** Contents
