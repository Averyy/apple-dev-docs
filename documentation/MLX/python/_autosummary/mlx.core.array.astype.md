---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.array.astype.html
---

# mlx.core.array.astype

```python
array.astype(self, dtype: Dtype, stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None) → array
```

Cast the array to a specified type.

**Parameters:**

- **dtype** ([Dtype](mlx.core.Dtype.md#mlx.core.Dtype)) – Type to which the array is cast.
- **stream** ([Stream](stream_class.md#mlx.core.Stream)) – Stream (or device) for the operation.

**Returns:**
: The array with type `dtype`.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
