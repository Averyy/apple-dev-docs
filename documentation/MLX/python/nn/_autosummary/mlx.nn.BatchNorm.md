---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.BatchNorm.html
---

# mlx.nn.BatchNorm

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.BatchNorm.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.BatchNorm

 Table of contents 

## Contents

# mlx.nn.BatchNorm

**class BatchNorm(*num_features: int*, *eps: float = 1e-05*, *momentum: float = 0.1*, *affine: bool = True*, *track_running_stats: bool = True*)**
: Applies Batch Normalization over a 2D, 3D or 4D input.
Computes

\[y = \frac{x - E[x]}{\sqrt{Var[x] + \epsilon}} \gamma + \beta,\]
where \(\gamma\) and \(\beta\) are learned per feature dimension
parameters initialized at 1 and 0 respectively.
The input shape is specified as `NC` or `NLC`, where `N` is the
batch, `C` is the number of features or channels, and `L` is the
sequence length. The output has the same shape as the input. For
four-dimensional arrays, the shape is `NHWC`, where `H` and `W` are
the height and width respectively.
For more information on Batch Normalization, see the original paper [Batch
Normalization: Accelerating Deep Network Training by Reducing Internal
Covariate Shift](https://arxiv.org/abs/1502.03167).

Parameters:

**num_features** ([int](https://docs.python.org/3/library/functions.html#int)) – The feature dimension to normalize over.
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – A small additive constant for numerical
stability. Default: `1e-5`.
**momentum** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The momentum for updating the running
mean and variance. Default: `0.1`.
**affine** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, apply a learned affine
transformation after the normalization. Default: `True`.
**track_running_stats** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, track the
running mean and variance. Default: `True`.

Examples
>>> import mlx.core as mx
>>> import mlx.nn as nn
>>> x = mx.random.normal((5, 4))
>>> bn = nn.BatchNorm(num_features=4, affine=True)
>>> output = bn(x)

Methods

`unfreeze`(*args, **kwargs)
Wrap unfreeze to make sure that running_mean and var are always frozen parameters.

** Contents
