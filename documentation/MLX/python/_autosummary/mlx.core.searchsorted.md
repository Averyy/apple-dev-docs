---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.searchsorted.html
---

# mlx.core.searchsorted

**

- [.rst](../../_sources/python/_autosummary/mlx.core.searchsorted.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.core.searchsorted

 Table of contents 

## Contents

# mlx.core.searchsorted

**searchsorted(*sorted_sequence: array*, *values: array*, */*, *side: str = 'left'*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Find the indices that keep `sorted_sequence` sorted when inserting `values`.

Parameters:

**sorted_sequence** ([array](mlx.core.array.html#mlx.core.array)) – A 1-D array sorted in ascending order.
**values** ([array](mlx.core.array.html#mlx.core.array)) – The values to insert. May have any shape.
**side** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Either `'left'` or `'right'`. With
`'left'` the first suitable index is returned, so the result is
the number of elements strictly less than the value. With
`'right'` the last is returned, so the result is the number of
elements less than or equal to it. The two differ only where a
value is already present. Default: `'left'`.

Returns:
A `uint32` array with the same shape as `values`, holding
indices in `[0, sorted_sequence.size]`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

Example
>>> a = mx.array([1, 2, 2, 4])
>>> mx.searchsorted(a, mx.array([0, 2, 3, 5]))
array([0, 1, 3, 4], dtype=uint32)
>>> mx.searchsorted(a, mx.array([0, 2, 3, 5]), side="right")
array([0, 3, 3, 4], dtype=uint32)

** Contents
