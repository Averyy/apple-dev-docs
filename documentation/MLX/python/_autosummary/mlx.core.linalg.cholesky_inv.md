---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.cholesky_inv.html
---

# mlx.core.linalg.cholesky_inv

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.cholesky_inv.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.core.linalg.cholesky_inv

 Table of contents 

## Contents

# mlx.core.linalg.cholesky_inv

**cholesky_inv(*a: array*, *upper: bool = False*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the inverse of a real symmetric positive semi-definite matrix using it’s Cholesky decomposition.
Let \(\mathbf{A}\) be a real symmetric positive semi-definite matrix and \(\mathbf{L}\) its Cholesky decomposition such that:

\[\begin{aligned}
  \mathbf{A} = \mathbf{L}\mathbf{L}^T
\end{aligned}\]
This function computes \(\mathbf{A}^{-1}\).
This function supports arrays with at least 2 dimensions. When the input
has more than two dimensions, the Cholesky inverse is computed for each matrix
in the last two dimensions of \(\mathbf{L}\).
If the input matrix is not a triangular matrix behaviour is undefined.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array. This is the Cholesky factor
\(\mathbf{L}\), not \(\mathbf{A}\) itself.
**upper** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, return the upper triangular Cholesky factor.
If `False`, return the lower triangular Cholesky factor. Default: `False`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
\(\mathbf{A^{-1}}\) where \(\mathbf{A} = \mathbf{L}\mathbf{L}^T\).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
