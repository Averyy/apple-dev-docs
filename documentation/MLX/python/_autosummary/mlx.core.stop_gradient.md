---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.stop_gradient.html
---

# mlx.core.stop_gradient

```python
stop_gradient(a: array, /, *, stream: StreamOrDevice = None) → array
```

Stop gradients from being computed.

The operation is the identity but it prevents gradients from flowing
through the array.

**Parameters:**
: **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.

**Returns:**
: The unchanged input `a` but without gradient flowing
through it.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
