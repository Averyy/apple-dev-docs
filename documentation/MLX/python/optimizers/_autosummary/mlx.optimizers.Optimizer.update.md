---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Optimizer.update.html
---

# mlx.optimizers.Optimizer.update

**Optimizer.update(*model: Module*, *gradients: dict*)**
: Apply the gradients to the parameters of the model and update the
model with the new parameters.

Parameters:

**model** ([Module](../../nn/module.md#mlx.nn.Module)) – An mlx module to be updated.
**gradients** ([dict](https://docs.python.org/3/builtins/stdtypes.html#dict)) – A Python tree of gradients, most likely computed
via [mlx.nn.value_and_grad()](../../_autosummary/mlx.nn.value_and_grad.md#mlx.nn.value_and_grad).
