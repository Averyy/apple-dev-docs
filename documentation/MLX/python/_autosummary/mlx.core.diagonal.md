---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.diagonal.html
---

# mlx.core.diagonal

**

- [.rst](../../_sources/python/_autosummary/mlx.core.diagonal.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.diagonal

 Table of contents 

## Contents

# mlx.core.diagonal

**diagonal(*a: array*, *offset: int = 0*, *axis1: int = 0*, *axis2: int = 1*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return specified diagonals.
If `a` is 2-D, then a 1-D array containing the diagonal at the given
`offset` is returned.
If `a` has more than two dimensions, then `axis1` and `axis2`
determine the 2D subarrays from which diagonals are extracted. The new
shape is the original shape with `axis1` and `axis2` removed and a
new dimension inserted at the end corresponding to the diagonal.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**offset** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Offset of the diagonal from the main diagonal.
Can be positive or negative. Default: `0`.
**axis1** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The first axis of the 2-D sub-arrays from which
the diagonals should be taken. Default: `0`.
**axis2** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The second axis of the 2-D sub-arrays from which
the diagonals should be taken. Default: `1`.

Returns:
The diagonals of the array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
