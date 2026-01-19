---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Optimizer.init.html
---

# mlx.optimizers.Optimizer.init

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Optimizer.init.rst)
- **

.pdf

**

# mlx.optimizers.Optimizer.init

 Table of contents 

## Contents

# mlx.optimizers.Optimizer.init

**Optimizer.init(*parameters: dict*)**
: Initialize the optimizer’s state
This function can be used to initialize optimizers which have state
(like momentum in [SGD](mlx.optimizers.SGD.html#mlx.optimizers.SGD)). Using this method is optional as the
optimizer will initialize itself if the state is not yet set. However,
there are some cases where explicit initialization is useful in order
to have access to the [Optimizer.state](mlx.optimizers.Optimizer.state.html#mlx.optimizers.Optimizer.state) before the first call to
[Optimizer.update()](mlx.optimizers.Optimizer.update.html#mlx.optimizers.Optimizer.update).

Parameters:
**model** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – A Python tree of parameters.

Example
>>> optimizer = optim.SGD(learning_rate=1e-1, momentum=0.9)
>>> model = nn.Linear(2, 2)
>>> optimizer.init(model.trainable_parameters())
>>> optimizer.state.keys()
dict_keys(['step', 'learning_rate', 'weight', 'bias'])

** Contents
