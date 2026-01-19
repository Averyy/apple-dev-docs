---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.qr.html
---

# mlx.core.linalg.qr

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.qr.rst)
- **

.pdf

**

# mlx.core.linalg.qr

 Table of contents 

## Contents

# mlx.core.linalg.qr

**qr(*a: array*, ***, *stream: None | Stream | Device = None*) → Tuple[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]**
: The QR factorization of the input matrix.
This function supports arrays with at least 2 dimensions. The matrices
which are factorized are assumed to be in the last two dimensions of
the input.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
`Q` and `R` matrices such that `Q @ R = a`.

Return type:
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array))

Example
>>> A = mx.array([[2., 3.], [1., 2.]])
>>> Q, R = mx.linalg.qr(A, stream=mx.cpu)
>>> Q
array([[-0.894427, -0.447214],
       [-0.447214, 0.894427]], dtype=float32)
>>> R
array([[-2.23607, -3.57771],
       [0, 0.447214]], dtype=float32)

** Contents
