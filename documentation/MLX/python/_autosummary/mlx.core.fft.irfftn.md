---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.irfftn.html
---

# mlx.core.fft.irfftn

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.irfftn.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.fft.irfftn

 Table of contents 

## Contents

# mlx.core.fft.irfftn

**irfftn(*a: array*, *s: tuple[int, ...] | None = None*, *axes: Sequence[int] | None = None*, *norm: str = 'backward'*, *stream: Stream | mlx.core.ThreadLocalStream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: The inverse of [rfftn()](mlx.core.fft.rfftn.html#mlx.core.fft.rfftn).
Note the input is generally complex. The dimensions of the input
specified in `axes` are padded or truncated to match the sizes
from `s`. The last axis in `axes` is treated as the real axis
and will have size `s[-1] // 2 + 1`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
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
The real array containing the inverse of [rfftn()](mlx.core.fft.rfftn.html#mlx.core.fft.rfftn).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
