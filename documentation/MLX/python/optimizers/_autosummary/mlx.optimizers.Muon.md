---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Muon.html
---

# mlx.optimizers.Muon

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Muon.rst)
- **

.pdf

**

# mlx.optimizers.Muon

 Table of contents 

## Contents

# mlx.optimizers.Muon

**class Muon(*learning_rate: float | Callable[[array], array]*, *momentum: float = 0.95*, *weight_decay: float = 0.01*, *nesterov: bool = True*, *ns_steps: int = 5*)**
: The Muon optimizer.
Our Muon (MomentUm Orthogonalized by Newton-schulz) optimizer follows the
original implementation: [Muon: An optimizer for hidden layers in neural
networks](https://kellerjordan.github.io/posts/muon/)

Note

Muon may be sub-optimal for the embedding layer, the final fully
connected layer, or any 0D/1D parameters. Those should be optimized
by a different method (e.g., [AdamW](mlx.optimizers.AdamW.html#mlx.optimizers.AdamW)).
For 4D convolutional filters, it works by flattening their last
dimensions.

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate.
**momentum** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The momentum strength. Default: `0.95`
**weight_decay** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The weight decay (L2 penalty).
Default: `0.01`
**nesterov** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Enables Nesterov momentum. Recommended for
better performance.  Default: `True`
**ns_steps** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Number of Newton-Schulz iteration steps for
orthogonalization.  Default: `5`

Methods

`__init__`(learning_rate[, momentum, ...])

`apply_single`(gradient, parameter, state)
Performs the Muon parameter update

`init_single`(parameter, state)
Initialize optimizer state

** Contents
