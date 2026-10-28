---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.split.html
---

# mlx.core.random.split

```python
split(key: array, num: int = 2, stream: StreamOrDevice = None) → array
```

Split a PRNG key into sub keys.

**Parameters:**

- **key** ([array](mlx.core.array.md#mlx.core.array)) – Input key to split.
- **num** ([int](https://docs.python.org/3/builtins/functions.html#int), *optional*) – Number of sub keys. Default: `2`.

**Returns:**
: The array of sub keys with `num` as its first dimension.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
