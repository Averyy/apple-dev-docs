---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.new_stream.html
---

# mlx.core.new_stream

```python
new_stream(device: Device | DeviceType) → Stream
```

Make a new stream on the given device.

The stream can only be used on the thread where it was created on, using
it in any other thread would result in errors.
