---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.glorot_normal.html
---

# mlx.nn.init.glorot_normal

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.glorot_normal.rst)
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

# mlx.nn.init.glorot_normal

 Table of contents 

## Contents

# mlx.nn.init.glorot_normal

**glorot_normal(*dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array), [float](https://docs.python.org/3/library/functions.html#float)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: A Glorot normal initializer.
This initializer samples from a normal distribution with a standard
deviation computed from the number of input (`fan_in`) and output
(`fan_out`) units according to:

\[\sigma = \gamma \sqrt{\frac{2.0}{\text{fan\_in} + \text{fan\_out}}}\]
For more details see the original reference: [Understanding the difficulty
of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a.md)

Parameters:
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the array. Default: `float32`.

Returns:
An initializer that returns an array
with the same shape as the input, filled with samples from the Glorot
normal distribution.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array), [float](https://docs.python.org/3/library/functions.html#float)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

Example
>>> init_fn = nn.init.glorot_normal()
>>> init_fn(mx.zeros((2, 2)))
array([[0.191107, 1.61278],
       [-0.150594, -0.363207]], dtype=float32)
>>> init_fn(mx.zeros((2, 2)), gain=4.0)
array([[1.89613, -4.53947],
       [4.48095, 0.995016]], dtype=float32)

** Contents
