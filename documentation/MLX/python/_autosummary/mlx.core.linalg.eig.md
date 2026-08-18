---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.eig.html
---

# mlx.core.linalg.eig

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.eig.rst)
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

# mlx.core.linalg.eig

 Table of contents 

## Contents

# mlx.core.linalg.eig

**eig(*a: array*, ***, *stream: StreamOrDevice = None*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]**
: Compute the eigenvalues and eigenvectors of a square matrix.
This function differs from [numpy.linalg.eig()](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html#numpy.linalg.eig) in that the
return type is always complex even if the eigenvalues are all real.
This function supports arrays with at least 2 dimensions. When the input
has more than two dimensions, the eigenvalues and eigenvectors are
computed for each matrix in the last two dimensions.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
A tuple containing the eigenvalues and the normalized right
eigenvectors. The column `v[:, i]` is the eigenvector
corresponding to the i-th eigenvalue.

Return type:
*Tuple*[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]

Example
>>> A = mx.array([[1., -2.], [-2., 1.]])
>>> w, v = mx.linalg.eig(A, stream=mx.cpu)
>>> w
array([3+0j, -1+0j], dtype=complex64)
>>> v
array([[0.707107+0j, 0.707107+0j],
       [-0.707107+0j, 0.707107+0j]], dtype=complex64)

** Contents
