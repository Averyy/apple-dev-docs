---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.set_wired_limit.html
---

# mlx.core.set_wired_limit

**

- [.rst](../../_sources/python/_autosummary/mlx.core.set_wired_limit.rst)
- **

.pdf

**

# mlx.core.set_wired_limit

 Table of contents 

## Contents

# mlx.core.set_wired_limit

**set_wired_limit(*limit: int*) → [int](https://docs.python.org/3/library/functions.html#int)**
: Set the wired size limit.

Note

This function is only useful on macOS 15.0 or higher.
The wired limit should remain strictly less than the total
memory size.

The wired limit is the total size in bytes of memory that will be kept
resident. The default value is `0`.
Setting a wired limit larger than system wired limit is an error. You can
increase the system wired limit with:
sudo sysctl iogpu.wired_limit_mb=<size_in_megabytes>

Use [device_info()](mlx.core.device_info.html#mlx.core.device_info) to query the system wired limit
(`"max_recommended_working_set_size"`) and the total memory size
(`"memory_size"`).

Parameters:
**limit** ([int](https://docs.python.org/3/library/functions.html#int)) – The wired limit in bytes.

Returns:
The previous wired limit in bytes.

Return type:
[int](https://docs.python.org/3/library/functions.html#int)

** Contents
