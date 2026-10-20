---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.convolve.html
---

# mlx.core.convolve

**convolve(*a: array*, *v: array*, */*, *mode: str = 'full'*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.md#mlx.core.array)**
: The discrete convolution of 1D arrays.
If `v` is longer than `a`, then they are swapped.
The conv filter is flipped following signal processing convention.

Parameters:

**a** ([array](mlx.core.array.md#mlx.core.array)) – 1D Input array.
**v** ([array](mlx.core.array.md#mlx.core.array)) – 1D Input array.
**mode** ([str](https://docs.python.org/3/builtins/stdtypes.html#str)*, **optional*) – {‘full’, ‘valid’, ‘same’}

Returns:
The convolved array.

Return type:
[array](mlx.core.array.md#mlx.core.array)
