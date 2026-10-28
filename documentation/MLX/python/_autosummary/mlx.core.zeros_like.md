---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.zeros_like.html
---

# mlx.core.zeros_like

```python
zeros_like(a: array, /, dtype: Dtype | None = None, *, stream: StreamOrDevice = None) → array
```

An array of zeros like the input.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – The input to take the shape from.
- **dtype** ([Dtype](mlx.core.Dtype.md#mlx.core.Dtype), *optional*) – Output data type. If `None`, the output
type defaults to the input array’s data type.

**Returns:**
: The output array filled with zeros.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
