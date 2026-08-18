---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.InstanceNorm.html
---

# mlx.nn.InstanceNorm

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.InstanceNorm.rst)
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

# mlx.nn.InstanceNorm

 Table of contents 

## Contents

# mlx.nn.InstanceNorm

**class InstanceNorm(*dims: int*, *eps: float = 1e-05*, *affine: bool = False*)**
: Applies instance normalization [1] on the inputs.
Computes

\[y = \frac{x - \mathrm{E}[x]}{ \sqrt{\mathrm{Var}[x] + \epsilon}} * \gamma + \beta,\]
where \(\gamma\) and \(\beta\) are learned per feature dimension
parameters initialized at 1 and 0 respectively. Both are of size `dims`,
if `affine` is `True`.

Parameters:

**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of features of the input.
**eps** ([float](https://docs.python.org/3/library/functions.html#float)) – A value added to the denominator for numerical stability. Default: `1e-5`.
**affine** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Default: `False`.

Shape:
Input: \((N, ..., C)\) where \(C\) is equal to `dims`.
The input must have at least 3 dimensions.
Output: Same shape as the input.

Examples
>>> import mlx.core as mx
>>> import mlx.nn as nn
>>> x = mx.random.normal((8, 4, 4, 16))
>>> inorm = nn.InstanceNorm(dims=16)
>>> output = inorm(x)

References
[1]: [https://arxiv.org/abs/1607.08022](https://arxiv.org/abs/1607.08022)
Methods

** Contents
