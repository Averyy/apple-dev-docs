---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.binary_cross_entropy.html
---

# mlx.nn.losses.binary_cross_entropy

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.binary_cross_entropy.rst)
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

# mlx.nn.losses.binary_cross_entropy

 Table of contents 

## Contents

# mlx.nn.losses.binary_cross_entropy

**class binary_cross_entropy(*inputs: array*, *targets: array*, *weights: array | None = None*, *with_logits: bool = True*, *reduction: Literal['none', 'mean', 'sum'] = 'mean'*)**
: Computes the binary cross entropy loss.
By default, this function takes the pre-sigmoid logits, which results in a faster
and more precise loss. For improved numerical stability when `with_logits=False`,
the loss calculation clips the input probabilities (in log-space) to a minimum value
of `-100`.

Parameters:

**inputs** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The predicted values. If `with_logits` is `True`, then
`inputs` are unnormalized logits. Otherwise, `inputs` are probabilities.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The binary target values in {0, 1}.
**weights** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)*, **optional*) – Optional weights for each target. Default: `None`.
**with_logits** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether `inputs` are logits. Default: `True`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'mean'`.

Returns:
The computed binary cross entropy loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

Examples
>>> import mlx.core as mx
>>> import mlx.nn as nn

>>> logits = mx.array([0.105361, 0.223144, 1.20397, 0.916291])
>>> targets = mx.array([0, 0, 1, 1])
>>> loss = nn.losses.binary_cross_entropy(logits, targets, reduction="mean")
>>> loss
array(0.539245, dtype=float32)

>>> probs = mx.array([0.1, 0.1, 0.4, 0.4])
>>> targets = mx.array([0, 0, 1, 1])
>>> loss = nn.losses.binary_cross_entropy(probs, targets, with_logits=False, reduction="mean")
>>> loss
array(0.510826, dtype=float32)

** Contents
