---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.ifft.html
---

# mlx.core.fft.ifft

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.ifft.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.fft.ifft

 Table of contents 

## Contents

# mlx.core.fft.ifft

**ifft(*a: array*, *n: int | None = None*, *axis: int = -1*, *norm: str = 'backward'*, *stream: Stream | mlx.core.ThreadLocalStream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: One dimensional inverse discrete Fourier Transform.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**n** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Size of the transformed axis. The
corresponding axis in the input is truncated or padded with
zeros to match `n`. The default value is `a.shape[axis]`.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Axis along which to perform the FFT. The
default is `-1`.
**norm** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – One of `"backward"`, `"ortho"`, or
`"forward"`. Default is `"backward"`.

Returns:
The inverse DFT of the input along the given axis.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
