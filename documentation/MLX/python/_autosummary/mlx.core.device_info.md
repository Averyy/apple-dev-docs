---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.device_info.html
---

# mlx.core.device_info

```python
device_info(d: None | Device | DeviceType = None) → dict[str, str | int]
```

Get information about a device.

Returns a dictionary with device properties. Available keys depend
on the backend and device type. Common keys include `device_name`,
`architecture`, and `total_memory` (or `memory_size`).

**Parameters:**
: **d** ([Device](mlx.core.Device.md#mlx.core.Device)) – The device to query (defaults to the default device).

**Returns:**
: Device information.

**Return type:**
: [dict](https://docs.python.org/3/builtins/stdtypes.html#dict)
