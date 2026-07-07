---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.slogdet.html
---

# mlx.core.linalg.slogdet

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.slogdet.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.linalg.slogdet

 Table of contents 

## Contents

# mlx.core.linalg.slogdet

**slogdet(*a: array*, ***, *stream: None | Stream | Device = None*) → Tuple[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]**
: Compute the sign and natural log of the absolute value of the
determinant of a square matrix.
This function supports arrays with at least 2 dimensions. When the
input has more than two dimensions, the sign and log-absolute-determinant
are computed for each matrix in the last two dimensions.
For a singular matrix, `sign` is 0 and `logabsdet` is `-inf`.
The determinant can be reconstructed as `det = sign * exp(logabsdet)`.
This is more numerically stable than computing the determinant directly
for matrices with large or small determinants.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:

The `sign` and `logabsdet` of thedeterminant. `sign` is -1, 0, or +1. `logabsdet` is the
natural log of the absolute value of the determinant.

Return type:
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array))

Example
>>> A = mx.array([[1., 2.], [3., 4.]])
>>> sign, logabsdet = mx.linalg.slogdet(A, stream=mx.cpu)
>>> sign
array(-1, dtype=float32)
>>> logabsdet
array(0.693147, dtype=float32)

** Contents
