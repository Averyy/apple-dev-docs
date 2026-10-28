---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.stack.html
---

# mlx.core.stack

```python
stack(arrays: list[array], axis: int | None = 0, *, stream: StreamOrDevice = None) → array
```

Stacks the arrays along a new axis.

**Parameters:**

- **arrays** ([list](https://docs.python.org/3/builtins/stdtypes.html#list)([array](mlx.core.array.md#mlx.core.array))) – A list of arrays to stack.
- **axis** ([int](https://docs.python.org/3/builtins/functions.html#int), *optional*) – The axis in the result array along which the
input arrays are stacked. Defaults to `0`.
- **stream** ([Stream](stream_class.md#mlx.core.Stream), *optional*) – Stream or device. Defaults to `None`.

**Returns:**
: The resulting stacked array.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
