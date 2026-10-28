---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/optimizer.html
---

# Optimizer

```python
class Optimizer(schedulers=None)
```

The base class for all optimizers. It allows us to implement an
optimizer on a per-parameter basis and apply it to a parameter tree.

Attributes

| [Optimizer.state](_autosummary/mlx.optimizers.Optimizer.state.md#mlx.optimizers.Optimizer.state) | The optimizer's state dictionary. |
| --- | --- |

Methods

| [Optimizer.apply_gradients](_autosummary/mlx.optimizers.Optimizer.apply_gradients.md#mlx.optimizers.Optimizer.apply_gradients)(gradients, parameters) | Apply the gradients to the parameters and return the updated parameters. |
| --- | --- |
| [Optimizer.init](_autosummary/mlx.optimizers.Optimizer.init.md#mlx.optimizers.Optimizer.init)(parameters) | Initialize the optimizer's state |
| [Optimizer.update](_autosummary/mlx.optimizers.Optimizer.update.md#mlx.optimizers.Optimizer.update)(model, gradients) | Apply the gradients to the parameters of the model and update the model with the new parameters. |
