---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Module.train.html
---

# mlx.nn.Module.train

**Module.train(*mode: bool = True*) → [Module](../module.md#mlx.nn.Module)**
: Set the model in or out of training mode.
Training mode only applies to certain layers. For example
[Dropout](mlx.nn.Dropout.md#mlx.nn.Dropout) applies a random mask in training mode, but is the
identity in evaluation mode.

Parameters:
**mode** ([bool](https://docs.python.org/3/builtins/functions.html#bool)) – Indicate if the model should be in training or
evaluation mode. Default: `True`.

Returns:
The module instance after updating the training mode.
