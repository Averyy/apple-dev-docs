---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.rfftn.html
---

# mlx.core.fft.rfftn

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.rfftn.rst)
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

# mlx.core.fft.rfftn

 Table of contents 

## Contents

# mlx.core.fft.rfftn

**rfftn(*a: array*, *s: tuple[int, ...] | None = None*, *axes: Sequence[int] | None = None*, *norm: str = 'backward'*, *stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: n-dimensional real discrete Fourier Transform.
The output has the same shape as the input except along the dimensions in
`axes` in which case it has sizes from `s`. The last axis in `axes` is
treated as the real axis and will have size `s[-1] // 2 + 1`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array. If the array is complex it will be silently
cast to a real type.
**s** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Sizes of the transformed axes. The
corresponding axes in the input are truncated or padded with
zeros to match the sizes in `s`. The default value is the
sizes of `a` along `axes`.
**axes** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Axes along which to perform the FFT.
The default is `None` in which case the FFT is over the last
`len(s)` axes or all axes if `s` is also `None`.
**norm** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – One of `"backward"`, `"ortho"`, or
`"forward"`. Default is `"backward"`.

Returns:
The real DFT of the input along the given axes. The output
data type will be complex.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
