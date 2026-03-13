---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.all_gather.html
---

# mlx.core.distributed.all_gather

**

- [.rst](../../_sources/python/_autosummary/mlx.core.distributed.all_gather.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.distributed.all_gather

 Table of contents 

## Contents

# mlx.core.distributed.all_gather

**all_gather(*x: array*, ***, *group: Group | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Gather arrays from all processes.
Gather the `x` arrays from all processes in the group and concatenate
them along the first axis. The arrays should all have the same shape.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**group** ([Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)) – The group of processes that will participate in the
gather. If set to `None` the global group is used. Default:
`None`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The concatenation of all `x` arrays.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
