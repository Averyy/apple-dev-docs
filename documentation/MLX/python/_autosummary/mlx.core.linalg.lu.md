---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.lu.html
---

# mlx.core.linalg.lu

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.lu.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.linalg.lu

 Table of contents 

## Contents

# mlx.core.linalg.lu

**lu(*a: array*, ***, *stream: None | Stream | Device = None*) → Tuple[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]**
: Compute the LU factorization of the given matrix `A`.
Note, unlike the default behavior of `scipy.linalg.lu`, the pivots
are indices. To reconstruct the input use `L[P, :] @ U` for 2
dimensions or `mx.take_along_axis(L, P[..., None], axis=-2) @ U`
for more than 2 dimensions.
To construct the full permuation matrix do:
P = mx.put_along_axis(mx.zeros_like(L), p[..., None], mx.array(1.0), axis=-1)

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The `p`, `L`, and `U` arrays, such that `A = L[P, :] @ U`

Return type:
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array))

** Contents
