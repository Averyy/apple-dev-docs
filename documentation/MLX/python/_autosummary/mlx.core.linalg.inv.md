---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.inv.html
---

# mlx.core.linalg.inv

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.inv.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.linalg.inv

 Table of contents 

## Contents

# mlx.core.linalg.inv

**inv(*a: array*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the inverse of a square matrix.
This function supports arrays with at least 2 dimensions. When the input
has more than two dimensions, the inverse is computed for each matrix
in the last two dimensions of `a`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
`ainv` such that `dot(a, ainv) = dot(ainv, a) = eye(a.shape[0])`

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
