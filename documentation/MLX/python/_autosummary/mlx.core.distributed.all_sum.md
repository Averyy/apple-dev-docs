---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.all_sum.html
---

# mlx.core.distributed.all_sum

**

- [.rst](../../_sources/python/_autosummary/mlx.core.distributed.all_sum.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.distributed.all_sum

 Table of contents 

## Contents

# mlx.core.distributed.all_sum

**all_sum(*x: array*, ***, *group: Group | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: All reduce sum.
Sum the `x` arrays from all processes in the group.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**group** ([Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)) – The group of processes that will participate in the
reduction. If set to `None` the global group is used. Default:
`None`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The sum of all `x` arrays.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
