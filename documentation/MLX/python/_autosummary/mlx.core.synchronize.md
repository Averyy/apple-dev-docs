---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.synchronize.html
---

# mlx.core.synchronize

```python
synchronize(stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None) → None
```

Synchronize with the given stream.

**Parameters:**
: **stream** ([Stream](stream_class.md#mlx.core.Stream), *optional*) – Stream to synchronize. If device is
provided the default stream for that device is used. If `None`
then the default stream of the default device is used.
Default: `None`.
