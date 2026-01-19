---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.core.CharTrie.html
---

# mlx.data.core.CharTrie

**

- [.rst](../../_sources/python/_autosummary/mlx.data.core.CharTrie.rst)
- **

.pdf

**

# mlx.data.core.CharTrie

 Table of contents 

## Contents

# mlx.data.core.CharTrie

***class *mlx.data.core.CharTrie**
: A Trie implementation for characters.
It enables making a graph of all possible tokenizations and then
searching for the shortest one.
Methods

[__init__](_autosummary/mlx.data.core.CharTrie.__init__.html#mlx.data.core.CharTrie.__init__)(self)

[insert](_autosummary/mlx.data.core.CharTrie.insert.html#mlx.data.core.CharTrie.insert)(self, token[, id])
Insert a token in the trie making a new token if it doesn't already exist.

[key](_autosummary/mlx.data.core.CharTrie.key.html#mlx.data.core.CharTrie.key)(self, id)
Get the `id`-th token as a list of characters.

[key_bytes](_autosummary/mlx.data.core.CharTrie.key_bytes.html#mlx.data.core.CharTrie.key_bytes)(self, id)
Get the `id`-th token as bytes.

[key_string](_autosummary/mlx.data.core.CharTrie.key_string.html#mlx.data.core.CharTrie.key_string)(self, id)
Get the string that corresponds to the `id`-th token.

[num_keys](_autosummary/mlx.data.core.CharTrie.num_keys.html#mlx.data.core.CharTrie.num_keys)(self)
Return how many keys/nodes have been inserted in the Trie.

[root](_autosummary/mlx.data.core.CharTrie.root.html#mlx.data.core.CharTrie.root)(self)
Get the root node of the trie

[search](_autosummary/mlx.data.core.CharTrie.search.html#mlx.data.core.CharTrie.search)(self, token)
Search a the passed string or list of characters in the trie and return the node or None if not found.

** Contents
