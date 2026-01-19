---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.set_memory_limit.html
---

# mlx.core.set_memory_limit

**

- [.rst](../../_sources/python/_autosummary/mlx.core.set_memory_limit.rst)
- **

.pdf

**

# mlx.core.set_memory_limit

 Table of contents 

## Contents

# mlx.core.set_memory_limit

**set_memory_limit(*limit: int*) → [int](https://docs.python.org/3/library/functions.html#int)**
: Set the memory limit.
The memory limit is a guideline for the maximum amount of memory to use
during graph evaluation. If the memory limit is exceeded and there is no
more RAM (including swap when available) allocations will result in an
exception.
When metal is available the memory limit defaults to 1.5 times the
maximum recommended working set size reported by the device.

Parameters:
**limit** ([int](https://docs.python.org/3/library/functions.html#int)) – Memory limit in bytes.

Returns:
The previous memory limit in bytes.

Return type:
[int](https://docs.python.org/3/library/functions.html#int)

** Contents
