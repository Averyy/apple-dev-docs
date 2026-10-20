---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.floor_divide.html
---

# mlx.core.floor_divide

**floor_divide(*a: scalar | array*, *b: scalar | array*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.md#mlx.core.array)**
: Element-wise integer division.
If either array is a floating point type then it is equivalent to
calling [floor()](mlx.core.floor.md#mlx.core.floor) after [divide()](mlx.core.divide.md#mlx.core.divide).

Parameters:

**a** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.
**b** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.

Returns:
The quotient `a // b`.

Return type:
[array](mlx.core.array.md#mlx.core.array)
