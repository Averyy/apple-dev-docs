---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.any.html
---

# mlx.core.any

**

- [.rst](../../_sources/python/_autosummary/mlx.core.any.rst)
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

# mlx.core.any

 Table of contents 

## Contents

# mlx.core.any

**any(*a: array*, */*, *axis: None | int | Sequence[int] = None*, *keepdims: bool = False*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: An or reduction over the given axes.

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
