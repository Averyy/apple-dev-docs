---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.layers.distributed.fully_shard.html
---

# mlx.nn.layers.distributed.fully_shard

**fully_shard(*module: Module*, ***, *group: Group | None = None*, *compute_dtype: Dtype | None = None*) → [Module](../module.md#mlx.nn.Module)**
: Wrap `module` in a [FullyShardedModule](mlx.nn.FullyShardedModule.md#mlx.nn.FullyShardedModule).

Parameters:

**module** ([Module](../module.md#mlx.nn.Module)) – The module to wrap.
**group** ([Group](../../_autosummary/mlx.core.distributed.Group.md#mlx.core.distributed.Group)*, **optional*) – The group to shard
across. If not set, the global group is used. Default: `None`.
**compute_dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.md#mlx.core.Dtype)*, **optional*) – If set, the gathered
parameters are cast to this dtype for the forward pass.
Default: `None`.

Returns:
The wrapped [FullyShardedModule](mlx.nn.FullyShardedModule.md#mlx.nn.FullyShardedModule), or `module` unchanged.
