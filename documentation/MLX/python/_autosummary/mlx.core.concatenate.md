---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.concatenate.html
---

# mlx.core.concatenate

```python
concatenate(arrays: list[array], axis: int | None = 0, *, stream: StreamOrDevice = None) → array
```

Concatenate the arrays along the given axis.

**Parameters:**

- **arrays** ([list](https://docs.python.org/3/builtins/stdtypes.html#list)([array](mlx.core.array.md#mlx.core.array))) – Input [list](https://docs.python.org/3/builtins/stdtypes.html#list) or [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple) of arrays.
- **axis** ([int](https://docs.python.org/3/builtins/functions.html#int), *optional*) – Optional axis to concatenate along. If
unspecified defaults to `0`.

**Returns:**
: The concatenated array.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
