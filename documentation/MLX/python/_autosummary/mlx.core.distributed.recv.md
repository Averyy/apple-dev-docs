---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.recv.html
---

# mlx.core.distributed.recv

**recv(*shape: Sequence[int]*, *dtype: Dtype*, *src: int*, ***, *group: Group | None = None*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.md#mlx.core.array)**
: Recv an array with shape `shape` and dtype `dtype` from process
with rank `src`.

Parameters:

**shape** (*Tuple**[*[int](https://docs.python.org/3/builtins/functions.html#int)*]*) – The shape of the array we are receiving.
**dtype** ([Dtype](mlx.core.Dtype.md#mlx.core.Dtype)) – The data type of the array we are receiving.
**src** ([int](https://docs.python.org/3/builtins/functions.html#int)) – Rank of the source process in the group.
**group** ([Group](mlx.core.distributed.Group.md#mlx.core.distributed.Group)) – The group of processes that will participate in the
recv. If set to `None` the global group is used. Default:
`None`.
**stream** ([Stream](stream_class.md#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The array that was received from `src`.

Return type:
[array](mlx.core.array.md#mlx.core.array)
