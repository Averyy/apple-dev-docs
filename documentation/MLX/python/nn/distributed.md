---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/distributed.html
---

# Distributed

**

- [.rst](../../_sources/python/nn/distributed.rst)
- **

.pdf

**

# Distributed

 Table of contents 

## Contents

# Distributed

## Helper Routines

The `mlx.nn.layers.distributed` package contains helpful routines to
create sharded layers from existing [Modules](module.html#mlx.nn.Module).

| shard_linear(module, sharding, *[, ...]) | Create a new linear layer that has its parameters sharded and also performs distributed communication either in the forward or backward pass. |
| --- | --- |
| shard_inplace(module, sharding, *[, ...]) | Shard a module in-place by updating its parameter dictionary with the sharded parameter dictionary. |

## Layers

| AllToShardedLinear(input_dims, output_dims) | Each member of the group applies part of the affine transformation such that the result is sharded across the group. |
| --- | --- |
| ShardedToAllLinear(input_dims, output_dims) | Each member of the group applies part of the affine transformation and then aggregates the results. |
| QuantizedAllToShardedLinear(input_dims, ...) | Each member of the group applies part of the affine transformation with a quantized matrix such that the result is sharded across the group. |
| QuantizedShardedToAllLinear(input_dims, ...) | Each member of the group applies part of the affine transformation using the quantized matrix and then aggregates the results. |

** Contents
