---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.logaddexp.html
---

# mlx.core.logaddexp

```python
logaddexp(a: scalar | array, b: scalar | array, /, *, stream: StreamOrDevice = None) → array
```

Element-wise log-add-exp.

This is a numerically stable log-add-exp of two arrays with numpy-style
broadcasting semantics. Either or both input arrays can also be scalars.

The computation is a numerically stable version of `log(exp(a) + exp(b))`.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.
- **b** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.

**Returns:**
: The log-add-exp of `a` and `b`.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
