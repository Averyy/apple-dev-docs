---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Stream.partition.html
---

# mlx.data.Stream.partition

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Stream.partition.rst)
- **

.pdf

**

# mlx.data.Stream.partition

 Table of contents 

## Contents

# mlx.data.Stream.partition

**Stream.partition(*self: mlx.data._c.Stream*, *num_partitions: int*, *partition: int*) → mlx.data._c.Stream**
: For every `num_partitions` consecutive samples return the `partition`-th.
This can be used for distributed settings where different nodes
should load different parts of a dataset.

Parameters:

**num_partitions** ([int](https://docs.python.org/3/library/functions.html#int)) – How many different partitions to split the stream into.
**partition** ([int](https://docs.python.org/3/library/functions.html#int)) – Which partition to use (0-based).

** Contents
