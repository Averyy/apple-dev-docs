---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.AllToShardedLinear.html
---

# mlx.nn.AllToShardedLinear

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.AllToShardedLinear.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.AllToShardedLinear

 Table of contents 

## Contents

# mlx.nn.AllToShardedLinear

**class AllToShardedLinear(*input_dims: int*, *output_dims: int*, *bias: bool = True*, *group: Group | None = None*)**
: Each member of the group applies part of the affine transformation such
that the result is sharded across the group.
The gradients are automatically aggregated from each member of the group.

Parameters:

**input_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the input features
**output_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the output features
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `False` the layer will not use a
bias. Default is `True`.
**group** (*mx.distributed.Group**, **optional*) – The sharding will happen across
this group. If not set then the global group is used. Default is
`None`.

Methods

`from_linear`(linear_layer, *[, segments, group])

** Contents
