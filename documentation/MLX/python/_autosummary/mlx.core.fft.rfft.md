---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.rfft.html
---

# mlx.core.fft.rfft

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.rfft.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.fft.rfft

 Table of contents 

## Contents

# mlx.core.fft.rfft

**rfft(*a: array*, *n: int | None = None*, *axis: int = -1*, *stream: Stream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: One dimensional discrete Fourier Transform on a real input.
The output has the same shape as the input except along `axis` in
which case it has size `n // 2 + 1`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array. If the array is complex it will be silently
cast to a real type.
**n** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Size of the transformed axis. The
corresponding axis in the input is truncated or padded with
zeros to match `n`. The default value is `a.shape[axis]`.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Axis along which to perform the FFT. The
default is `-1`.

Returns:
The DFT of the input along the given axis. The output
data type will be complex.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
