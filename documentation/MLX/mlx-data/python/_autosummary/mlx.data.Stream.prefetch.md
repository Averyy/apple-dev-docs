---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Stream.prefetch.html
---

# mlx.data.Stream.prefetch

```python
Stream.prefetch(self: mlx.data._c.Stream, prefetch_size: int, num_threads: int) → mlx.data._c.Stream
```

Fetch samples in background threads.

This operation is the workhorse of data loading. It uses
`num_threads` background threads and fetches
`prefetch_size` samples so that they are ready to be used
when needed.

Prefetch can be used both to parallelize operations but also to
overlap computation with data loading in a background thread.

This prefetching order is not deterministic and samples’ ordering depends
on scheduling of the threads. If you need deterministic ordering, look for
[Buffer.ordered_prefetch()](mlx.data.Buffer.ordered_prefetch.md#mlx.data.Buffer.ordered_prefetch) instead.

```
# The final prefetch is parallelizing the whole pipeline and
# ensures that images are going to be available for training.
dset = (
  dset
  .load_image("image")
  .image_resize_smallest_side("image", 256)
  .image_center_crop("image", 256, 256)
  .batch(32)
  .prefetch(8, 8)
)
```

**Parameters:**

- **prefetch_size** ([int](https://docs.python.org/3/library/functions.html#int)) – How many samples to prefetch.
- **num_threads** ([int](https://docs.python.org/3/library/functions.html#int)) – How many background threads to launch.
