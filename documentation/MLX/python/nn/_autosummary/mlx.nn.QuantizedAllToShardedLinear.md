---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.QuantizedAllToShardedLinear.html
---

# mlx.nn.QuantizedAllToShardedLinear

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.QuantizedAllToShardedLinear.rst)
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

# mlx.nn.QuantizedAllToShardedLinear

 Table of contents 

## Contents

# mlx.nn.QuantizedAllToShardedLinear

**class QuantizedAllToShardedLinear(*input_dims: int*, *output_dims: int*, *bias: bool = True*, *group_size: int = 64*, *bits: int = 4*, *mode: str = 'affine'*, *group: Group | None = None*)**
: Each member of the group applies part of the affine transformation with
a quantized matrix such that the result is sharded across the group.
It is the quantized equivalent of [mlx.nn.AllToShardedLinear](mlx.nn.AllToShardedLinear.html#mlx.nn.AllToShardedLinear).
Similar to [mlx.nn.QuantizedLinear](mlx.nn.QuantizedLinear.html#mlx.nn.QuantizedLinear) its parameters are frozen and
will not be included in any gradient computation.

Parameters:

**input_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the input features.
**output_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the output features.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `False` then the layer will not use
a bias. Default: `True`.
**group_size** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The group size to use for the quantized
weight. See [quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize). Default: `64`.
**bits** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The bit width to use for the quantized weight.
See [quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize). Default: `4`.
**mode** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – The quantization method to use (see
[quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize)). Default: `"affine"`.
**group** (*mx.distributed.Group**, **optional*) – The sharding will happen across
this group. If not set then the global group is used. Default is
`None`.

Methods

`from_quantized_linear`(quantized_linear_layer, *)

`unfreeze`(*args, **kwargs)
Wrap unfreeze so that we unfreeze any layers we might contain but our parameters will remain frozen.

** Contents
