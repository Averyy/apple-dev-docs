---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.filter_and_map.html
---

# mlx.nn.Module.filter_and_map

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.filter_and_map.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.nn.Module.filter_and_map

 Table of contents 

## Contents

# mlx.nn.Module.filter_and_map

**Module.filter_and_map(*filter_fn: Callable[[Module, str, Any], bool]*, *map_fn: Callable | None = None*, *is_leaf_fn: Callable[[Module, str, Any], bool] | None = None*)**
: Recursively filter the contents of the module using `filter_fn`,
namely only select keys and values where `filter_fn` returns true.
This is used to implement [parameters()](mlx.nn.Module.parameters.html#mlx.nn.Module.parameters) and [trainable_parameters()](mlx.nn.Module.trainable_parameters.html#mlx.nn.Module.trainable_parameters)
but it can also be used to extract any subset of the module’s parameters.

Parameters:

**filter_fn** (*Callable*) – Given the containing module, the key in which
it is found and the value, decide whether to keep the value or
drop it.
**map_fn** (*Callable**, **optional*) – Optionally transform the value before
returning it.
**is_leaf_fn** (*Callable**, **optional*) – Given the containing module, the
key in which it is found and the value decide if it is a leaf.

Returns:
A dictionary containing the contents of the module recursively filtered

** Contents
