---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.orthogonal.html
---

# mlx.nn.init.orthogonal

```python
orthogonal(gain: float = 1.0, dtype: Dtype = mlx.core.float32) → Callable[[array], array]
```

An initializer that returns an orthogonal matrix.

**Parameters:**

- **gain** ([float](https://docs.python.org/3/builtins/functions.html#float), *optional*) – Scaling factor for the orthogonal matrix.
Default: `1.0`.
- **dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.md#mlx.core.Dtype), *optional*) – Data type of the array. Default: `float32`.

**Returns:**
: An initializer that returns
an orthogonal matrix with the same shape as the input.

**Return type:**
: *Callable*[[[array](../../_autosummary/mlx.core.array.md#mlx.core.array)], [array](../../_autosummary/mlx.core.array.md#mlx.core.array)]
