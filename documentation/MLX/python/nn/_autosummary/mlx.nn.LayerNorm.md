---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.LayerNorm.html
---

# mlx.nn.LayerNorm

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.LayerNorm.rst)
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

# mlx.nn.LayerNorm

 Table of contents 

## Contents

# mlx.nn.LayerNorm

**class LayerNorm(*dims: int*, *eps: float = 1e-05*, *affine: bool = True*, *bias: bool = True*)**
: Applies layer normalization [1] on the inputs.
Computes

\[y = \frac{x - E[x]}{\sqrt{Var[x] + \epsilon}} \gamma + \beta,\]
where \(\gamma\) and \(\beta\) are learned per feature dimension
parameters initialized at 1 and 0 respectively.
[1]: [https://arxiv.org/abs/1607.06450](https://arxiv.org/abs/1607.06450)

Parameters:

**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The feature dimension of the input to normalize over
**eps** ([float](https://docs.python.org/3/library/functions.html#float)) – A small additive constant for numerical stability.
Default: `1e-5`.
**affine** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True learn an affine transform to apply after the
normalization. Default: `True`.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True include a translation to the affine
transformation. If set to False the transformation is not really affine
just scaling. Default: `True`.

Methods

** Contents
