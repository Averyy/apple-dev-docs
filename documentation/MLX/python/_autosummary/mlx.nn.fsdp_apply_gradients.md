---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.nn.fsdp_apply_gradients.html
---

# mlx.nn.fsdp_apply_gradients

**

- [.rst](../../_sources/python/_autosummary/mlx.nn.fsdp_apply_gradients.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.fsdp_apply_gradients

 Table of contents 

## Contents

# mlx.nn.fsdp_apply_gradients

**fsdp_apply_gradients(*gradients*, *parameters*, *optimizer*, *fsdp_group=None*, *dp_group=None*, *communication_size=33554432*, *communication_stream=None*, *max_norm=None*)**
: Perform a distributed optimizer step by sharding gradients and optimizer states across ranks.
This helper function performs the following steps:
1. Reduce-scatter the gradients across ranks so each rank gets a shard of the averaged gradients.
2. Optionally clip the sharded gradients by global norm.
3. Apply the optimizer update on the local parameter slice using the sharded gradients.
4. All-gather the updated parameter slices from all ranks to reconstruct the full parameters tree.
This is similar to PyTorch’s FSDP with reshard_after_forward=False.

Parameters:

**gradients** (*Any*) – The Python tree containing the full gradients (it should
have the same structure as `parameters`). Each gradient’s first
dimension must be divisible by `fsdp_group.size()`.
**parameters** (*Any*) – The Python tree containing the full parameters (it should
have the same structure across processes). Each parameter’s first
dimension must be divisible by `fsdp_group.size()`.
**optimizer** – Optimizer with an `apply_gradients` method.
**fsdp_group** (*Optional**[*[Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)*]*) – The group of processes
for FSDP sharding. If `None`, the global group is used.
**dp_group** (*Optional**[*[Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)*]*) – The group of processes
for data-parallel gradient averaging. Required when `fsdp_group` is
smaller than the world (e.g. FSDP intra-node, DDP inter-node).
Default: `None`.
**communication_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Group arrays until their size in bytes exceeds
this number. Perform one communication step per group of arrays. If
less or equal to 0 array grouping is disabled. Default: `32MiB`.
**communication_stream** (*Optional**[*[Stream](stream_class.html#mlx.core.Stream)*]*) – The stream to use
for the communication. If unspecified the default communication
stream is used which can vary by back-end. Default: `None`.
**max_norm** (*Optional**[*[float](https://docs.python.org/3/library/functions.html#float)*]*) – If provided, clip gradients to this
maximum global norm before applying the optimizer update.
Default: `None`.

Returns:
If `max_norm` is `None`, returns the updated full-parameter tree.
Otherwise returns `(parameters, grad_norm)`, where `grad_norm` is
the global gradient norm before clipping.

Example
>>> optimizer = optim.SGD(learning_rate=0.01)
>>> # Without gradient clipping
>>> updated_params = fsdp_apply_gradients(grads, params, optimizer)
>>> model.update(updated_params)
>>>
>>> # With gradient clipping
>>> updated_params, grad_norm = fsdp_apply_gradients(
...     grads, params, optimizer, max_norm=1.0
... )
>>> model.update(updated_params)

** Contents
