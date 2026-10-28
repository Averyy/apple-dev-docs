---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.apply_to_modules.html
---

# mlx.nn.Module.apply_to_modules

```python
Module.apply_to_modules(apply_fn: Callable[[str, Module], Any]) → Module
```

Apply a function to all the modules in this instance (including this
instance).

**Parameters:**
: **apply_fn** (*Callable*) – The function to apply to the modules which
takes two parameters. The first parameter is the string path of
the module (e.g. `"model.layers.0.linear"`). The second
parameter is the module object.

**Returns:**
: The module instance after updating submodules.
