---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/devices_and_streams.html
---

# Devices and Streams

| [Device](_autosummary/mlx.core.Device.md#mlx.core.Device)(*args, **kwargs) | A device to run operations on. |
| --- | --- |
| [Stream](_autosummary/stream_class.md#mlx.core.Stream) | A stream for running operations on a given device. |
| [ThreadLocalStream](_autosummary/mlx.core.ThreadLocalStream.md#mlx.core.ThreadLocalStream) | A stream that will be unique per thread and can be used to run operations on a given device. |
| [default_device](_autosummary/mlx.core.default_device.md#mlx.core.default_device)() | Get the default device. |
| [set_default_device](_autosummary/mlx.core.set_default_device.md#mlx.core.set_default_device)(device) | Set the default device. |
| [default_stream](_autosummary/mlx.core.default_stream.md#mlx.core.default_stream)(device) | Get the device's default stream. |
| [new_stream](_autosummary/mlx.core.new_stream.md#mlx.core.new_stream)(device) | Make a new stream on the given device. |
| [new_thread_local_stream](_autosummary/mlx.core.new_thread_local_stream.md#mlx.core.new_thread_local_stream)(device) | Make a new stream that will be unique per thread. |
| [new_thread_unsafe_stream](_autosummary/mlx.core.new_thread_unsafe_stream.md#mlx.core.new_thread_unsafe_stream)(device) | Make a new stream that can be used in any thread. |
| [set_default_stream](_autosummary/mlx.core.set_default_stream.md#mlx.core.set_default_stream)(stream) | Set the default stream. |
| [stream](_autosummary/mlx.core.stream.md#mlx.core.stream)(s) | Create a context manager to set the default device and stream. |
| [synchronize](_autosummary/mlx.core.synchronize.md#mlx.core.synchronize)([stream]) | Synchronize with the given stream. |
| [clear_streams](_autosummary/mlx.core.clear_streams.md#mlx.core.clear_streams)() | Destroy all streams created in current thread. |
| [device_count](_autosummary/mlx.core.device_count.md#mlx.core.device_count)(device_type) | Get the number of available devices for the given device type. |
| [device_info](_autosummary/mlx.core.device_info.md#mlx.core.device_info)([d]) | Get information about a device. |
