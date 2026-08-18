---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.eigh.html
---

# mlx.core.linalg.eigh

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.eigh.rst)
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

# mlx.core.linalg.eigh

 Table of contents 

## Contents

# mlx.core.linalg.eigh

**eigh(*a: array*, *UPLO: str = 'L'*, ***, *stream: StreamOrDevice = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]**
: Compute the eigenvalues and eigenvectors of a complex Hermitian or
real symmetric matrix.
This function supports arrays with at least 2 dimensions. When the input
has more than two dimensions, the eigenvalues and eigenvectors are
computed for each matrix in the last two dimensions.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array. Must be a real symmetric or complex
Hermitian matrix.
**UPLO** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Whether to use the upper (`"U"`) or
lower (`"L"`) triangle of the matrix.  Default: `"L"`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
A tuple containing the eigenvalues in ascending order and
the normalized eigenvectors. The column `v[:, i]` is the
eigenvector corresponding to the i-th eigenvalue.

Return type:
*Tuple*[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]

Note
The input matrix is assumed to be symmetric (or Hermitian). Only
the selected triangle is used. No checks for symmetry are performed.

Example
>>> A = mx.array([[1., -2.], [-2., 1.]])
>>> w, v = mx.linalg.eigh(A, stream=mx.cpu)
>>> w
array([-1., 3.], dtype=float32)
>>> v
array([[ 0.707107, -0.707107],
      [ 0.707107,  0.707107]], dtype=float32)

** Contents
