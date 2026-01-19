---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.AdaDelta.html
---

# mlx.optimizers.AdaDelta

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.AdaDelta.rst)
- **

.pdf

**

# mlx.optimizers.AdaDelta

 Table of contents 

## Contents

# mlx.optimizers.AdaDelta

**class AdaDelta(*learning_rate: float | Callable[[array], array]*, *rho: float = 0.9*, *eps: float = 1e-06*)**
: The AdaDelta optimizer with a learning rate [1].
Our AdaDelta implementation follows the original paper. In detail,
[1]: Zeiler, M.D., 2012. ADADELTA: an adaptive learning rate method. arXiv preprint arXiv:1212.5701.

\[\begin{split}v_{t+1} &= \rho v_t + (1 - \rho) g_t^2 \\
\Delta w_{t+1} &= \frac{\sqrt{u_t + \epsilon}}{\sqrt{v_{t+1} + \epsilon}} g_t \\
u_{t+1} &= \rho u_t + (1 - \rho) \Delta w_{t+1}^2 \\
w_{t+1} &= w_t - \lambda \Delta w_{t+1}\end{split}\]

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate \(\lambda\).
**rho** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The coefficient \(\rho\) used for computing a
running average of squared gradients. Default: `0.9`
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The term \(\epsilon\) added to the denominator to improve
numerical stability. Default: 1e-8

Methods

`__init__`(learning_rate[, rho, eps])

`apply_single`(gradient, parameter, state)
Performs the AdaDelta parameter update and stores \(v\) and \(u\) in the optimizer state.

`init_single`(parameter, state)
Initialize optimizer state

** Contents
