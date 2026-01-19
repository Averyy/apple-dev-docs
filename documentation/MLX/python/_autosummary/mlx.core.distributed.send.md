---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.send.html
---

# mlx.core.distributed.send

**

- [.rst](../../_sources/python/_autosummary/mlx.core.distributed.send.rst)
- **

.pdf

**

# mlx.core.distributed.send

 Table of contents 

## Contents

# mlx.core.distributed.send

**send(*x: array*, *dst: int*, ***, *group: Group | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Send an array from the current process to the process that has rank
`dst` in the group.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**dst** ([int](https://docs.python.org/3/library/functions.html#int)) – Rank of the destination process in the group.
**group** ([Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)) – The group of processes that will participate in the
send. If set to `None` the global group is used. Default:
`None`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
An array identical to `x` which when evaluated the send is performed.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
