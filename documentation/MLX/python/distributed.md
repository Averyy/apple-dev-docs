---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/distributed.html
---

# Distributed Communication

**

- [.rst](../_sources/python/distributed.rst)
- **

.pdf

**

**
**
**

**

# Distributed Communication

 Table of contents 

# Distributed Communication

MLX provides a distributed communication package using MPI. The MPI library is
loaded at runtime; if MPI is available then distributed communication is also
made available.

| Group | Anmlx.core.distributed.Grouprepresents a group of independent mlx processes that can communicate. |
| --- | --- |
| is_available([backend]) | Check if a communication backend is available. |
| init([strict, backend]) | Initialize the communication backend and create the global communication group. |
| all_sum(x, *[, group, stream]) | All reduce sum. |
| all_gather(x, *[, group, stream]) | Gather arrays from all processes. |
| send(x, dst, *[, group, stream]) | Send an array from the current process to the process that has rankdstin the group. |
| recv(shape, dtype, src, *[, group, stream]) | Recv an array with shapeshapeand dtypedtypefrom process with ranksrc. |
| recv_like(x, src, *[, group, stream]) | Recv an array with shape and type likexfrom process with ranksrc. |
