---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.load_weights.html
---

# mlx.nn.Module.load_weights

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Module.load_weights.rst)
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

# mlx.nn.Module.load_weights

 Table of contents 

## Contents

# mlx.nn.Module.load_weights

**Module.load_weights(*file_or_weights: str | List[Tuple[str, array]]*, *strict: bool = True*) → [Module](../module.html#mlx.nn.Module)**
: Update the model’s weights from a `.npz`, a `.safetensors` file, or a list.

Parameters:

**file_or_weights** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[array](../../_autosummary/mlx.core.array.html#mlx.core.array)*)**)*) – The path to
the weights `.npz` file (`.npz` or `.safetensors`) or a list
of pairs of parameter names and arrays.
**strict** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True` then checks that the provided
weights exactly match the parameters of the model. Otherwise,
only the weights actually contained in the model are loaded and
shapes are not checked. Default: `True`.

Returns:
The module instance after updating the weights.

Example
import mlx.core as mx
import mlx.nn as nn
model = nn.Linear(10, 10)

# Load from file
model.load_weights("weights.npz")

# Load from .safetensors file
model.load_weights("weights.safetensors")

# Load from list
weights = [
    ("weight", mx.random.uniform(shape=(10, 10))),
    ("bias",  mx.zeros((10,))),
]
model.load_weights(weights)

# Missing weight
weights = [
    ("weight", mx.random.uniform(shape=(10, 10))),
]

# Raises a ValueError exception
model.load_weights(weights)

# Ok, only updates the weight but not the bias
model.load_weights(weights, strict=False)

** Contents
