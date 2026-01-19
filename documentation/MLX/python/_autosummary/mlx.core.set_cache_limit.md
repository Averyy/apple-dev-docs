---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.set_cache_limit.html
---

# mlx.core.set_cache_limit

**

- [.rst](../../_sources/python/_autosummary/mlx.core.set_cache_limit.rst)
- **

.pdf

**

# mlx.core.set_cache_limit

 Table of contents 

## Contents

# mlx.core.set_cache_limit

**set_cache_limit(*limit: int*) → [int](https://docs.python.org/3/library/functions.html#int)**
: Set the free cache limit.
If using more than the given limit, free memory will be reclaimed
from the cache on the next allocation. To disable the cache, set
the limit to `0`.
The cache limit defaults to the memory limit. See
[set_memory_limit()](mlx.core.set_memory_limit.html#mlx.core.set_memory_limit) for more details.

Parameters:
**limit** ([int](https://docs.python.org/3/library/functions.html#int)) – The cache limit in bytes.

Returns:
The previous cache limit in bytes.

Return type:
[int](https://docs.python.org/3/library/functions.html#int)

** Contents
