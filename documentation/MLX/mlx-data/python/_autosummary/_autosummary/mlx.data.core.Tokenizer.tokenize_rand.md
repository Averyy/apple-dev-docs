---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/_autosummary/mlx.data.core.Tokenizer.tokenize_rand.html
---

# mlx.data.core.Tokenizer.tokenize_rand

**

- [.rst](../../../_sources/python/_autosummary/_autosummary/mlx.data.core.Tokenizer.tokenize_rand.rst)
- **

.pdf

**

# mlx.data.core.Tokenizer.tokenize_rand

 Table of contents 

## Contents

# mlx.data.core.Tokenizer.tokenize_rand

**Tokenizer.tokenize_rand(*self: mlx.data._c.core.Tokenizer*, *input: str*) → List[[int](https://docs.python.org/3/library/functions.html#int)]**
: Tokenize the input with a valid tokenization chosen randomly from
the set of valid tokenizations.
For instance if our set of tokens is {‘a’, ‘aa’, ‘b’} then the
string ‘aab’ can have 2 different tokenizations:

0, 0, 2
1, 2

[Tokenizer.tokenize_shortest()](mlx.data.core.Tokenizer.tokenize_shortest.html#mlx.data.core.Tokenizer.tokenize_shortest) will return the second one if no
`trie_key_scores` are provided while
[Tokenizer.tokenize_rand()](#mlx.data.core.Tokenizer.tokenize_rand) will sample either of the two.

Parameters:
**input** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The input string to be tokenized.

** Contents
