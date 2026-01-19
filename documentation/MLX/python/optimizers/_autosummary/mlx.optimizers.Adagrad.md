---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Adagrad.html
---

# mlx.optimizers.Adagrad

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adagrad.rst)
- **

.pdf

**

# mlx.optimizers.Adagrad

 Table of contents 

## Contents

# mlx.optimizers.Adagrad

**class Adagrad(*learning_rate: float | Callable[[array], array]*, *eps: float = 1e-08*)**
: The Adagrad optimizer [1].
Our Adagrad implementation follows the original paper. In detail,
[1]: Duchi, J., Hazan, E. and Singer, Y., 2011. Adaptive subgradient methods
for online learning and stochastic optimization. JMLR 2011.

\[\begin{split}v_{t+1} &= v_t + g_t^2 \\
w_{t+1} &= w_t - \lambda \frac{g_t}{\sqrt{v_{t+1}} + \epsilon}\end{split}\]

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate \(\lambda\).
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The term \(\epsilon\) added to the
denominator to improve numerical stability. Default: `1e-8`

Methods

`__init__`(learning_rate[, eps])

`apply_single`(gradient, parameter, state)
Performs the Adagrad parameter update and stores \(v\) in the optimizer state.

`init_single`(parameter, state)
Initialize optimizer state

** Contents
