---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.cholesky.html
---

# mlx.core.linalg.cholesky

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.cholesky.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.linalg.cholesky

 Table of contents 

## Contents

# mlx.core.linalg.cholesky

**cholesky(*a: array*, *upper: bool = False*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the Cholesky decomposition of a real symmetric positive semi-definite matrix.
This function supports arrays with at least 2 dimensions. When the input
has more than two dimensions, the Cholesky decomposition is computed for each matrix
in the last two dimensions of `a`.
If the input matrix is not symmetric positive semi-definite, behaviour is undefined.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**upper** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, return the upper triangular Cholesky factor.
If `False`, return the lower triangular Cholesky factor. Default: `False`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
If `upper = False`, it returns a lower triangular `L` matrix such
that `L @ L.T = a`.  If `upper = True`, it returns an upper triangular
`U` matrix such that `U.T @ U = a`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
