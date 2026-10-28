---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.hanning.html
---

# mlx.core.hanning

```python
hanning(M: int, *, stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None) → array
```

Return the Hanning window.

The Hanning window is a taper formed by using a weighted cosine.

\[w(n) = 0.5 - 0.5 \cos\left(\frac{2\pi n}{M-1}\right)
 \qquad 0 \le n \le M-1\]

**Parameters:**
: **M** ([int](https://docs.python.org/3/builtins/functions.html#int)) – Number of points in the output window.

**Returns:**
: The window, with the maximum value normalized to one (the value oneappears only if the number of samples is odd).

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
