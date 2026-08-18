---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Adam.html
---

# mlx.optimizers.Adam

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Adam.rst)
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

# mlx.optimizers.Adam

 Table of contents 

## Contents

# mlx.optimizers.Adam

**class Adam(*learning_rate: float | Callable[[array], array]*, *betas: List[float] = [0.9, 0.999]*, *eps: float = 1e-08*, *bias_correction: bool = False*)**
: The Adam optimizer [1]. In detail,
[1]: Kingma, D.P. and Ba, J., 2015. Adam: A method for stochastic
optimization. ICLR 2015.

\[\begin{split}m_{t+1} &= \beta_1 m_t + (1 - \beta_1) g_t \\
v_{t+1} &= \beta_2 v_t + (1 - \beta_2) g_t^2 \\
w_{t+1} &= w_t - \lambda \frac{m_{t+1}}{\sqrt{v_{t+1}} + \epsilon}\end{split}\]

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate \(\lambda\).
**betas** (*Tuple**[*[float](https://docs.python.org/3/library/functions.html#float)*, *[float](https://docs.python.org/3/library/functions.html#float)*]**, **optional*) – The coefficients
\((\beta_1, \beta_2)\) used for computing running averages of the
gradient and its square. Default: `(0.9, 0.999)`
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The term \(\epsilon\) added to the
denominator to improve numerical stability. Default: `1e-8`
**bias_correction** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `True`, bias correction
is applied. Default: `False`

Methods

`__init__`(learning_rate[, betas, eps, ...])

`apply_single`(gradient, parameter, state)
Performs the Adam parameter update and stores \(v\) and \(m\) in the optimizer state.

`init_single`(parameter, state)
Initialize optimizer state

** Contents
