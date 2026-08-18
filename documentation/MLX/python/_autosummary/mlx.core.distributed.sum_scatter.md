---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.sum_scatter.html
---

# mlx.core.distributed.sum_scatter

**

- [.rst](../../_sources/python/_autosummary/mlx.core.distributed.sum_scatter.rst)
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

# mlx.core.distributed.sum_scatter

 Table of contents 

## Contents

# mlx.core.distributed.sum_scatter

**sum_scatter(*x: array*, ***, *group: Group | None = None*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Sum `x` across all processes in the group and shard the result along the first axis across ranks.
`x.shape[0]` must be divisible by the group size.
The result is equivalent to `all_sum(x)[rank*chunk_size:(rank+1)*chunk_size]`, where `chunk_size = x.shape[0] // group.size()` and `rank` is the rank of this process in the group.
Note: `all_sum` is mentioned only for illustration; the actual implementation does not perform `all_sum` and uses a single reduce-scatter collective instead.
Currently supported only for the NCCL backend.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**group** ([Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)) – The group of processes that will participate in the
sum scatter. If set to `None` the global group is used. Default:
`None`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The output array with shape `[x.shape[0] // group.size(), *x.shape[1:]]`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
