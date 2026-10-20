---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.transpose.html
---

# mlx.core.transpose

**transpose(*a: array*, */*, *axes: Sequence[int] | None = None*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.md#mlx.core.array)**
: Transpose the dimensions of the array.

Parameters:

**a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
**axes** ([list](https://docs.python.org/3/builtins/stdtypes.html#list)*(*[int](https://docs.python.org/3/builtins/functions.html#int)*)**, **optional*) – Specifies the source axis for each axis
in the new array. The default is to reverse the axes.

Returns:
The transposed array.

Return type:
[array](mlx.core.array.md#mlx.core.array)
