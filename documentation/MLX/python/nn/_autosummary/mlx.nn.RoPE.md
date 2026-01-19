---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.RoPE.html
---

# mlx.nn.RoPE

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.RoPE.rst)
- **

.pdf

**

# mlx.nn.RoPE

 Table of contents 

## Contents

# mlx.nn.RoPE

**class RoPE(*dims: int*, *traditional: bool = False*, *base: float = 10000*, *scale: float = 1.0*)**
: Implements the rotary positional encoding.
The traditional implementation rotates consecutive pairs of elements in the
feature dimension while the default implementation rotates pairs with
stride half the feature dimensions for efficiency.
For more details see [RoFormer: Enhanced Transformer with Rotary Position
Embedding](https://arxiv.org/abs/2104.09864).

Parameters:

**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The feature dimensions to be rotated. If the input feature
is larger than dims then the rest is left unchanged.
**traditional** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `True` choose the traditional
implementation which is slightly less efficient. Default: `False`.
**base** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The base used to compute angular frequency for
each dimension in the positional encodings. Default: `10000`.
**scale** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The scale used to scale the positions. Default: `1.0`.

Methods

** Contents
