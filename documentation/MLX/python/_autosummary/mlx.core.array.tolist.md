---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.array.tolist.html
---

# mlx.core.array.tolist

**

- [.rst](../../_sources/python/_autosummary/mlx.core.array.tolist.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.array.tolist

 Table of contents 

## Contents

# mlx.core.array.tolist

**array.tolist(*self*) → list_or_scalar**
: Convert the array to a Python [list](https://docs.python.org/3/library/stdtypes.html#list).

Returns:
The Python list.
If the array is a scalar then a standard Python scalar is returned.
If the array has more than one dimension then the result is a nested
list of lists.
The value type of the list corresponding to the last dimension is either
`bool`, `int` or `float` depending on the `dtype` of the array.

Return type:
[list](https://docs.python.org/3/library/stdtypes.html#list)

** Contents
