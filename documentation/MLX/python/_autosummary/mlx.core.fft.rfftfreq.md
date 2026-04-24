---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.rfftfreq.html
---

# mlx.core.fft.rfftfreq

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.rfftfreq.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.fft.rfftfreq

 Table of contents 

## Contents

# mlx.core.fft.rfftfreq

**rfftfreq(*n: int*, *d: float = 1.0*, *stream: Stream | mlx.core.ThreadLocalStream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the discrete Fourier Transform sample frequencies
for use with [rfft()](mlx.core.fft.rfft.html#mlx.core.fft.rfft) and [irfft()](mlx.core.fft.irfft.html#mlx.core.fft.irfft).
The returned array contains the non-negative frequency terms
in the range `[0, floor(n/2)]`.

Parameters:

**n** ([int](https://docs.python.org/3/library/functions.html#int)) – Window length.
**d** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Sample spacing. The default is `1.0`.

Returns:
The sample frequencies as a one-dimensional array of type `float32`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
