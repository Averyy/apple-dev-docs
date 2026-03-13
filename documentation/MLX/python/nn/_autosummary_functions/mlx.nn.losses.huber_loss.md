---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.huber_loss.html
---

# mlx.nn.losses.huber_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.huber_loss.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.losses.huber_loss

 Table of contents 

## Contents

# mlx.nn.losses.huber_loss

**class huber_loss(*inputs: array*, *targets: array*, *delta: float = 1.0*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Computes the Huber loss between inputs and targets.

\[\begin{split}l_{\delta}(a) =
\left\{ \begin{array}{ll}
    \frac{1}{2} a^2 & \text{for } |a| \leq \delta, \\
    \delta \left( |a| - \frac{1}{2} \delta \right) & \text{otherwise.}
\end{array} \right.\end{split}\]

Parameters:

**inputs** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The predicted values.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The target values.
**delta** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The threshold at which to change between L1 and L2 loss.
Default: `1.0`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:
The computed Huber loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

** Contents
