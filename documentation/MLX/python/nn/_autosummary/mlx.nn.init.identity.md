---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.identity.html
---

# mlx.nn.init.identity

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.identity.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.init.identity

 Table of contents 

## Contents

# mlx.nn.init.identity

**identity(*dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: An initializer that returns an identity matrix.

Parameters:
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the array. Default:
`float32`.

Returns:
An initializer that returns an identity
matrix with the same shape as the input.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

Example
>>> init_fn = nn.init.identity()
>>> init_fn(mx.zeros((2, 2)))
array([[1, 0],
       [0, 1]], dtype=float32)

** Contents
