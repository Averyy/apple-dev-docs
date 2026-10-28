---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.reshape.html
---

# mlx.core.reshape

```python
reshape(a: array, /, shape: Sequence[int], *, stream: StreamOrDevice = None) → array
```

Reshape an array while preserving the size.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
- **shape** ([tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)([int](https://docs.python.org/3/builtins/functions.html#int))) – New shape.
- **stream** ([Stream](stream_class.md#mlx.core.Stream), *optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

**Returns:**
: The reshaped array.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
