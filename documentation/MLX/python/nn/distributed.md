---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/distributed.html
---

# Distributed

## Helper Routines

The `mlx.nn.layers.distributed` package contains helpful routines to
create sharded layers from existing [Modules](module.md#mlx.nn.Module).

| [shard_linear](_autosummary/mlx.nn.layers.distributed.shard_linear.md#mlx.nn.layers.distributed.shard_linear)(module, sharding, *[, ...]) | Create a new linear layer that has its parameters sharded and also performs distributed communication either in the forward or backward pass. |
| --- | --- |
| [shard_inplace](_autosummary/mlx.nn.layers.distributed.shard_inplace.md#mlx.nn.layers.distributed.shard_inplace)(module, sharding, *[, ...]) | Shard a module in-place by updating its parameter dictionary with the sharded parameter dictionary. |
| [fully_shard](_autosummary/mlx.nn.layers.distributed.fully_shard.md#mlx.nn.layers.distributed.fully_shard)(module, *[, group, compute_dtype]) | Wrap `module` in a [FullyShardedModule](_autosummary/mlx.nn.FullyShardedModule.md#mlx.nn.FullyShardedModule). |

## Layers

| [AllToShardedLinear](_autosummary/mlx.nn.AllToShardedLinear.md#mlx.nn.AllToShardedLinear)(input_dims, output_dims) | Each member of the group applies part of the affine transformation such that the result is sharded across the group. |
| --- | --- |
| [ShardedToAllLinear](_autosummary/mlx.nn.ShardedToAllLinear.md#mlx.nn.ShardedToAllLinear)(input_dims, output_dims) | Each member of the group applies part of the affine transformation and then aggregates the results. |
| [QuantizedAllToShardedLinear](_autosummary/mlx.nn.QuantizedAllToShardedLinear.md#mlx.nn.QuantizedAllToShardedLinear)(input_dims, ...) | Each member of the group applies part of the affine transformation with a quantized matrix such that the result is sharded across the group. |
| [QuantizedShardedToAllLinear](_autosummary/mlx.nn.QuantizedShardedToAllLinear.md#mlx.nn.QuantizedShardedToAllLinear)(input_dims, ...) | Each member of the group applies part of the affine transformation using the quantized matrix and then aggregates the results. |
| [FullyShardedModule](_autosummary/mlx.nn.FullyShardedModule.md#mlx.nn.FullyShardedModule)(module[, group, ...]) | Wrap a module so each member of the group holds only a shard of its parameters. |
