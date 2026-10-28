---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.sigmoid.html
---

# mlx.core.sigmoid

```python
sigmoid(a: array, /, *, stream: StreamOrDevice = None) → array
```

Element-wise logistic sigmoid.

The logistic sigmoid function is:

\[\mathrm{sigmoid}(x) = \frac{1}{1 + e^{-x}}\]

**Parameters:**
: **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.

**Returns:**
: The logistic sigmoid of `a`.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
