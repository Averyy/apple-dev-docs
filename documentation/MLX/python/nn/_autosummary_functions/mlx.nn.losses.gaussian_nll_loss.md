---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.gaussian_nll_loss.html
---

# mlx.nn.losses.gaussian_nll_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.gaussian_nll_loss.rst)
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

# mlx.nn.losses.gaussian_nll_loss

 Table of contents 

## Contents

# mlx.nn.losses.gaussian_nll_loss

**class gaussian_nll_loss(*inputs: array*, *targets: array*, *vars: array*, *full: bool = False*, *eps: float = 1e-06*, *reduction: Literal['none', 'mean', 'sum'] = 'mean'*)**
: Computes the negative log likelihood loss for a Gaussian distribution.
The loss is given by:

\[\frac{1}{2}\left(\log\left(\max\left(\text{vars},
\ \epsilon\right)\right) + \frac{\left(\text{inputs} - \text{targets} \right)^2}
{\max\left(\text{vars}, \ \epsilon \right)}\right) + \text{const.}\]
where `inputs` are the predicted means and `vars` are the
predicted variances.

Parameters:

**inputs** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The predicted expectation of the Gaussian distribution.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The target values (samples from the Gaussian distribution).
**vars** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The predicted variance of the Gaussian distribution.
**full** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether to include the constant term in the loss calculation.
Default: `False`.
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Small positive constant for numerical stability.
Default: `1e-6`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'mean'`.

Returns:
The Gaussian NLL loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

** Contents
