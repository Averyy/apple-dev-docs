---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.irfft.html
---

# mlx.core.fft.irfft

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.irfft.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.core.fft.irfft

 Table of contents 

## Contents

# mlx.core.fft.irfft

**irfft(*a: array*, *n: int | None = None*, *axis: int = -1*, *norm: str = 'backward'*, *stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: The inverse of [rfft()](mlx.core.fft.rfft.html#mlx.core.fft.rfft).
The output has the same shape as the input except along `axis` in
which case it has size `n`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**n** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Size of the transformed axis. The
corresponding axis in the input is truncated or padded with
zeros to match `n // 2 + 1`. The default value is
`a.shape[axis] // 2 + 1`.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Axis along which to perform the FFT. The
default is `-1`.
**norm** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – One of `"backward"`, `"ortho"`, or
`"forward"`. Default is `"backward"`.

Returns:
The real array containing the inverse of [rfft()](mlx.core.fft.rfft.html#mlx.core.fft.rfft).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
