---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GroupNorm.html
---

# mlx.nn.GroupNorm

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.GroupNorm.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.GroupNorm

 Table of contents 

## Contents

# mlx.nn.GroupNorm

**class GroupNorm(*num_groups: int*, *dims: int*, *eps: float = 1e-05*, *affine: bool = True*, *pytorch_compatible: bool = False*)**
: Applies Group Normalization [1] to the inputs.
Computes the same normalization as layer norm, namely

\[y = \frac{x - E[x]}{\sqrt{Var[x] + \epsilon}} \gamma + \beta,\]
where \(\gamma\) and \(\beta\) are learned per feature dimension
parameters initialized at 1 and 0 respectively. However, the mean and
variance are computed over the spatial dimensions and each group of
features. In particular, the input is split into num_groups across the
feature dimension.
The feature dimension is assumed to be the last dimension and the dimensions
that precede it (except the first) are considered the spatial dimensions.
[1]: [https://arxiv.org/abs/1803.08494](https://arxiv.org/abs/1803.08494)

Parameters:

**num_groups** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of groups to separate the features into
**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The feature dimensions of the input to normalize over
**eps** ([float](https://docs.python.org/3/library/functions.html#float)) – A small additive constant for numerical stability
**affine** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True learn an affine transform to apply after the
normalization.
**pytorch_compatible** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True perform the group normalization in
the same order/grouping as PyTorch.

Methods

** Contents
