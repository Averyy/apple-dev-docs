---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.meshgrid.html
---

# mlx.core.meshgrid

**

- [.rst](../../_sources/python/_autosummary/mlx.core.meshgrid.rst)
- **

.pdf

**

# mlx.core.meshgrid

 Table of contents 

## Contents

# mlx.core.meshgrid

**meshgrid(**arrays: array*, *sparse: bool | None = False*, *indexing: str | None = 'xy'*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate multidimensional coordinate grids from 1-D coordinate arrays

Parameters:

***arrays** ([array](mlx.core.array.html#mlx.core.array)) – Input arrays.
**sparse** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, a sparse grid is returned in which each output
array has a single non-zero element. If `False`, a dense grid is returned.
Defaults to `False`.
**indexing** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Cartesian (‘xy’) or matrix (‘ij’) indexing of the output arrays.
Defaults to `'xy'`.

Returns:
The output arrays.

Return type:
[list](https://docs.python.org/3/library/stdtypes.html#list)([array](mlx.core.array.html#mlx.core.array))

** Contents
