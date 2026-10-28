---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.left_shift.html
---

# mlx.core.left_shift

```python
left_shift(a: scalar | array, b: scalar | array, stream: StreamOrDevice = None) → array
```

Element-wise left shift.

Shift the bits of the first input to the left by the second using
numpy-style broadcasting semantics. Either or both input arrays can
also be scalars.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.
- **b** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.

**Returns:**
: The bitwise left shift `a << b`.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
