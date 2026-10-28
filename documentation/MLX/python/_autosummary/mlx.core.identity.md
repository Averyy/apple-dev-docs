---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.identity.html
---

# mlx.core.identity

```python
identity(n: int, dtype: Dtype | None = float32, *, stream: StreamOrDevice = None) → array
```

Create a square identity matrix.

**Parameters:**

- **n** ([int](https://docs.python.org/3/builtins/functions.html#int)) – The number of rows and columns in the output.
- **dtype** ([Dtype](mlx.core.Dtype.md#mlx.core.Dtype), *optional*) – Data type of the output array. Defaults to float32.
- **stream** ([Stream](stream_class.md#mlx.core.Stream), *optional*) – Stream or device. Defaults to None.

**Returns:**
: An identity matrix of size n x n.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
