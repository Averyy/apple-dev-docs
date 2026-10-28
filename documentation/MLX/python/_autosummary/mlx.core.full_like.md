---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.full_like.html
---

# mlx.core.full_like

```python
full_like(a: array, vals: scalar | array, dtype: Dtype | None = None, *, stream: StreamOrDevice = None) → array
```

An array filled with `vals` with the same shape as the input.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – The input to take the shape from.
- **vals** ([float](https://docs.python.org/3/builtins/functions.html#float) *or* [int](https://docs.python.org/3/builtins/functions.html#int) *or* [array](mlx.core.array.md#mlx.core.array)) – Values to fill the array with.
- **dtype** ([Dtype](mlx.core.Dtype.md#mlx.core.Dtype), *optional*) – Data type of the output array. If
unspecified the type of the input is used.

**Returns:**
: The output array.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
