---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.tokenize.html
---

# mlx.data.Buffer.tokenize

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.tokenize.rst)
- **

.pdf

**

# mlx.data.Buffer.tokenize

 Table of contents 

## Contents

# mlx.data.Buffer.tokenize

**Buffer.tokenize(*self: mlx.data._c.Buffer*, *key: str*, *trie: mlx::data::core::Trie<char>*, *mode: mlx.data._c.TokenizeMode = <TokenizeMode.Shortest: 0>*, *ignore_unk: bool = False*, *trie_key_scores: List[float] = []*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Tokenize the contents of the array at `key`.
This operation uses a [mlx.data.core.CharTrie](mlx.data.core.CharTrie.html#mlx.data.core.CharTrie) to tokenize the
contents of the array. The tokenizer computes a graph of Trie nodes
that matches the content of the array at `key`. Subsequently, it
either samples a path along the graph (if mode is
`mlx.data.core.TokenizeMode.rand`) or finds the shortest weighted
path using the `trie_key_scores` for weights.
If `trie_key_scores` are not provided, then each has the same weight
of 1 and the result is the smallest number of tokens that can represent
the content.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**trie** ([mlx.data.core.CharTrie](mlx.data.core.CharTrie.html#mlx.data.core.CharTrie)) – The trie to use for the tokenization.
**mode** (*mlx.data.core.TokenizeMode*) – The tokenizer mode to use.
Shortest or random as described above. (default: mlx.data.core.TokenizeMode.shortest)
**ignore_unk** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True then ignore content that cannot be
represented. Otherwise throw an exception. (default: False)
**trie_key_scores** ([list](https://docs.python.org/3/library/stdtypes.html#list)* of *[float](https://docs.python.org/3/library/functions.html#float)) – The weights of each node in the
trie. (default: [] which means each node gets a weight of 1)
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If it is not empty then write the result to this
key instead of overwriting `key`. (default: ‘’)

** Contents
