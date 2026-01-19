---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.core.Tokenizer.html
---

# mlx.data.core.Tokenizer

**

- [.rst](../../_sources/python/_autosummary/mlx.data.core.Tokenizer.rst)
- **

.pdf

**

# mlx.data.core.Tokenizer

 Table of contents 

## Contents

# mlx.data.core.Tokenizer

***class *mlx.data.core.Tokenizer**
: A Tokenizer that can be used to tokenize arbitrary strings.

Parameters:

**trie** ([mlx.data.core.CharTrie](mlx.data.core.CharTrie.html#mlx.data.core.CharTrie)) – The trie containing the possible tokens.
**ignore_unk** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether unknown tokens should be ignored or
an error should be raised. (default: false)
**trie_key_scores** ([list](https://docs.python.org/3/library/stdtypes.html#list)*[*[float](https://docs.python.org/3/library/functions.html#float)*]*) – A list containing one score per
trie node. If left empty each score is assumed equal to 1.
Tokenize shortest minimizes the sum of these scores over
the sequence of tokens.

Methods

[__init__](_autosummary/mlx.data.core.Tokenizer.__init__.html#mlx.data.core.Tokenizer.__init__)(self, trie[, ignore_unk, ...])
Make a tokenizer object that can be used to tokenize arbitrary strings.

[tokenize](_autosummary/mlx.data.core.Tokenizer.tokenize.html#mlx.data.core.Tokenizer.tokenize)(self, input)
Return the full graph of possible tokenizations.

[tokenize_rand](_autosummary/mlx.data.core.Tokenizer.tokenize_rand.html#mlx.data.core.Tokenizer.tokenize_rand)(self, input)
Tokenize the input with a valid tokenization chosen randomly from the set of valid tokenizations.

[tokenize_shortest](_autosummary/mlx.data.core.Tokenizer.tokenize_shortest.html#mlx.data.core.Tokenizer.tokenize_shortest)(self, input)
Tokenize the input such that the sum of `trie_key_scores` is minimized.

** Contents
