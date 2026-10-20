---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.stream.html
---

# mlx.core.stream

**stream(*s: Stream | ThreadLocalStream | Device | mlx.core.DeviceType*) → mlx.core.StreamContext**
: Create a context manager to set the default device and stream.

Parameters:
**s** – The [Stream](stream_class.md#mlx.core.Stream) or [Device](mlx.core.Device.md#mlx.core.Device) to set as the default.

Returns:
A context manager that sets the default device and stream.

Example:
