---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.config.get.html
---

# mlx.core.config.get

```python
get(name: str, default_value: int) → int
```

Read the value of a configuration. The lookup order is:

1. The value set by [mlx.core.config.scoped_update()](mlx.core.config.scoped_update.md#mlx.core.config.scoped_update).
2. The value set by [mlx.core.config.update()](mlx.core.config.update.md#mlx.core.config.update).
3. The environment variable.
4. The `default_value`.

See [Environment Variables](../../usage/environment_variables.md#environment-variables) for available configurations.

**Parameters:**

- **name** ([str](https://docs.python.org/3/builtins/stdtypes.html#str)) – Name of configuration.
- **default_value** ([int](https://docs.python.org/3/builtins/functions.html#int)) – Fallback value to return when not set.
