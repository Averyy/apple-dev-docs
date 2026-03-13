---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.utils.tree_reduce.html
---

# mlx.utils.tree_reduce

**

- [.rst](../../_sources/python/_autosummary/mlx.utils.tree_reduce.rst)
- **

.pdf

**

**
**
**

**

# mlx.utils.tree_reduce

 Table of contents 

## Contents

# mlx.utils.tree_reduce

**tree_reduce(*fn*, *tree*, *initializer=None*, *is_leaf=None*)**
: Applies a reduction to the leaves of a Python tree.
This function reduces Python trees into an accumulated result by applying
the provided function `fn` to the leaves of the tree.
Example
>>> from mlx.utils import tree_reduce
>>> tree = {"a": [1, 2, 3], "b": [4, 5]}
>>> tree_reduce(lambda acc, x: acc + x, tree, 0)
15

Parameters:

**fn** (*callable*) – The reducer function that takes two arguments (accumulator,
current value) and returns the updated accumulator.
**tree** (*Any*) – The Python tree to reduce. It can be any nested combination of
lists, tuples, or dictionaries.
**initializer** (*Any**, **optional*) – The initial value to start the reduction. If
not provided, the first leaf value is used.
**is_leaf** (*callable**, **optional*) – A function to determine if an object is a
leaf, returning `True` for leaf nodes and `False` otherwise.

Returns:
The accumulated value.

Return type:
*Any*

** Contents
