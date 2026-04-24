---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.ifftshift.html
---

# mlx.core.fft.ifftshift

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.ifftshift.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.fft.ifftshift

 Table of contents 

## Contents

# mlx.core.fft.ifftshift

**ifftshift(*a: array*, *axes: int | Sequence[int] | None = None*, *stream: Stream | mlx.core.ThreadLocalStream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: The inverse of [fftshift()](mlx.core.fft.fftshift.html#mlx.core.fft.fftshift). While identical to [fftshift()](mlx.core.fft.fftshift.html#mlx.core.fft.fftshift) for even-length axes,
the behavior differs for odd-length axes.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**axes** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Axis or axes over which to perform the inverse shift.
If `None`, shift all axes.

Returns:
The inverse-shifted array with the same shape as the input.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
