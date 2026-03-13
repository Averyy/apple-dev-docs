---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.freeze.html
---

# mlx.nn.Module.freeze

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.freeze.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.Module.freeze

 Table of contents 

## Contents

# mlx.nn.Module.freeze

**Module.freeze(***, *recurse: bool = True*, *keys: str | List[str] | None = None*, *strict: bool = False*) → [Module](../module.html#mlx.nn.Module)**
: Freeze the Module’s parameters or some of them. Freezing a parameter means not
computing gradients for it.
This function is idempotent i.e. freezing a frozen model is a no-op.
Example
For instance to only train the attention parameters from a Transformer:
model = nn.Transformer()
model.freeze()
model.apply_to_modules(lambda k, v: v.unfreeze() if k.endswith("attention") else None)

Parameters:

**recurse** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If True then freeze the parameters of the
submodules as well. Default: `True`.
**keys** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]**, **optional*) – If provided then only these
parameters will be frozen otherwise all the parameters of a
module. For instance freeze all biases by calling
`module.freeze(keys="bias")`.
**strict** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `True` validate that the passed keys exist.
Default: `False`.

Returns:
The module instance after freezing the parameters.

** Contents
