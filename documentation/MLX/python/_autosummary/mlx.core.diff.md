---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.diff.html
---

# mlx.core.diff

```python
diff(a: array, /, n: int = 1, axis: int = -1, *, stream: StreamOrDevice = None) → array
```

The n-th discrete difference along the given axis.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
- **n** ([int](https://docs.python.org/3/builtins/functions.html#int), *optional*) – The number of times to difference. Default: `1`.
- **axis** ([int](https://docs.python.org/3/builtins/functions.html#int), *optional*) – The axis along which to difference.
Default: `-1`.

**Returns:**
: The n-th differences.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
