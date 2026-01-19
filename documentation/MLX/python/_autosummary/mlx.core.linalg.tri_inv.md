---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.tri_inv.html
---

# mlx.core.linalg.tri_inv

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.tri_inv.rst)
- **

.pdf

**

# mlx.core.linalg.tri_inv

 Table of contents 

## Contents

# mlx.core.linalg.tri_inv

**tri_inv(*a: array*, *upper: bool = False*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the inverse of a triangular square matrix.
This function supports arrays with at least 2 dimensions. When the input
has more than two dimensions, the inverse is computed for each matrix
in the last two dimensions of `a`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**upper** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether the array is upper or lower triangular. Defaults to `False`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
`ainv` such that `dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])`

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
