---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.round.html
---

# mlx.core.round

```python
round(a: array, /, decimals: int = 0, stream: StreamOrDevice = None) → array
```

Round to the given number of decimals.

Basically performs:

```
s = 10**decimals
x = round(x * s) / s
```

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array
- **decimals** ([int](https://docs.python.org/3/builtins/functions.html#int)) – Number of decimal places to round to. (default: 0)

**Returns:**
: An array of the same type as `a` rounded to the
given number of decimals.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
