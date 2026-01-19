---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.eigvals.html
---

# mlx.core.linalg.eigvals

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.eigvals.rst)
- **

.pdf

**

# mlx.core.linalg.eigvals

 Table of contents 

## Contents

# mlx.core.linalg.eigvals

**eigvals(*a: array*, ***, *stream: Stream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the eigenvalues of a square matrix.
This function differs from [numpy.linalg.eigvals()](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eigvals.html#numpy.linalg.eigvals) in that the
return type is always complex even if the eigenvalues are all real.
This function supports arrays with at least 2 dimensions. When the
input has more than two dimensions, the eigenvalues are computed for
each matrix in the last two dimensions.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The eigenvalues (not necessarily in order).

Return type:
[array](mlx.core.array.html#mlx.core.array)

Example
>>> A = mx.array([[1., -2.], [-2., 1.]])
>>> eigenvalues = mx.linalg.eigvals(A, stream=mx.cpu)
>>> eigenvalues
array([3+0j, -1+0j], dtype=complex64)

** Contents
