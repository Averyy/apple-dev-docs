---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.ordered_prefetch.html
---

# mlx.data.Buffer.ordered_prefetch

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.ordered_prefetch.rst)
- **

.pdf

**

# mlx.data.Buffer.ordered_prefetch

 Table of contents 

## Contents

# mlx.data.Buffer.ordered_prefetch

**Buffer.ordered_prefetch(*self: mlx.data._c.Buffer*, *prefetch_size: int*, *num_thread: int*) → mlx.data._c.Stream**
: Fetch samples in background threads, while preserving original ordering.
This operation is the workhorse of data loading. It uses
`num_threads` background threads and fetches
`prefetch_size` samples so that they are ready to be used
when needed.
Prefetch can be used both to parallelize operations but also to
overlap computation with data loading in a background thread.
If you don’t need deterministic ordering, look for [Stream.prefetch()](mlx.data.Stream.prefetch.html#mlx.data.Stream.prefetch)
instead, as it may be more efficient.
# The final prefetch is parallelizing the whole pipeline and
# ensures that images are going to be available for training.
dset = (
  dset
  .load_image("image")
  .image_resize_smallest_side("image", 256)
  .image_center_crop("image", 256, 256)
  .batch(32)
  .ordered_prefetch(8, 8)
)

Parameters:

**num_partitions** ([int](https://docs.python.org/3/library/functions.html#int)) – How many different partitions to split the buffer into.
**partition** ([int](https://docs.python.org/3/library/functions.html#int)) – Which partition to use (0-based).

** Contents
