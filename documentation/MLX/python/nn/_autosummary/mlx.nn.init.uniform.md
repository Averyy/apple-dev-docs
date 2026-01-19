---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.uniform.html
---

# mlx.nn.init.uniform

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.uniform.rst)
- **

.pdf

**

# mlx.nn.init.uniform

 Table of contents 

## Contents

# mlx.nn.init.uniform

**uniform(*low: float = 0.0*, *high: float = 1.0*, *dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: An initializer that returns samples from a uniform distribution.

Parameters:

**low** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The lower bound of the uniform distribution.
Default: `0.0`.
**high** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The upper bound of the uniform distribution.
Default: `1.0`
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the array. Default: `float32`.

Returns:
An initializer that returns an array
with the same shape as the input, filled with samples from a uniform
distribution

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

Example
>>> init_fn = nn.init.uniform(low=0, high=1)
>>> init_fn(mx.zeros((2, 2)))
array([[0.883935, 0.863726],
       [0.617261, 0.417497]], dtype=float32)

** Contents
