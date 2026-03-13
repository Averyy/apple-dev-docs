---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.RMSNorm.html
---

# mlx.nn.RMSNorm

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.RMSNorm.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.RMSNorm

 Table of contents 

## Contents

# mlx.nn.RMSNorm

**class RMSNorm(*dims: int*, *eps: float = 1e-05*)**
: Applies Root Mean Square normalization [1] to the inputs.
Computes

\[y = \frac{x}{\sqrt{E[x^2] + \epsilon}} \gamma\]
where \(\gamma\) is a learned per feature dimension parameter initialized at
1.
Note the accumulation for the mean is done in 32-bit precision.
[1]: [https://arxiv.org/abs/1910.07467](https://arxiv.org/abs/1910.07467)

Parameters:

**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The feature dimension of the input to normalize over
**eps** ([float](https://docs.python.org/3/library/functions.html#float)) – A small additive constant for numerical stability

Methods

** Contents
