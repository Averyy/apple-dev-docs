---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.distributed.all_min.html
---

# mlx.core.distributed.all_min

```python
all_min(x: array, *, group: Group | None = None, stream: StreamOrDevice = None) → array
```

All reduce min.

Find the minimum of the `x` arrays from all processes in the group.

**Parameters:**

- **x** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
- **group** ([Group](mlx.core.distributed.Group.md#mlx.core.distributed.Group)) – The group of processes that will participate in the
reduction. If set to `None` the global group is used. Default:
`None`.
- **stream** ([Stream](stream_class.md#mlx.core.Stream), *optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

**Returns:**
: The minimum of all `x` arrays.

**Return type:**
: [array](mlx.core.array.md#mlx.core.array)
