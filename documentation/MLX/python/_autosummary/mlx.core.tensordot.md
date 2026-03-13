---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.tensordot.html
---

# mlx.core.tensordot

**

- [.rst](../../_sources/python/_autosummary/mlx.core.tensordot.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.tensordot

 Table of contents 

## Contents

# mlx.core.tensordot

**tensordot(*a: array*, *b: array*, */*, *axes: int | list[Sequence[int]] = 2*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the tensor dot product along the specified axes.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**axes** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**)**, **optional*) – The number of dimensions to
sum over. If an integer is provided, then sum over the last
`axes` dimensions of `a` and the first `axes` dimensions of
`b`. If a list of lists is provided, then sum over the
corresponding dimensions of `a` and `b`. Default: 2.

Returns:
The tensor dot product.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
