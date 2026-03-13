---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.put_along_axis.html
---

# mlx.core.put_along_axis

**

- [.rst](../../_sources/python/_autosummary/mlx.core.put_along_axis.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.put_along_axis

 Table of contents 

## Contents

# mlx.core.put_along_axis

**put_along_axis(*a: array*, */*, *indices: array*, *values: array*, *axis: int | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Put values along an axis at the specified indices.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Destination array.
**indices** ([array](mlx.core.array.html#mlx.core.array)) – Indices array. These should be broadcastable with
the input array excluding the axis dimension.
**values** ([array](mlx.core.array.html#mlx.core.array)) – Values array. These should be broadcastable with
the indices.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or **None*) – Axis in the destination to put the values to. If
`axis == None` the destination is flattened prior to the put
operation.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
