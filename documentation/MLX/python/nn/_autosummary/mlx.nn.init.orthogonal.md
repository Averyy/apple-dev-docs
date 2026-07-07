---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.orthogonal.html
---

# mlx.nn.init.orthogonal

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.orthogonal.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.init.orthogonal

 Table of contents 

## Contents

# mlx.nn.init.orthogonal

**orthogonal(*gain: float = 1.0*, *dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: An initializer that returns an orthogonal matrix.

Parameters:

**gain** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Scaling factor for the orthogonal matrix.
Default: `1.0`.
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Data type of the array. Default: `float32`.

Returns:
An initializer that returns
an orthogonal matrix with the same shape as the input.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

** Contents
