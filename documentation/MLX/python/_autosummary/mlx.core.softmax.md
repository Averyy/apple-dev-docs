---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.softmax.html
---

# mlx.core.softmax

**

- [.rst](../../_sources/python/_autosummary/mlx.core.softmax.rst)
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

# mlx.core.softmax

 Table of contents 

## Contents

# mlx.core.softmax

**softmax(*a: array*, */*, *axis: None | int | Sequence[int] = None*, ***, *precise: bool = False*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Perform the softmax along the given axis.
This operation is a numerically stable version of:
exp(a) / sum(exp(a), axis, keepdims=True)

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Optional axis or axes to compute
the softmax over. If unspecified this performs the softmax over
the full array.
**precise** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Accumulate in `float32` for inputs of
lower precision. Otherwise the accumulation type matches the
input, which can lose precision over long reduction axes.
Default: `False`.

Returns:
The output of the softmax.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
