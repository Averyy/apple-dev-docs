---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/distributed.html
---

# Distributed Communication

MLX provides a distributed communication package using MPI. The MPI library is
loaded at runtime; if MPI is available then distributed communication is also
made available.

| [Group](_autosummary/mlx.core.distributed.Group.md#mlx.core.distributed.Group) | An [mlx.core.distributed.Group](_autosummary/mlx.core.distributed.Group.md#mlx.core.distributed.Group) represents a group of independent mlx processes that can communicate. |
| --- | --- |
| [is_available](_autosummary/mlx.core.distributed.is_available.md#mlx.core.distributed.is_available)([backend]) | Check if a communication backend is available. |
| [init](_autosummary/mlx.core.distributed.init.md#mlx.core.distributed.init)([strict, backend, all_gather_factory]) | Initialize the communication backend and create the global communication group. |
| [all_max](_autosummary/mlx.core.distributed.all_max.md#mlx.core.distributed.all_max)(x, *[, group, stream]) | All reduce max. |
| [all_min](_autosummary/mlx.core.distributed.all_min.md#mlx.core.distributed.all_min)(x, *[, group, stream]) | All reduce min. |
| [all_sum](_autosummary/mlx.core.distributed.all_sum.md#mlx.core.distributed.all_sum)(x, *[, group, stream]) | All reduce sum. |
| [all_gather](_autosummary/mlx.core.distributed.all_gather.md#mlx.core.distributed.all_gather)(x, *[, group, stream]) | Gather arrays from all processes. |
| [send](_autosummary/mlx.core.distributed.send.md#mlx.core.distributed.send)(x, dst, *[, group, stream]) | Send an array from the current process to the process that has rank `dst` in the group. |
| [recv](_autosummary/mlx.core.distributed.recv.md#mlx.core.distributed.recv)(shape, dtype, src, *[, group, stream]) | Recv an array with shape `shape` and dtype `dtype` from process with rank `src`. |
| [recv_like](_autosummary/mlx.core.distributed.recv_like.md#mlx.core.distributed.recv_like)(x, src, *[, group, stream]) | Recv an array with shape and type like `x` from process with rank `src`. |
| [sum_scatter](_autosummary/mlx.core.distributed.sum_scatter.md#mlx.core.distributed.sum_scatter)(x, *[, group, stream]) | Sum `x` across all processes in the group and shard the result along the first axis across ranks. |
