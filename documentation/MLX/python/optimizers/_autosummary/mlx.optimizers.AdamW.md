---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.AdamW.html
---

# mlx.optimizers.AdamW

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.AdamW.rst)
- **

.pdf

**

# mlx.optimizers.AdamW

 Table of contents 

## Contents

# mlx.optimizers.AdamW

**class AdamW(*learning_rate: float | Callable[[array], array]*, *betas: List[float] = [0.9, 0.999]*, *eps: float = 1e-08*, *weight_decay: float = 0.01*, *bias_correction: bool = False*)**
: The AdamW optimizer [1]. We update the weights with a weight_decay
(\(\lambda\)) value:
[1]: Loshchilov, I. and Hutter, F., 2019. Decoupled weight decay
regularization. ICLR 2019.

\[\begin{split}m_{t+1} &= \beta_1 m_t + (1 - \beta_1) g_t \\
v_{t+1} &= \beta_2 v_t + (1 - \beta_2) g_t^2 \\
w_{t+1} &= w_t - \alpha (\frac{m_{t+1}}{\sqrt{v_{t+1}} + \epsilon} + \lambda w_t)\end{split}\]

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate \(\alpha\).
**betas** (*Tuple**[*[float](https://docs.python.org/3/library/functions.html#float)*, *[float](https://docs.python.org/3/library/functions.html#float)*]**, **optional*) – The coefficients
\((\beta_1, \beta_2)\) used for computing running averages of the
gradient and its square. Default: `(0.9, 0.999)`
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The term \(\epsilon\) added to the
denominator to improve numerical stability. Default: `1e-8`
**weight_decay** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The weight decay \(\lambda\).
Default: `0.01`.
**bias_correction** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `True`, bias correction
is applied. Default: `False`

Methods

`__init__`(learning_rate[, betas, eps, ...])

`apply_single`(gradient, parameter, state)
Performs the AdamW parameter update by modifying the parameters passed into Adam.

** Contents
