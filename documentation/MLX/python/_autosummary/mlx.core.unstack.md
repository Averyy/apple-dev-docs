---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.unstack.html
---

# mlx.core.unstack

**

- [.rst](../../_sources/python/_autosummary/mlx.core.unstack.rst)
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

# mlx.core.unstack

 Table of contents 

## Contents

# mlx.core.unstack

**unstack(*x: array*, */*, ***, *axis: int = 0*, *stream: StreamOrDevice = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list)[[array](mlx.core.array.html#mlx.core.array)]**
: Split an array into a sequence of arrays along the given axis.
The inverse of [stack()](mlx.core.stack.html#mlx.core.stack). The given axis is removed from each of
the returned arrays.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Axis along which to unstack. Default: `0`.

Returns:
A list of arrays, one for each index along `axis`.

Return type:
[list](https://docs.python.org/3/library/stdtypes.html#list)([array](mlx.core.array.html#mlx.core.array))

** Contents
