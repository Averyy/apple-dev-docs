---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.not_equal.html
---

# mlx.core.not_equal

```python
not_equal(a: scalar | array, b: scalar | array, stream: StreamOrDevice = None) → array
```

Element-wise not equal.

Not equal comparison on two arrays with numpy-style broadcasting semantics.
Either or both input arrays can also be scalars.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.
- **b** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.

**Returns:**
: The element-wise comparison `a != b`.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
