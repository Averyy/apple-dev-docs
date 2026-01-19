---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.core.AWSFileFetcher.prefetch.html
---

# mlx.data.core.AWSFileFetcher.prefetch

**

- [.rst](../../_sources/python/_autosummary/mlx.data.core.AWSFileFetcher.prefetch.rst)
- **

.pdf

**

# mlx.data.core.AWSFileFetcher.prefetch

 Table of contents 

## Contents

# mlx.data.core.AWSFileFetcher.prefetch

**AWSFileFetcher.prefetch(*self: mlx.data._c.core.FileFetcher*, *filenames: List[str]*) → [None](https://docs.python.org/3/library/constants.html#None)**
: Start prefetching these files.
`num_prefetch_max` files are downloaded with
`num_prefetch_threads` parallelism. When one of the prefetched
files is accessed by `fetch` then more of the prefetch file list is
downloaded.
At any given point we keep `num_kept_files` in the local cache.

Parameters:
**filenames** ([list](https://docs.python.org/3/library/stdtypes.html#list)*[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – A list of filenames to be prefetched in order.

** Contents
