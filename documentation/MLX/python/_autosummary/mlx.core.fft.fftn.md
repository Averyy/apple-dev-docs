---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.fftn.html
---

# mlx.core.fft.fftn

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.fftn.rst)
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

# mlx.core.fft.fftn

 Table of contents 

## Contents

# mlx.core.fft.fftn

**fftn(*a: array*, *s: tuple[int, ...] | None = None*, *axes: Sequence[int] | None = None*, *norm: str = 'backward'*, *stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: n-dimensional discrete Fourier Transform.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**s** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Sizes of the transformed axes. The
corresponding axes in the input are truncated or padded with
zeros to match the sizes in `s`. The default value is the
sizes of `a` along `axes`.
**axes** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Axes along which to perform the FFT.
The default is `None` in which case the FFT is over the last
`len(s)` axes are or all axes if `s` is also `None`.
**norm** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – One of `"backward"`, `"ortho"`, or
`"forward"`. Default is `"backward"`.

Returns:
The DFT of the input along the given axes.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
