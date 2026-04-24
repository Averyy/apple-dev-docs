---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/devices_and_streams.html
---

# Devices and Streams

**

- [.rst](../_sources/python/devices_and_streams.rst)
- **

.pdf

**

**
**
**

**

# Devices and Streams

 Table of contents 

# Devices and Streams

| Device(*args, **kwargs) | A device to run operations on. |
| --- | --- |
| Stream | A stream for running operations on a given device. |
| default_device() | Get the default device. |
| set_default_device(device) | Set the default device. |
| default_stream(device) | Get the device's default stream. |
| new_stream(device) | Make a new stream on the given device. |
| new_thread_local_stream(device) | Make a new stream that will be unique per thread. |
| set_default_stream(stream) | Set the default stream. |
| stream(s) | Create a context manager to set the default device and stream. |
| synchronize([stream]) | Synchronize with the given stream. |
| clear_streams() | Destroy all streams created in current thread. |
| device_count(device_type) | Get the number of available devices for the given device type. |
| device_info([d]) | Get information about a device. |
