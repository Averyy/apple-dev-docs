---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.triplet_loss.html
---

# mlx.nn.losses.triplet_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.triplet_loss.rst)
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

# mlx.nn.losses.triplet_loss

 Table of contents 

## Contents

# mlx.nn.losses.triplet_loss

**class triplet_loss(*anchors: array*, *positives: array*, *negatives: array*, *axis: int = -1*, *p: int = 2*, *margin: float = 1.0*, *eps: float = 1e-06*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Computes the triplet loss for a set of anchor, positive, and negative samples.
Margin is represented with alpha in the math section.

\[\max\left(\|A - P\|_p - \|A - N\|_p + \alpha, 0\right)\]

Parameters:

**anchors** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The anchor samples.
**positives** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The positive samples.
**negatives** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The negative samples.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The distribution axis. Default: `-1`.
**p** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The norm degree for pairwise distance. Default: `2`.
**margin** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Margin for the triplet loss. Defaults to `1.0`.
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Small positive constant added to the p-norm sum
before taking the `1 / p` power. Defaults to `1e-6`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:

Computed triplet loss. If reduction is `"none"`, returns a tensor with thesame shape as the inputs but with the `axis` dimension removed; if reduction
is `"mean"` or `"sum"`, returns a scalar tensor.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

** Contents
