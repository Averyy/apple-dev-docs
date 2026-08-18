---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Optimizer.apply_gradients.html
---

# mlx.optimizers.Optimizer.apply_gradients

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Optimizer.apply_gradients.rst)
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

# mlx.optimizers.Optimizer.apply_gradients

 Table of contents 

## Contents

# mlx.optimizers.Optimizer.apply_gradients

**Optimizer.apply_gradients(*gradients: dict*, *parameters: dict*)**
: Apply the gradients to the parameters and return the updated parameters.
Can be used to update a model via
`model.update(opt.apply_gradients(grads, model))` which is precisely
how [Optimizer.update()](mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update) is implemented.

Parameters:

**gradients** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – A Python tree of gradients.
**parameters** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – A Python tree of parameters. It can be a
superset of the gradients. In that case the returned python
tree will be of the same structure as the gradients.

** Contents
