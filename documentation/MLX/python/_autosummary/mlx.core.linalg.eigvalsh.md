---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.eigvalsh.html
---

# mlx.core.linalg.eigvalsh

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.eigvalsh.rst)
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

# mlx.core.linalg.eigvalsh

 Table of contents 

## Contents

# mlx.core.linalg.eigvalsh

**eigvalsh(*a: array*, *UPLO: str = 'L'*, ***, *stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the eigenvalues of a complex Hermitian or real symmetric matrix.
This function supports arrays with at least 2 dimensions. When the
input has more than two dimensions, the eigenvalues are computed for
each matrix in the last two dimensions.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array. Must be a real symmetric or complex
Hermitian matrix.
**UPLO** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Whether to use the upper (`"U"`) or
lower (`"L"`) triangle of the matrix.  Default: `"L"`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The eigenvalues in ascending order.

Return type:
[array](mlx.core.array.html#mlx.core.array)

Note
The input matrix is assumed to be symmetric (or Hermitian). Only
the selected triangle is used. No checks for symmetry are performed.

Example
>>> A = mx.array([[1., -2.], [-2., 1.]])
>>> eigenvalues = mx.linalg.eigvalsh(A, stream=mx.cpu)
>>> eigenvalues
array([-1., 3.], dtype=float32)

** Contents
