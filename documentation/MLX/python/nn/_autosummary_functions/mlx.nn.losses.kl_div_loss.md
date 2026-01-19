---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.kl_div_loss.html
---

# mlx.nn.losses.kl_div_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.kl_div_loss.rst)
- **

.pdf

**

# mlx.nn.losses.kl_div_loss

 Table of contents 

## Contents

# mlx.nn.losses.kl_div_loss

**class kl_div_loss(*inputs: array*, *targets: array*, *axis: int = -1*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Computes the Kullback-Leibler divergence loss.
Computes the following when `reduction == 'none'`:
mx.exp(targets) * (targets - inputs).sum(axis)

Parameters:

**inputs** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – Log probabilities for the predicted distribution.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – Log probabilities for the target distribution.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The distribution axis. Default: `-1`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:
The computed Kullback-Leibler divergence loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

** Contents
