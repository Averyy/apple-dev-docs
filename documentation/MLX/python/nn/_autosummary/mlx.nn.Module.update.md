---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.update.html
---

# mlx.nn.Module.update

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.update.rst)
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

# mlx.nn.Module.update

 Table of contents 

## Contents

# mlx.nn.Module.update

**Module.update(*parameters: dict*, *strict: bool = True*) → [Module](../module.html#mlx.nn.Module)**
: Replace the parameters of this Module with the provided ones in the
dict of dicts and lists.
Commonly used by the optimizer to change the model to the updated
(optimized) parameters. Also used by the [mlx.nn.value_and_grad()](../../_autosummary/mlx.nn.value_and_grad.html#mlx.nn.value_and_grad) to set the
tracers in the model in order to compute gradients.
The passed in parameters dictionary need not be a full dictionary
similar to [parameters()](mlx.nn.Module.parameters.html#mlx.nn.Module.parameters). Only the provided locations will be
updated.

Parameters:

**parameters** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – A complete or partial dictionary of the modules
parameters.
**strict** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If `True` checks that `parameters` is a
subset of the module’s parameters. Default: `True`.

Returns:
The module instance after updating the parameters.

** Contents
