---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.partition.html
---

# mlx.data.Buffer.partition

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.partition.rst)
- **

.pdf

**

# mlx.data.Buffer.partition

 Table of contents 

## Contents

# mlx.data.Buffer.partition

**Buffer.partition(*self: mlx.data._c.Buffer*, *num_partitions: int*, *partition: int*) → mlx.data._c.Buffer**
: Equivalent to slicing the buffer with a step equal to
`num_partitions` and starting offset of `partition`.
This can be used for distributed settings where different nodes
should load different parts of a dataset.

Parameters:

**num_partitions** ([int](https://docs.python.org/3/library/functions.html#int)) – How many different partitions to split the buffer into.
**partition** ([int](https://docs.python.org/3/library/functions.html#int)) – Which partition to use (0-based).

** Contents
