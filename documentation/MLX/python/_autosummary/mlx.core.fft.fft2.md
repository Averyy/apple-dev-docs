---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.fft2.html
---

# mlx.core.fft.fft2

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.fft2.rst)
- **

.pdf

**

# mlx.core.fft.fft2

 Table of contents 

## Contents

# mlx.core.fft.fft2

**fft2(*a: array*, *s: tuple[int, ...] | None = None*, *axes: Sequence[int] | None = [-2, -1]*, *stream: Stream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Two dimensional discrete Fourier Transform.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**s** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Sizes of the transformed axes. The
corresponding axes in the input are truncated or padded with
zeros to match the sizes in `s`. The default value is the
sizes of `a` along `axes`.
**axes** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Axes along which to perform the FFT.
The default is `[-2, -1]`.

Returns:
The DFT of the input along the given axes.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
