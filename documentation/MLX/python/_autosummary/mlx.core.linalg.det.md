---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.det.html
---

# mlx.core.linalg.det

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.det.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.linalg.det

 Table of contents 

## Contents

# mlx.core.linalg.det

**det(*a: array*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the determinant of a square matrix.
This function supports arrays with at least 2 dimensions. When the
input has more than two dimensions, the determinant is computed for
each matrix in the last two dimensions.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The determinant(s) of the input matrix (matrices).

Return type:
[array](mlx.core.array.html#mlx.core.array)

Example
>>> A = mx.array([[1., 2.], [3., 4.]])
>>> mx.linalg.det(A, stream=mx.cpu)
array(-2, dtype=float32)

** Contents
