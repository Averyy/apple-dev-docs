---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.layers.distributed.shard_linear.html
---

# mlx.nn.layers.distributed.shard_linear

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.layers.distributed.shard_linear.rst)
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

# mlx.nn.layers.distributed.shard_linear

 Table of contents 

## Contents

# mlx.nn.layers.distributed.shard_linear

**shard_linear(*module: Module*, *sharding: str*, ***, *segments: int | list = 1*, *group: Group | None = None*)**
: Create a new linear layer that has its parameters sharded and also
performs distributed communication either in the forward or backward
pass.

Note
Contrary to `shard_inplace`, the original layer is not changed but a
new layer is returned.

Parameters:

**module** ([Module](../module.html#mlx.nn.Module)) – The linear layer to be sharded.
**sharding** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – One of “all-to-sharded” and
“sharded-to-all” that defines the type of sharding to perform.
**segments** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)) – The segments to use. Default: `1`.
**group** ([Group](../../_autosummary/mlx.core.distributed.Group.html#mlx.core.distributed.Group)) – The distributed group to shard
across. If not set, the global group will be used. Default: `None`.

** Contents
