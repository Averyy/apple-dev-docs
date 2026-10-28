---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.FullyShardedModule.html
---

# mlx.nn.FullyShardedModule

```python
class FullyShardedModule(module: Module, group: Group | None = None, compute_dtype: Dtype | None = None)
```

Wrap a module so each member of the group holds only a shard of its
parameters.

The full parameters are gathered for the forward pass and the gradients
are reduce-scattered in the backward pass, so during training
each member of the group stores and updates only its own shard.

Every parameter is sharded along axis 0, so each parameter’s size along
that axis must be divisible by the size of `group`.

Use [fully_shard()](mlx.nn.layers.distributed.fully_shard.md#mlx.nn.layers.distributed.fully_shard) to wrap a module.

**Parameters:**

- **module** ([Module](../module.md#mlx.nn.Module)) – The module whose parameters will be sharded.
- **group** ([Group](../../_autosummary/mlx.core.distributed.Group.md#mlx.core.distributed.Group), *optional*) – The group to shard
across. If not set, the global group is used. Default: `None`.
- **compute_dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.md#mlx.core.Dtype), *optional*) – If set, the gathered
parameters are cast to this dtype for the forward pass.
Default: `None`.

Methods

| `as_linear`(*args, **kwargs) |  |
| --- | --- |
