---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.SGD.html
---

# mlx.optimizers.SGD

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.SGD.rst)
- **

.pdf

**

**
**
**

**

# mlx.optimizers.SGD

 Table of contents 

## Contents

# mlx.optimizers.SGD

**class SGD(*learning_rate: float | Callable[[array], array]*, *momentum: float = 0.0*, *weight_decay: float = 0.0*, *dampening: float = 0.0*, *nesterov: bool = False*)**
: The stochastic gradient descent optimizer.
Updates a parameter \(w\) with a gradient \(g\) as follows

\[\begin{split}v_{t+1} &= \mu v_t + (1 - \tau) g_t \\
w_{t+1} &= w_t - \lambda v_{t+1}\end{split}\]

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate \(\lambda\).
**momentum** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The momentum strength \(\mu\). Default: `0`
**weight_decay** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The weight decay (L2 penalty). Default: `0`
**dampening** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Dampening for momentum \(\tau\). Default: `0`
**nesterov** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Enables Nesterov momentum. Default: `False`

Methods

`__init__`(learning_rate[, momentum, ...])

`apply_single`(gradient, parameter, state)
Performs the SGD parameter update and stores \(v\) in the optimizer state.

`init_single`(parameter, state)
Initialize optimizer state

** Contents
