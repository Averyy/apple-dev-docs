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

# mlx.core.distributed.init

 Table of contents 

## Contents

# mlx.core.distributed.init

**init(*strict: bool = False*, *backend: str = 'any'*) → [Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)**
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

Returns:
The group representing all the launched processes.

Return type:
[Group](mlx.core.distributed.Group.html#mlx.core.distributed.Group)

** Contents
