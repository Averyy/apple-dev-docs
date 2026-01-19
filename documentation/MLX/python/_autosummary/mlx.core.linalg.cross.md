---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.cross.html
---

# mlx.core.linalg.cross

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.cross.rst)
- **

.pdf

**

# mlx.core.linalg.cross

 Table of contents 

## Contents

# mlx.core.linalg.cross

**cross(*a: array*, *b: array*, *axis: int = -1*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the cross product of two arrays along a specified axis.
The cross product is defined for arrays with size 2 or 3 in the
specified axis. If the size is 2 then the third value is assumed
to be zero.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Axis along which to compute the cross
product. Default: `-1`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The cross product of `a` and `b` along the specified axis.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
