---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.normal.html
---

# mlx.nn.init.normal

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.normal.rst)
- **

.pdf

**

# mlx.nn.init.normal

 Table of contents 

## Contents

# mlx.nn.init.normal

**normal(*mean: float = 0.0*, *std: float = 1.0*, *dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: An initializer that returns samples from a normal distribution.

Parameters:

**mean** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Mean of the normal distribution. Default:
`0.0`.
**std** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Standard deviation of the normal distribution.
Default: `1.0`.
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the array. Default:
`float32`.

Returns:
An initializer that returns an array with the
same shape as the input, filled with samples from a normal distribution.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

Example
>>> init_fn = nn.init.normal()
>>> init_fn(mx.zeros((2, 2)))
array([[-0.982273, -0.534422],
       [0.380709, 0.0645099]], dtype=float32)

** Contents
