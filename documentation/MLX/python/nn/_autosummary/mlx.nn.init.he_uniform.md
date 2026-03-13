---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.he_uniform.html
---

# mlx.nn.init.he_uniform

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.he_uniform.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.init.he_uniform

 Table of contents 

## Contents

# mlx.nn.init.he_uniform

**he_uniform(*dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array), [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['fan_in', 'fan_out'], [float](https://docs.python.org/3/library/functions.html#float)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: A He uniform (Kaiming uniform) initializer.
This initializer samples from a uniform distribution with a range
computed from the number of input (`fan_in`) or output (`fan_out`)
units according to:

\[\sigma = \gamma \sqrt{\frac{3.0}{\text{fan}}}\]
where \(\text{fan}\) is either the number of input units when the
`mode` is `"fan_in"` or output units when the `mode` is
`"fan_out"`.
For more details see the original reference: [Delving Deep into Rectifiers:
Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/abs/1502.01852)

Parameters:
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the array. Default: `float32`.

Returns:
An initializer that returns an
array with the same shape as the input, filled with samples from  the
He uniform distribution.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array), [str](https://docs.python.org/3/library/stdtypes.html#str), [float](https://docs.python.org/3/library/functions.html#float)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

Example
>>> init_fn = nn.init.he_uniform()
>>> init_fn(mx.zeros((2, 2)))  # uses fan_in
array([[0.0300242, -0.0184009],
       [0.793615, 0.666329]], dtype=float32)
>>> init_fn(mx.zeros((2, 2)), mode="fan_out", gain=5)
array([[-1.64331, -2.16506],
       [1.08619, 5.79854]], dtype=float32)

** Contents
