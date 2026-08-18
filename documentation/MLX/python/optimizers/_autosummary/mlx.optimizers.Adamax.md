---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Adamax.html
---

# mlx.optimizers.Adamax

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adamax.rst)
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

# mlx.optimizers.Adamax

 Table of contents 

## Contents

# mlx.optimizers.Adamax

**class Adamax(*learning_rate: float | Callable[[array], array]*, *betas: List[float] = [0.9, 0.999]*, *eps: float = 1e-08*)**
: The Adamax optimizer, a variant of Adam based on the infinity norm [1].
Our Adam implementation follows the original paper and omits the bias
correction in the first and second moment estimates. In detail,
[1]: Kingma, D.P. and Ba, J., 2015. Adam: A method for stochastic
optimization. ICLR 2015.

\[\begin{split}m_{t+1} &= \beta_1 m_t + (1 - \beta_1) g_t \\
v_{t+1} &= \max(\beta_2 v_t, |g_t|) \\
w_{t+1} &= w_t - \lambda \frac{m_{t+1}}{v_{t+1} + \epsilon}\end{split}\]

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate \(\lambda\).
**betas** (*Tuple**[*[float](https://docs.python.org/3/library/functions.html#float)*, *[float](https://docs.python.org/3/library/functions.html#float)*]**, **optional*) – The coefficients
\((\beta_1, \beta_2)\) used for computing the running average of
the gradient and the exponentially weighted infinity norm.
Default: `(0.9, 0.999)`
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The term \(\epsilon\) added to the
denominator to improve numerical stability. Default: `1e-8`

Methods

`__init__`(learning_rate[, betas, eps])

`apply_single`(gradient, parameter, state)
Performs the Adamax parameter update and stores \(v\) and \(m\) in the optimizer state.

`init_single`(parameter, state)
Initialize optimizer state

** Contents
