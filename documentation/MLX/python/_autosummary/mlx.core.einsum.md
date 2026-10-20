---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.einsum.html
---

# mlx.core.einsum

**einsum(*subscripts: str*, **operands*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.md#mlx.core.array)**
: Perform the Einstein summation convention on the operands.
Contractions are implemented with [matmul()](mlx.core.matmul.md#mlx.core.matmul) and have the same
requirements.

Parameters:

**subscripts** ([str](https://docs.python.org/3/builtins/stdtypes.html#str)) – The Einstein summation convention equation.
***operands** ([array](mlx.core.array.md#mlx.core.array)) – The input arrays.

Returns:
The output array.

Return type:
[array](mlx.core.array.md#mlx.core.array)
