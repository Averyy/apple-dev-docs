---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.split.html
---

# mlx.core.split

**

- [.rst](../../_sources/python/_autosummary/mlx.core.split.rst)
- **

.pdf

**

# mlx.core.split

 Table of contents 

## Contents

# mlx.core.split

**split(*a: array*, */*, *indices_or_sections: int | Sequence[int]*, *axis: int = 0*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Split an array along a given axis.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**indices_or_sections** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – If `indices_or_sections`
is an integer the array is split into that many sections of equal
size. An error is raised if this is not possible. If
`indices_or_sections` is a list, then the indices are the split
points, and the array is divided into
`len(indices_or_sections) + 1` sub-arrays.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Axis to split along, defaults to 0.

Returns:
A list of split arrays.

Return type:
[list](https://docs.python.org/3/library/stdtypes.html#list)([array](mlx.core.array.html#mlx.core.array))

Example
>>> a = mx.array([1, 2, 3, 4], dtype=mx.int32)
>>> mx.split(a, 2)
[array([1, 2], dtype=int32), array([3, 4], dtype=int32)]
>>> mx.split(a, [1, 3])
[array([1], dtype=int32), array([2, 3], dtype=int32), array([4], dtype=int32)]

** Contents
