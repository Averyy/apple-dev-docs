---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.softmax.html
---

# mlx.core.softmax

**

- [.rst](../../_sources/python/_autosummary/mlx.core.softmax.rst)
- **

.pdf

**

# mlx.core.softmax

 Table of contents 

## Contents

# mlx.core.softmax

**softmax(*a: array*, */*, *axis: None | int | Sequence[int] = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Perform the softmax along the given axis.
This operation is a numerically stable version of:
exp(a) / sum(exp(a), axis, keepdims=True)

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Optional axis or axes to compute
the softmax over. If unspecified this performs the softmax over
the full array.

Returns:
The output of the softmax.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
