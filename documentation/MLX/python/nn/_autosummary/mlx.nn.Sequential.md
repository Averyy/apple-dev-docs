---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Sequential.html
---

# mlx.nn.Sequential

```python
class Sequential(*modules)
```

A layer that calls the passed callables in order.

We can pass either modules or plain callables to the Sequential module. If
our functions have learnable parameters they should be implemented as
`nn.Module` instances.

**Parameters:**
: **modules** ([tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple) *of* *Callables*) – The modules to call in order

Methods
