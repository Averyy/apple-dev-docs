---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.less.html
---

# mlx.core.less

**less(*a: scalar | array*, *b: scalar | array*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.md#mlx.core.array)**
: Element-wise less than.
Strict less than on two arrays with numpy-style broadcasting semantics.
Either or both input arrays can also be scalars.

Parameters:

**a** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.
**b** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.

Returns:
The element-wise comparison `a < b`.

Return type:
[array](mlx.core.array.md#mlx.core.array)
