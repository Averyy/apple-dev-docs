---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.ShardedToAllLinear.html
---

# mlx.nn.ShardedToAllLinear

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.ShardedToAllLinear.rst)
- **

.pdf

**

# mlx.nn.ShardedToAllLinear

 Table of contents 

## Contents

# mlx.nn.ShardedToAllLinear

**class ShardedToAllLinear(*input_dims: int*, *output_dims: int*, *bias: bool = True*, *group: Group | None = None*)**
: Each member of the group applies part of the affine transformation and
then aggregates the results.
All nodes will have the same exact result after this layer.
[ShardedToAllLinear](#mlx.nn.ShardedToAllLinear) provides a classmethod `from_linear()` to
convert linear layers to sharded [ShardedToAllLinear](#mlx.nn.ShardedToAllLinear) layers.

Parameters:

**input_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the input features
**output_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the output features
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `False` the the layer will not use a
bias. Default is `True`.
**group** (*mx.distributed.Group**, **optional*) – The sharding will happen across
this group. If not set then the global group is used. Default is
`None`.

Methods

`from_linear`(linear_layer, *[, segments, group])

** Contents
