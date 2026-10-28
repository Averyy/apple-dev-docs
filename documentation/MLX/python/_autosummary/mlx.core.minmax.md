---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.minmax.html
---

# mlx.core.minmax

```python
minmax(a: array, /, axis: None | int | Sequence[int] = None, keepdims: bool = False, *, stream: StreamOrDevice = None) → tuple[array, array]
```

Return the minimum and maximum over the given axes.

Equivalent to calling [min()](mlx.core.min.md#mlx.core.min) and [max()](mlx.core.max.md#mlx.core.max) separately.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
- **axis** ([int](https://docs.python.org/3/builtins/functions.html#int) *or* [list](https://docs.python.org/3/builtins/stdtypes.html#list)([int](https://docs.python.org/3/builtins/functions.html#int)), *optional*) – Axis or axes to reduce over.
If unspecified, reduce over the entire array.
- **keepdims** ([bool](https://docs.python.org/3/builtins/functions.html#bool), *optional*) – Keep reduced axes as singleton
dimensions. Default: `False`.

**Returns:**
: The minimum and maximum arrays, in that order.

**Return type:**
: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)([array](mlx.core.array.md#mlx.core.array), [array](mlx.core.array.md#mlx.core.array))
