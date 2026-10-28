---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.is_available.html
---

# mlx.core.distributed.is_available

```python
is_available(backend: str = 'any') → bool
```

Check if a communication backend is available.

Note, this function returns whether MLX has the capability of
instantiating that distributed backend not whether it is possible to
create a communication group. For that purpose one should use
`init(strict=True)`.

**Parameters:**
: **backend** ([str](https://docs.python.org/3/builtins/stdtypes.html#str), *optional*) – The name of the backend to check for availability.
It takes the same values as [init()](mlx.core.distributed.init.md#mlx.core.distributed.init). Default: `"any"`.

**Returns:**
: Whether the distributed backend is available.

**Return type:**
: [bool](https://docs.python.org/3/builtins/functions.html#bool)
