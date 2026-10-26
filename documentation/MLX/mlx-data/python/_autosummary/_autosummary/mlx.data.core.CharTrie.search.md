---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/_autosummary/mlx.data.core.CharTrie.search.html
---

# mlx.data.core.CharTrie.search

**CharTrie.search(*self: mlx.data._c.core.CharTrie*, *token: str | List[str]*) → mlx.data._c.core.CharTrieNode**
: Search a the passed string or list of characters in the trie and
return the node or None if not found.
To get the id of a token it suffices to do:

  ```
  print(trie.search("hello").id)
  ```

However, if ‘hello’ is not in the vocabulary then
[CharTrie.search()](#mlx.data.core.CharTrie.search) will return None.

Parameters:
**token** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*[**char**]*) – The token to be searched given
either as a string or a list of characters.

Returns:
The node corresponding to
the `token` or None.

Return type:
`mlx.data.core.CharTrieNode`
