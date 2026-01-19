---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.smooth_l1_loss.html
---

# mlx.nn.losses.smooth_l1_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.smooth_l1_loss.rst)
- **

.pdf

**

# mlx.nn.losses.smooth_l1_loss

 Table of contents 

## Contents

# mlx.nn.losses.smooth_l1_loss

**class smooth_l1_loss(*predictions: array*, *targets: array*, *beta: float = 1.0*, *reduction: Literal['none', 'mean', 'sum'] = 'mean'*)**
: Computes the smooth L1 loss.
The smooth L1 loss is a variant of the L1 loss which replaces the absolute
difference with a squared difference when the absolute difference is less
than `beta`.
The formula for the smooth L1 Loss is:

\[\begin{split}l = \begin{cases}
      0.5 (x - y)^2 / \beta, & \text{if } |x - y| < \beta \\
      |x - y| - 0.5 \beta, & \text{otherwise}
    \end{cases}\end{split}\]

Parameters:

**predictions** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – Predicted values.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – Ground truth values.
**beta** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The threshold after which the loss changes
from the squared to the absolute difference. Default: `1.0`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'mean'`.

Returns:
The computed smooth L1 loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

** Contents
