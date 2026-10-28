---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.unstack.html
---

# mlx.core.unstack

```python
unstack(x: array, /, *, axis: int = 0, stream: StreamOrDevice = None) → tuple[array, ...]
```

Split an array into a sequence of arrays along the given axis.

The inverse of [stack()](mlx.core.stack.md#mlx.core.stack). The given axis is removed from each of
the returned arrays.

**Parameters:**

- **x** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
- **axis** ([int](https://docs.python.org/3/builtins/functions.html#int), *optional*) – Axis along which to unstack. Default: `0`.

**Returns:**
: A tuple of arrays, one for each index along `axis`.

**Return type:**
: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)([array](mlx.core.array.md#mlx.core.array))
