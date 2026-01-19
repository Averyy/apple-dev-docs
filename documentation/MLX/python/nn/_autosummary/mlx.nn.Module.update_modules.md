---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.update_modules.html
---

# mlx.nn.Module.update_modules

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.update_modules.rst)
- **

.pdf

**

# mlx.nn.Module.update_modules

 Table of contents 

## Contents

# mlx.nn.Module.update_modules

**Module.update_modules(*modules: dict*, *strict: bool = True*) → [Module](../module.html#mlx.nn.Module)**
: Replace the child modules of this [Module](../module.html#mlx.nn.Module) instance with the
provided ones in the dict of dicts and lists.
It is the equivalent of [Module.update()](mlx.nn.Module.update.html#mlx.nn.Module.update) but for modules instead
of parameters and allows us to flexibly edit complex architectures by
programmatically swapping layers.
The passed in parameters dictionary need not be a full dictionary
similar to [modules()](mlx.nn.Module.modules.html#mlx.nn.Module.modules). Only the provided locations will be
updated.

Parameters:

**modules** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – A complete or partial dictionary of the module’s
submodules.
**strict** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If `True` checks that `modules` is a
subset of the child modules of this instance. Default: `True`.

Returns:
The module instance after updating the submodules.

** Contents
