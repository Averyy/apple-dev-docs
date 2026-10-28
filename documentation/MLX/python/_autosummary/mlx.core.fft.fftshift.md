---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fft.fftshift.html
---

# mlx.core.fft.fftshift

```python
fftshift(a: array, axes: int | Sequence[int] | None = None, stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None) → array
```

Shift the zero-frequency component to the center of the spectrum.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – The input array.
- **axes** ([int](https://docs.python.org/3/builtins/functions.html#int) *or* [list](https://docs.python.org/3/builtins/stdtypes.html#list)([int](https://docs.python.org/3/builtins/functions.html#int)), *optional*) – Axis or axes over which to perform the shift.
If `None`, shift all axes.

**Returns:**
: The shifted array with the same shape as the input.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
