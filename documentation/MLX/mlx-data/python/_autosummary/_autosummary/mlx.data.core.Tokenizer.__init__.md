---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/_autosummary/mlx.data.core.Tokenizer.__init__.html
---

# mlx.data.core.Tokenizer.__init__

**

- [.rst](../../../_sources/python/_autosummary/_autosummary/mlx.data.core.Tokenizer.__init__.rst)
- **

.pdf

**

# mlx.data.core.Tokenizer.__init__

 Table of contents 

## Contents

# mlx.data.core.Tokenizer.__init__

**Tokenizer.__init__(*self: mlx.data._c.core.Tokenizer*, *trie: mlx.data._c.core.CharTrie*, *ignore_unk: bool = False*, *trie_key_scores: List[float] = []*) → [None](https://docs.python.org/3/library/constants.html#None)**
: Make a tokenizer object that can be used to tokenize arbitrary strings.

Parameters:

**trie** ([mlx.data.core.CharTrie](../mlx.data.core.CharTrie.html#mlx.data.core.CharTrie)) – The trie containing the possible tokens.
**ignore_unk** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether unknown tokens should be ignored or
an error should be raised. (default: false)
**trie_key_scores** ([list](https://docs.python.org/3/library/stdtypes.html#list)*[*[float](https://docs.python.org/3/library/functions.html#float)*]*) – A list containing one score per
trie node. If left empty each score is assumed equal to 1.
Tokenize shortest minimizes the sum of these scores over
the sequence of tokens.

** Contents
