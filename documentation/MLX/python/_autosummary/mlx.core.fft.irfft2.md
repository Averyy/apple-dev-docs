---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.irfft2.html
---

# mlx.core.fft.irfft2

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.irfft2.rst)
- **

.pdf

**

# mlx.core.fft.irfft2

 Table of contents 

## Contents

# mlx.core.fft.irfft2

**irfft2(*a: array*, *s: tuple[int, ...] | None = None*, *axes: Sequence[int] | None = [-2, -1]*, *stream: Stream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: The inverse of [rfft2()](mlx.core.fft.rfft2.html#mlx.core.fft.rfft2).
Note the input is generally complex. The dimensions of the input
specified in `axes` are padded or truncated to match the sizes
from `s`. The last axis in `axes` is treated as the real axis
and will have size `s[-1] // 2 + 1`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**s** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Sizes of the transformed axes. The
corresponding axes in the input are truncated or padded with
zeros to match the sizes in `s` except for the last axis
which has size `s[-1] // 2 + 1`. The default value is the
sizes of `a` along `axes`.
**axes** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Axes along which to perform the FFT.
The default is `[-2, -1]`.

Returns:
The real array containing the inverse of [rfft2()](mlx.core.fft.rfft2.html#mlx.core.fft.rfft2).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
