---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.GLU.html
---

# mlx.nn.GLU

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.GLU.rst)
- **

.pdf

**

# mlx.nn.GLU

 Table of contents 

## Contents

# mlx.nn.GLU

**class GLU(*axis: int = -1*)**
: Applies the gated linear unit function.
This function splits the `axis` dimension of the input into two halves
(\(a\) and \(b\)) and applies \(a * \sigma(b)\).

\[\textrm{GLU}(x) = a * \sigma(b)\]

Parameters:
**axis** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimension to split along. Default: `-1`

Methods

** Contents
