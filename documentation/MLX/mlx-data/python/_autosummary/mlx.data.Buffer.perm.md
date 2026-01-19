---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.perm.html
---

# mlx.data.Buffer.perm

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.perm.rst)
- **

.pdf

**

# mlx.data.Buffer.perm

 Table of contents 

## Contents

# mlx.data.Buffer.perm

**Buffer.perm(*self: mlx.data._c.Buffer*, *perm: List[int]*) → mlx.data._c.Buffer**
: Arbitrarily reorder the buffer with the provided indices.
This operation actually performs arbitrary indexing of the
buffer which means it can be used to slice or filter the buffer.
It should be renamed in the future to avoid confusion.

Parameters:
**perm** ([list](https://docs.python.org/3/library/stdtypes.html#list)* of **ints*) – The indices defining the permutation/selection.

** Contents
