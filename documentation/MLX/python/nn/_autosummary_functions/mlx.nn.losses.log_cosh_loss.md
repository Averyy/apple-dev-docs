---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.log_cosh_loss.html
---

# mlx.nn.losses.log_cosh_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.log_cosh_loss.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.losses.log_cosh_loss

 Table of contents 

## Contents

# mlx.nn.losses.log_cosh_loss

**class log_cosh_loss(*inputs: array*, *targets: array*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Computes the log cosh loss between inputs and targets.
Logcosh acts like L2 loss for small errors, ensuring stable gradients,
and like the L1 loss for large errors, reducing sensitivity to outliers. This
dual behavior offers a balanced, robust approach for regression tasks.

\[\text{logcosh}(y_{\text{true}}, y_{\text{pred}}) =
     \frac{1}{n} \sum_{i=1}^{n}
     \log(\cosh(y_{\text{pred}}^{(i)} - y_{\text{true}}^{(i)}))\]

Parameters:

**inputs** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The predicted values.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The target values.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:
The computed log cosh loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

** Contents
