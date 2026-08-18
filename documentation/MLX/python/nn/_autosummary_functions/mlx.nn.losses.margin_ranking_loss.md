---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.margin_ranking_loss.html
---

# mlx.nn.losses.margin_ranking_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.margin_ranking_loss.rst)
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

# mlx.nn.losses.margin_ranking_loss

 Table of contents 

## Contents

# mlx.nn.losses.margin_ranking_loss

**class margin_ranking_loss(*inputs1: array*, *inputs2: array*, *targets: array*, *margin: float = 0.0*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Calculate the margin ranking loss that loss given inputs \(x_1\), \(x_2\) and a label
\(y\) (containing 1 or -1).
The loss is given by:

\[\text{loss} = \max (0, -y * (x_1 - x_2) + \text{margin})\]
Where \(y\) represents `targets`, \(x_1\) represents `inputs1` and \(x_2\)
represents `inputs2`.

Parameters:

**inputs1** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – Scores for the first input.
**inputs2** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – Scores for the second input.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – Labels indicating whether samples in `inputs1` should be ranked higher
than samples in `inputs2`. Values should be 1 or -1.
**margin** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The margin by which the scores should be separated.
Default: `0.0`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:
The computed margin ranking loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

Examples
>>> import mlx.core as mx
>>> import mlx.nn as nn
>>> targets = mx.array([1, 1, -1])
>>> inputs1 = mx.array([-0.573409, -0.765166, -0.0638])
>>> inputs2 = mx.array([0.75596, 0.225763, 0.256995])
>>> loss = nn.losses.margin_ranking_loss(inputs1, inputs2, targets)
>>> loss
array([1.32937, 0.990929, 0], dtype=float32)

** Contents
