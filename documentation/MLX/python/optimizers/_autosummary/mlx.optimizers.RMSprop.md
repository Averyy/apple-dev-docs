---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.RMSprop.html
---

# mlx.optimizers.RMSprop

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.RMSprop.rst)
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

# mlx.optimizers.RMSprop

 Table of contents 

## Contents

# mlx.optimizers.RMSprop

**class RMSprop(*learning_rate: float | Callable[[array], array]*, *alpha: float = 0.99*, *eps: float = 1e-08*)**
: The RMSprop optimizer [1].
[1]: Tieleman, T. and Hinton, G. 2012. Lecture 6.5-rmsprop, coursera: Neural networks for machine learning

\[\begin{split}v_{t+1} &= \alpha v_t + (1 - \alpha) g_t^2 \\
w_{t+1} &= w_t - \lambda \frac{g_t}{\sqrt{v_{t+1}} + \epsilon}\end{split}\]

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate \(\lambda\).
**alpha** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The smoothing constant \(\alpha\).
Default: `0.99`
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The term \(\epsilon\) added to the denominator
to improve numerical stability. Default: `1e-8`

Methods

`__init__`(learning_rate[, alpha, eps])

`apply_single`(gradient, parameter, state)
Performs the RMSprop parameter update and stores \(v\) in the optimizer state.

`init_single`(parameter, state)
Initialize optimizer state

** Contents
