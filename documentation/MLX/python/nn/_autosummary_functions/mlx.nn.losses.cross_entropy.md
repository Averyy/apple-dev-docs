---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.cross_entropy.html
---

# mlx.nn.losses.cross_entropy

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.cross_entropy.rst)
- **

.pdf

**

# mlx.nn.losses.cross_entropy

 Table of contents 

## Contents

# mlx.nn.losses.cross_entropy

**class cross_entropy(*logits: array*, *targets: array*, *weights: array | None = None*, *axis: int = -1*, *label_smoothing: float = 0.0*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Computes the cross entropy loss.

Parameters:

**logits** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The unnormalized logits.
**targets** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)) – The ground truth values. These can be class indices or
probabilities for each class. If the `targets` are class indices,
then `targets` shape should match the `logits` shape with
the `axis` dimension removed. If the `targets` are probabilities
(or one-hot encoded), then the `targets` shape should be the same as
the `logits` shape.
**weights** ([array](../../_autosummary/mlx.core.array.html#mlx.core.array)*, **optional*) – Optional weights for each target. Default: `None`.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The axis over which to compute softmax. Default: `-1`.
**label_smoothing** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Label smoothing factor. Default: `0`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:
The computed cross entropy loss.

Return type:
[array](../../_autosummary/mlx.core.array.html#mlx.core.array)

Examples
>>> import mlx.core as mx
>>> import mlx.nn as nn
>>>
>>> # Class indices as targets
>>> logits = mx.array([[2.0, -1.0], [-1.0, 2.0]])
>>> targets = mx.array([0, 1])
>>> nn.losses.cross_entropy(logits, targets)
array([0.0485873, 0.0485873], dtype=float32)
>>>
>>> # Probabilities (or one-hot vectors) as targets
>>> logits = mx.array([[2.0, -1.0], [-1.0, 2.0]])
>>> targets = mx.array([[0.9, 0.1], [0.1, 0.9]])
>>> nn.losses.cross_entropy(logits, targets)
array([0.348587, 0.348587], dtype=float32)

** Contents
