---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.hinge_loss.html
---

# mlx.nn.losses.hinge_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.hinge_loss.rst)
- **

.pdf

**

# mlx.nn.losses.hinge_loss

 Table of contents 

## Contents

# mlx.nn.losses.hinge_loss

**class hinge_loss(*inputs: array*, *targets: array*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Computes the hinge loss between inputs and targets.

\[\text{hinge}(y, y_{\text{pred}}) = \max(0, 1 - y \cdot y_{\text{pred}})\]

Parameters:

**inputs** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The predicted values.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The target values. They should be -1 or 1.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:
The computed hinge loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

** Contents
