---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.lu_factor.html
---

# mlx.core.linalg.lu_factor

**lu_factor(*a: array*, ***, *stream: StreamOrDevice = None*) → [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[array](mlx.core.array.md#mlx.core.array), [array](mlx.core.array.md#mlx.core.array)]**
: Computes a compact representation of the LU factorization.

Parameters:

**a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.md#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The `LU` matrix and `pivots` array.

Return type:
[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)([array](mlx.core.array.md#mlx.core.array), [array](mlx.core.array.md#mlx.core.array))
