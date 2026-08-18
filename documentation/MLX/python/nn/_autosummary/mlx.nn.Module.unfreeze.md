---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.unfreeze.html
---

# mlx.nn.Module.unfreeze

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.unfreeze.rst)
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

# mlx.nn.Module.unfreeze

 Table of contents 

## Contents

# mlx.nn.Module.unfreeze

**Module.unfreeze(***, *recurse: bool = True*, *keys: str | List[str] | None = None*, *strict: bool = False*) → [Module](../module.html#mlx.nn.Module)**
: Unfreeze the Module’s parameters or some of them.
This function is idempotent ie unfreezing a model that is not frozen is
a noop.
Example
For instance to only train the biases of a Transformer one can do:
model = nn.Transformer()
model.freeze()
model.unfreeze(keys="bias")

Parameters:

**recurse** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If True then unfreeze the parameters of the
submodules as well. Default: `True`.
**keys** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]**, **optional*) – If provided then only these
parameters will be unfrozen otherwise all the parameters of a
module. For instance unfreeze all biases by calling
`module.unfreeze(keys="bias")`.
**strict** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `True` validate that the passed keys exist.
Default: `False`.

Returns:
The module instance after unfreezing the parameters.

** Contents
