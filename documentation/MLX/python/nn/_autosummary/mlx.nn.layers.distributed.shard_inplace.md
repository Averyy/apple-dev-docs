---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.layers.distributed.shard_inplace.html
---

# mlx.nn.layers.distributed.shard_inplace

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.layers.distributed.shard_inplace.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.layers.distributed.shard_inplace

 Table of contents 

## Contents

# mlx.nn.layers.distributed.shard_inplace

**shard_inplace(*module: Module*, *sharding: str | Callable*, ***, *segments: int | list = 1*, *group: Group | None = None*)**
: Shard a module in-place by updating its parameter dictionary with the
sharded parameter dictionary.
The `sharding` argument can be any callable that given the path and the
weight returns the sharding axis and optionally also the segments that
comprise the unsharded weight. For instance if the weight is a fused QKV
matrix the segments should be 3.

Note
The module doesn’t change so in order for distributed communication to
happen the module needs to natively support it and for it to be enabled.

Parameters:

**module** ([Module](../module.html#mlx.nn.Module)) – The parameters of this module will be sharded
in-place.
**sharding** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or **callable*) – One of “all-to-sharded” and
“sharded-to-all” or a callable that returns the sharding axis and
segments.
**segments** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)) – The segments to use if `sharding` is a
string. Default: `1`.
**group** ([Group](../../_autosummary/mlx.core.distributed.Group.html#mlx.core.distributed.Group)) – The distributed group to shard
across. If not set, the global group will be used. Default: `None`.

** Contents
