---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.argmin.html
---

# mlx.core.argmin

**

- [.rst](../../_sources/python/_autosummary/mlx.core.argmin.rst)
- **

.pdf

**

# mlx.core.argmin

 Table of contents 

## Contents

# mlx.core.argmin

**argmin(*a: array*, */*, *axis: None | int = None*, *keepdims: bool = False*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Indices of the minimum values along the axis.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Optional axis to reduce over. If unspecified
this defaults to reducing over the entire array.
**keepdims** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Keep reduced axes as
singleton dimensions, defaults to False.

Returns:
The `uint32` array with the indices of the minimum values.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
