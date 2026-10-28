---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.broadcast_arrays.html
---

# mlx.core.broadcast_arrays

```python
broadcast_arrays(*arrays: array, stream: StreamOrDevice = None) → tuple[array, ...]
```

Broadcast arrays against one another.

The broadcasting semantics are the same as Numpy.

**Parameters:**
: **\*arrays** ([array](mlx.core.array.md#mlx.core.array)) – The input arrays.

**Returns:**
: The output arrays with the broadcasted shape.

**Return type:**
: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)([array](mlx.core.array.md#mlx.core.array))
