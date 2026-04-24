---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.device_info.html
---

# mlx.core.device_info

**

- [.rst](../../_sources/python/_autosummary/mlx.core.device_info.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.device_info

 Table of contents 

## Contents

# mlx.core.device_info

**device_info(*d: Device | None = None*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [str](https://docs.python.org/3/library/stdtypes.html#str) | [int](https://docs.python.org/3/library/functions.html#int)]**
: Get information about a device.
Returns a dictionary with device properties. Available keys depend
on the backend and device type. Common keys include `device_name`,
`architecture`, and `total_memory` (or `memory_size`).

Parameters:
**d** ([Device](mlx.core.Device.html#mlx.core.Device)) – The device to query (defaults to the default device).

Returns:
Device information.

Return type:
[dict](https://docs.python.org/3/library/stdtypes.html#dict)

** Contents
