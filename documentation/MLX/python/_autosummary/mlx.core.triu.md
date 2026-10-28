---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.triu.html
---

# mlx.core.triu

```python
triu(x: array, k: int = 0, *, stream: StreamOrDevice = None) → array
```

Zeros the array below the given diagonal.

**Parameters:**

- **x** ([array](mlx.core.array.md#mlx.core.array)) – input array.
- **k** ([int](https://docs.python.org/3/builtins/functions.html#int), *optional*) – The diagonal of the 2-D array. Defaults to `0`.
- **stream** ([Stream](stream_class.md#mlx.core.Stream), *optional*) – Stream or device. Defaults to `None`.

**Returns:**
: Array zeroed below the given diagonal

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
