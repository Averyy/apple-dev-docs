---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.istft.html
---

# mlx.core.fft.istft

**istft(*stft_matrix: array*, *n_fft: int | None = None*, *hop_length: int | None = None*, *win_length: int | None = None*, *window: array | None = None*, *center: bool = True*, *norm: str = 'backward'*, *onesided: bool | None = None*, *length: int | None = None*, *stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None*) → [array](mlx.core.array.md#mlx.core.array)**
: Inverse Short-Time Fourier Transform.
Inverts [stft()](mlx.core.fft.stft.md#mlx.core.fft.stft) by overlap-adding the windowed inverse transform
of each frame, normalized by the squared-window envelope.

Parameters:

**stft_matrix** ([array](mlx.core.array.md#mlx.core.array)) – The STFT with shape `(..., n_freq, n_frames)`.
**n_fft** ([int](https://docs.python.org/3/builtins/functions.html#int)*, **optional*) – Size of the Fourier Transform. Default is
inferred from `n_freq` and `onesided`. The onesided inference
is even; pass `n_fft` for an odd transform size.
**hop_length** ([int](https://docs.python.org/3/builtins/functions.html#int)*, **optional*) – Samples between frames. Default is `n_fft // 4`.
**win_length** ([int](https://docs.python.org/3/builtins/functions.html#int)*, **optional*) – Window size. Default is `n_fft`.
**window** ([array](mlx.core.array.md#mlx.core.array)*, **optional*) – A one-dimensional window. Default is a
rectangular window.
**center** ([bool](https://docs.python.org/3/builtins/functions.html#bool)*, **optional*) – Whether the STFT was centered. Default is `True`.
**norm** ([str](https://docs.python.org/3/builtins/stdtypes.html#str)*, **optional*) – One of `"backward"`, `"ortho"`, or
`"forward"`. Default is `"backward"`.
**onesided** ([bool](https://docs.python.org/3/builtins/functions.html#bool)*, **optional*) – Whether the STFT has only non-negative
frequencies. Default is `True`.
**length** ([int](https://docs.python.org/3/builtins/functions.html#int)*, **optional*) – Trim or zero-pad the output to this length.

Returns:
The reconstructed signal.

Return type:
[array](mlx.core.array.md#mlx.core.array)
