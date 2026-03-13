---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.svd.html
---

# mlx.core.linalg.svd

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.svd.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.linalg.svd

 Table of contents 

## Contents

# mlx.core.linalg.svd

**svd(*a: array*, *compute_uv: bool = True*, ***, *stream: None | Stream | Device = None*) → Tuple[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]**
: The Singular Value Decomposition (SVD) of the input matrix.
This function supports arrays with at least 2 dimensions. When the input
has more than two dimensions, the function iterates over all indices of the first
a.ndim - 2 dimensions and for each combination SVD is applied to the last two indices.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**compute_uv** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, return the `U`, `S`, and `Vt` components.
If `False`, return only the `S` array. Default: `True`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
If compute_uv is `True` returns the `U`, `S`, and `Vt` matrices, such that
`A = U @ diag(S) @ Vt`. If compute_uv is `False` returns singular values array `S`.

Return type:
*Union*[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([array](mlx.core.array.html#mlx.core.array), …), [array](mlx.core.array.html#mlx.core.array)]

** Contents
