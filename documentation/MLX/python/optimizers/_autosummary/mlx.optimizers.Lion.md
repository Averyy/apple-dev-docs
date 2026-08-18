---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/optimizers/_autosummary/mlx.optimizers.Lion.html
---

# mlx.optimizers.Lion

**

- [.rst](../../../_sources/python/optimizers/_autosummary/mlx.optimizers.Lion.rst)
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

# mlx.optimizers.Lion

 Table of contents 

## Contents

# mlx.optimizers.Lion

**class Lion(*learning_rate: float | Callable[[array], array]*, *betas: List[float] = [0.9, 0.99]*, *weight_decay: float = 0.0*)**
: The Lion optimizer [1].
Since updates are computed through the sign operation, they tend to
have larger norm than for other optimizers such as SGD and Adam.
We recommend a learning rate that is 3-10x smaller than AdamW and a
weight decay 3-10x larger than AdamW to maintain the strength
(lr * wd). Our Lion implementation follows the original paper. In
detail,
[1]: Chen, X. Symbolic Discovery of Optimization Algorithms. arXiv
preprint arXiv:2302.06675.

\[\begin{split}c_{t + 1} &= \beta_1 m_t + (1 - \beta_1) g_t \\
m_{t + 1} &= \beta_2 m_t + (1 - \beta_2) g_t \\
w_{t + 1} &= w_t - \eta (\text{sign}(c_t) + \lambda w_t)\end{split}\]

Parameters:

**learning_rate** ([float](https://docs.python.org/3/library/functions.html#float)* or **callable*) – The learning rate \(\eta\).
**betas** (*Tuple**[*[float](https://docs.python.org/3/library/functions.html#float)*, *[float](https://docs.python.org/3/library/functions.html#float)*]**, **optional*) – The coefficients
\((\beta_1, \beta_2)\) used for computing the gradient
momentum and update direction. Default: `(0.9, 0.99)`
**weight_decay** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The weight decay \(\lambda\). Default: `0.0`

Methods

`__init__`(learning_rate[, betas, weight_decay])

`apply_single`(gradient, parameter, state)
Performs the Lion parameter update and stores \(m\) in the optimizer state.

`init_single`(parameter, state)
Initialize optimizer state

** Contents
