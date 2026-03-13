---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.take_along_axis.html
---

# mlx.core.take_along_axis

**

- [.rst](../../_sources/python/_autosummary/mlx.core.take_along_axis.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.take_along_axis

 Table of contents 

## Contents

# mlx.core.take_along_axis

**take_along_axis(*a: array*, */*, *indices: array*, *axis: int | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Take values along an axis at the specified indices.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**indices** ([array](mlx.core.array.html#mlx.core.array)) – Indices array. These should be broadcastable with
the input array excluding the axis dimension.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or **None*) – Axis in the input to take the values from. If
`axis == None` the array is flattened to 1D prior to the indexing
operation.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
