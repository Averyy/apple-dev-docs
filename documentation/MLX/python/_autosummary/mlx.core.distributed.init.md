---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.init.html
---

# mlx.core.distributed.init

**

- [.rst](../../_sources/python/_autosummary/mlx.core.distributed.init.rst)
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

# mlx.core.distributed.init

 Table of contents 

## Contents

# mlx.core.distributed.init

**init(*strict: bool = False*, *backend: str = 'any'*, ***, *all_gather_factory: Callable[[int, int], Callable[[bytes, int], bytes]] | None = None*) → [Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)**
: Initialize the communication backend and create the global communication group.
Example
import mlx.core as mx

group = mx.distributed.init(backend="ring")

Parameters:

**strict** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to False it returns a singleton group
in case `mx.distributed.is_available()` returns False otherwise
it throws a runtime error. Default: `False`
**backend** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Which distributed backend to initialize.
Possible values `mpi`, `ring`, `nccl`, `jaccl`, `any`. If
set to `any` all available backends are tried and the first one
that succeeds becomes the global group which will be returned in
subsequent calls. Default: `any`
**all_gather_factory** (*Callable**, **optional*) – A factory used only with the
`jaccl` backend. It is called once per rank with `(rank, size)`
and must return a callable with signature
`f(src: bytes, n_bytes: int) -> bytes`. The returned callable
performs a byte-level all-gather used as the JACCL side channel
when exchanging RDMA connection metadata. The returned bytes must
have length `size * n_bytes`.

Returns:
The group representing all the launched processes.

Return type:
[Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)

** Contents
