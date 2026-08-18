---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.apply.html
---

# mlx.nn.Module.apply

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.apply.rst)
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

# mlx.nn.Module.apply

 Table of contents 

## Contents

# mlx.nn.Module.apply

**Module.apply(*map_fn: Callable[[array], array]*, *filter_fn: Callable[[Module, str, Any], bool] | None = None*) → [Module](../module.html#mlx.nn.Module)**
: Map all the parameters using the provided `map_fn` and immediately
update the module with the mapped parameters.
For instance running `model.apply(lambda x: x.astype(mx.float16))`
casts all parameters to 16 bit floats.

Parameters:

**map_fn** (*Callable*) – Maps an array to another array
**filter_fn** (*Callable**, **optional*) – Filter to select which arrays to
map (default: `Module.valid_parameter_filter()`).

Returns:
The module instance after updating the parameters.

** Contents
