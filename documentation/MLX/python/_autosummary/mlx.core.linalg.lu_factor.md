---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.lu_factor.html
---

# mlx.core.linalg.lu_factor

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.lu_factor.rst)
- **

.pdf

**

# mlx.core.linalg.lu_factor

 Table of contents 

## Contents

# mlx.core.linalg.lu_factor

**lu_factor(*a: array*, ***, *stream: None | Stream | Device = None*) → Tuple[[array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array)]**
: Computes a compact representation of the LU factorization.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The `LU` matrix and `pivots` array.

Return type:
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([array](mlx.core.array.html#mlx.core.array), [array](mlx.core.array.html#mlx.core.array))

** Contents
