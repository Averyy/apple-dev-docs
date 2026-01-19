---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/_autosummary/mlx.data.core.CharTrie.insert.html
---

# mlx.data.core.CharTrie.insert

**

- [.rst](../../../_sources/python/_autosummary/_autosummary/mlx.data.core.CharTrie.insert.rst)
- **

.pdf

**

# mlx.data.core.CharTrie.insert

 Table of contents 

## Contents

# mlx.data.core.CharTrie.insert

**CharTrie.insert(*self: mlx.data._c.core.CharTrie*, *token: str | List[str]*, *id: int = -1*) → mlx.data._c.core.CharTrieNode**
: Insert a token in the trie making a new token if it doesn’t already exist.

Parameters:

**token** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*[**char**]*) – The new token to be inserted given
either as a string or a list of characters.
**id** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The id to assign to the new token to be
inserted. If negative then use `num_keys()` as default.
Default: `-1`.

** Contents
