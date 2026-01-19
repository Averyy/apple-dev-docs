---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.nll_loss.html
---

# mlx.nn.losses.nll_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.nll_loss.rst)
- **

.pdf

**

# mlx.nn.losses.nll_loss

 Table of contents 

## Contents

# mlx.nn.losses.nll_loss

**class nll_loss(*inputs: array*, *targets: array*, *axis: int = -1*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Computes the negative log likelihood loss.

Parameters:

**inputs** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The predicted distribution in log space.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The target values.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The distribution axis. Default: `-1`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:
The computed NLL loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

** Contents
