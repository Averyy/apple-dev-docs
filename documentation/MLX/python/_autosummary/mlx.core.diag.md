---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.diag.html
---

# mlx.core.diag

```python
diag(a: array, /, k: int = 0, *, stream: StreamOrDevice = None) → array
```

Extract a diagonal or construct a diagonal matrix.
If `a` is 1-D then a diagonal matrix is constructed with `a` on the
\(k\)-th diagonal. If `a` is 2-D then the \(k\)-th diagonal is
returned.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – 1-D or 2-D input array.
- **k** ([int](https://docs.python.org/3/builtins/functions.html#int), *optional*) – The diagonal to extract or construct.
Default: `0`.

**Returns:**
: The extracted diagonal or the constructed diagonal matrix.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
