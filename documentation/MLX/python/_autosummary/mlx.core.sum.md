---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.sum.html
---

# mlx.core.sum

**

- [.rst](../../_sources/python/_autosummary/mlx.core.sum.rst)
- **

.pdf

**

# mlx.core.sum

 Table of contents 

## Contents

# mlx.core.sum

**sum(*a: array*, */*, *axis: None | int | Sequence[int] = None*, *keepdims: bool = False*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Sum reduce the array over the given axes.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Optional axis or
axes to reduce over. If unspecified this defaults
to reducing over the entire array.
**keepdims** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Keep reduced axes as
singleton dimensions, defaults to False.

Returns:
The output array with the corresponding axes reduced.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
