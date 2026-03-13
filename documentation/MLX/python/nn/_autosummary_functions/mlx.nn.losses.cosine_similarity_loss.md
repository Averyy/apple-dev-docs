---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary_functions/mlx.nn.losses.cosine_similarity_loss.html
---

# mlx.nn.losses.cosine_similarity_loss

**

- [.rst](../../../_sources/python/nn/_autosummary_functions/mlx.nn.losses.cosine_similarity_loss.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.losses.cosine_similarity_loss

 Table of contents 

## Contents

# mlx.nn.losses.cosine_similarity_loss

**class cosine_similarity_loss(*x1: array*, *x2: array*, *axis: int = 1*, *eps: float = 1e-08*, *reduction: Literal['none', 'mean', 'sum'] = 'none'*)**
: Computes the cosine similarity between the two inputs.
The cosine similarity loss is given by

\[\frac{x_1 \cdot x_2}{\max(\|x_1\|  \cdot \|x_2\|, \epsilon)}\]

Parameters:

**x1** (*mx.array*) – The first set of inputs.
**x2** (*mx.array*) – The second set of inputs.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The embedding axis. Default: `1`.
**eps** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The minimum value of the denominator used for
numerical stability. Default: `1e-8`.
**reduction** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Specifies the reduction to apply to the output:
`'none'` | `'mean'` | `'sum'`. Default: `'none'`.

Returns:
The computed cosine similarity loss.

Return type:
mx.array

** Contents
