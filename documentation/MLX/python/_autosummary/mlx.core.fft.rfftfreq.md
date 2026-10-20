---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.rfftfreq.html
---

# mlx.core.fft.rfftfreq

**rfftfreq(*n: int*, *d: float = 1.0*, *stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None*) → [array](mlx.core.array.md#mlx.core.array)**
: Return the discrete Fourier Transform sample frequencies
for use with [rfft()](mlx.core.fft.rfft.md#mlx.core.fft.rfft) and [irfft()](mlx.core.fft.irfft.md#mlx.core.fft.irfft).
The returned array contains the non-negative frequency terms
in the range `[0, floor(n/2)]`.

Parameters:

**n** ([int](https://docs.python.org/3/builtins/functions.html#int)) – Window length.
**d** ([float](https://docs.python.org/3/builtins/functions.html#float)*, **optional*) – Sample spacing. The default is `1.0`.

Returns:
The sample frequencies as a one-dimensional array of type `float32`.

Return type:
[array](mlx.core.array.md#mlx.core.array)
