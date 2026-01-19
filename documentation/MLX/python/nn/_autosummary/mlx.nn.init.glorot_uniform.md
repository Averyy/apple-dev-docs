---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.glorot_uniform.html
---

# mlx.nn.init.glorot_uniform

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.glorot_uniform.rst)
- **

.pdf

**

# mlx.nn.init.glorot_uniform

 Table of contents 

## Contents

# mlx.nn.init.glorot_uniform

**glorot_uniform(*dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array), [float](https://docs.python.org/3/library/functions.html#float)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: A Glorot uniform initializer.
This initializer samples from a uniform distribution with a range
computed from the number of input (`fan_in`) and output (`fan_out`)
units according to:

\[\sigma = \gamma \sqrt{\frac{6.0}{\text{fan\_in} + \text{fan\_out}}}\]
For more details see the original reference: [Understanding the difficulty
of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a.md)

Parameters:
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the array. Default: `float32`.

Returns:
An initializer that returns an array
with the same shape as the input, filled with samples from the Glorot
uniform distribution.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array), [float](https://docs.python.org/3/library/functions.html#float)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

Example
>>> init_fn = nn.init.glorot_uniform()
>>> init_fn(mx.zeros((2, 2)))
array([[0.223404, -0.890597],
       [-0.379159, -0.776856]], dtype=float32)
>>> init_fn(mx.zeros((2, 2)), gain=4.0)
array([[-1.90041, 3.02264],
       [-0.912766, 4.12451]], dtype=float32)

** Contents
