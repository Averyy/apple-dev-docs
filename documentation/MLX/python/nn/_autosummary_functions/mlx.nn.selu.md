---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.selu.html
---

# mlx.nn.selu

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.selu.rst)
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

# mlx.nn.selu

 Table of contents 

## Contents

# mlx.nn.selu

**class selu(*x*)**
: Applies the Scaled Exponential Linear Unit.

\[\begin{split}\text{selu}(x) = \begin{cases}
\lambda x & \text{if } x > 0 \\
\lambda \alpha (\exp(x) - 1) & \text{if } x \leq 0
\end{cases}\end{split}\]
where \(\lambda = 1.0507\) and \(\alpha = 1.67326\).
See also [elu()](mlx.nn.elu.html#mlx.nn.elu).

** Contents
