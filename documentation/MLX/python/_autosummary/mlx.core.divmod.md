---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.divmod.html
---

# mlx.core.divmod

```python
divmod(a: scalar | array, b: scalar | array, stream: StreamOrDevice = None) → array
```

Element-wise quotient and remainder.

The fuction `divmod(a, b)` is equivalent to but faster than
`(a // b, a % b)`. The function uses numpy-style broadcasting
semantics. Either or both input arrays can also be scalars.

**Parameters:**

- **a** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.
- **b** ([array](mlx.core.array.md#mlx.core.array)) – Input array or scalar.

**Returns:**
: The quotient `a // b` and remainder `a % b`.

**Return type:**
: [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)([array](mlx.core.array.md#mlx.core.array), [array](mlx.core.array.md#mlx.core.array))
