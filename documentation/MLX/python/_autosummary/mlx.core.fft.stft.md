---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.stft.html
---

# mlx.core.fft.stft

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fft.stft.rst)
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

# mlx.core.fft.stft

 Table of contents 

## Contents

# mlx.core.fft.stft

**stft(*x: array*, *n_fft: int = 2048*, *hop_length: int | None = None*, *win_length: int | None = None*, *window: array | None = None*, *center: bool = True*, *pad_mode: str = 'reflect'*, *norm: str = 'backward'*, *onesided: bool | None = None*, *stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Short-Time Fourier Transform.
Splits the last axis of `x` into overlapping frames of length
`n_fft`, applies `window`, and takes the Fourier Transform of each
frame. The output is always complex with shape `(..., n_freq, n_frames)`.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**n_fft** ([int](https://docs.python.org/3/builtins/functions.html#int)*, **optional*) – Size of the Fourier Transform. Default is `2048`.
**hop_length** ([int](https://docs.python.org/3/builtins/functions.html#int)*, **optional*) – Samples between frames. Default is `n_fft // 4`.
**win_length** ([int](https://docs.python.org/3/builtins/functions.html#int)*, **optional*) – Window size. Default is `n_fft`.
**window** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A one-dimensional window, centered and
zero-padded to `n_fft`. Default is a rectangular window.
**center** ([bool](https://docs.python.org/3/builtins/functions.html#bool)*, **optional*) – Pad both ends so frames are centered. Default is `True`.
**pad_mode** ([str](https://docs.python.org/3/builtins/stdtypes.html#str)*, **optional*) – One of `"reflect"`, `"constant"`, or
`"edge"`, used when `center` is `True`. Default is `"reflect"`.
**norm** ([str](https://docs.python.org/3/builtins/stdtypes.html#str)*, **optional*) – One of `"backward"`, `"ortho"`, or
`"forward"`. Default is `"backward"`.
**onesided** ([bool](https://docs.python.org/3/builtins/functions.html#bool)*, **optional*) – Return only non-negative frequencies.
Default is `True` for real input and `False` for complex input.

Returns:
The STFT of `x`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
