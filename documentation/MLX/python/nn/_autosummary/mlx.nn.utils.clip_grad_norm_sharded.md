---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.utils.clip_grad_norm_sharded.html
---

# mlx.nn.utils.clip_grad_norm_sharded

```python
clip_grad_norm_sharded(gradients: Any, max_norm: float, group: Group | None = None)
```

Clip the global norm of gradients that are sharded across a group.

This is the sharded equivalent of
[mlx.optimizers.clip_grad_norm()](../../_autosummary/mlx.optimizers.clip_grad_norm.md#mlx.optimizers.clip_grad_norm). Each member of the group holds only
a shard of the gradients, so the global norm is computed by summing the
local squared norms across the group before rescaling. It is useful for
clipping the gradients of a module wrapped with
[mlx.nn.layers.distributed.fully_shard()](mlx.nn.layers.distributed.fully_shard.md#mlx.nn.layers.distributed.fully_shard).

**Parameters:**

- **gradients** (*Any*) – A Python tree containing the local shard of the
gradient arrays.
- **max_norm** ([float](https://docs.python.org/3/builtins/functions.html#float)) – The maximum allowed global norm of the gradients.
- **group** (*Optional*[[Group](../../_autosummary/mlx.core.distributed.Group.md#mlx.core.distributed.Group)]) – The group across which
the gradients are sharded. If set to `None` the global group is
used. Default: `None`.

**Returns:**
: The possibly rescaled local shard of the
gradients and the global gradient norm.

**Return type:**
: (*Any*, [array](../../_autosummary/mlx.core.array.md#mlx.core.array))
