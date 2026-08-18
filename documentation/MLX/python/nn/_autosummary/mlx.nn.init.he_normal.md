---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.he_normal.html
---

# mlx.nn.init.he_normal

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.he_normal.rst)
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

# mlx.nn.init.he_normal

 Table of contents 

## Contents

# mlx.nn.init.he_normal

**he_normal(*dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array), [Literal](https://docs.python.org/3/library/typing.html#typing.Literal)['fan_in', 'fan_out'], [float](https://docs.python.org/3/library/functions.html#float)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: Build a He normal initializer.
This initializer samples from a normal distribution with a standard
deviation computed from the number of input (`fan_in`) or output
(`fan_out`) units according to:

\[\sigma = \gamma \frac{1}{\sqrt{\text{fan}}}\]
where \(\text{fan}\) is either the number of input units when the
`mode` is `"fan_in"` or output units when the `mode` is
`"fan_out"`.
For more details see the original reference: [Delving Deep into Rectifiers:
Surpassing Human-Level Performance on ImageNet Classification](https://arxiv.org/abs/1502.01852)

Parameters:
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the array. Default: `float32`.

Returns:
An initializer that returns an
array with the same shape as the input, filled with samples from the He
normal distribution.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array), [str](https://docs.python.org/3/library/stdtypes.html#str), [float](https://docs.python.org/3/library/functions.html#float)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

Example
>>> init_fn = nn.init.he_normal()
>>> init_fn(mx.zeros((2, 2)))  # uses fan_in
array([[-1.25211, 0.458835],
       [-0.177208, -0.0137595]], dtype=float32)
>>> init_fn(mx.zeros((2, 2)), mode="fan_out", gain=5)
array([[5.6967, 4.02765],
       [-4.15268, -2.75787]], dtype=float32)

** Contents
