---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.identity.html
---

# mlx.nn.init.identity

```python
identity(dtype: Dtype = mlx.core.float32) → Callable[[array], array]
```

An initializer that returns an identity matrix.

**Parameters:**
: **dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.md#mlx.core.Dtype), *optional*) – The data type of the array. Default:
`float32`.

**Returns:**
: An initializer that returns an identity
matrix with the same shape as the input.

**Return type:**
: *Callable*[[[array](../../_autosummary/mlx.core.array.md#mlx.core.array)], [array](../../_autosummary/mlx.core.array.md#mlx.core.array)]

Example

```
>>> init_fn = nn.init.identity()
>>> init_fn(mx.zeros((2, 2)))
array([[1, 0],
       [0, 1]], dtype=float32)
```
