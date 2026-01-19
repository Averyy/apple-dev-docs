---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.recv_like.html
---

# mlx.core.distributed.recv_like

**

- [.rst](../../_sources/python/_autosummary/mlx.core.distributed.recv_like.rst)
- **

.pdf

**

# mlx.core.distributed.recv_like

 Table of contents 

## Contents

# mlx.core.distributed.recv_like

**recv_like(*x: array*, *src: int*, ***, *group: Group | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Recv an array with shape and type like `x` from process with rank
`src`.
It is equivalent to calling `mx.distributed.recv(x.shape, x.dtype, src)`.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – An array defining the shape and dtype of the array we are
receiving.
**src** ([int](https://docs.python.org/3/library/functions.html#int)) – Rank of the source process in the group.
**group** ([Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)) – The group of processes that will participate in the
recv. If set to `None` the global group is used. Default:
`None`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The array that was received from `src`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
