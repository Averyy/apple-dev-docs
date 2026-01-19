---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.recv.html
---

# mlx.core.distributed.recv

**

- [.rst](../../_sources/python/_autosummary/mlx.core.distributed.recv.rst)
- **

.pdf

**

# mlx.core.distributed.recv

 Table of contents 

## Contents

# mlx.core.distributed.recv

**recv(*shape: Sequence[int]*, *dtype: Dtype*, *src: int*, ***, *group: Group | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Recv an array with shape `shape` and dtype `dtype` from process
with rank `src`.

Parameters:

**shape** (*Tuple**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The shape of the array we are receiving.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)) – The data type of the array we are receiving.
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
