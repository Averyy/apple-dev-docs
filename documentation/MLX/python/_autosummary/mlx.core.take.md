---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.take.html
---

# mlx.core.take

**

- [.rst](../../_sources/python/_autosummary/mlx.core.take.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.take

 Table of contents 

## Contents

# mlx.core.take

**take(*a: array*, */*, *indices: int | array*, *axis: int | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Take elements along an axis.
The elements are taken from `indices` along the specified axis.
If the axis is not specified the array is treated as a flattened
1-D array prior to performing the take.
As an example, if the `axis=1` this is equivalent to `a[:, indices, ...]`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**indices** ([int](https://docs.python.org/3/library/functions.html#int)* or *[array](mlx.core.array.html#mlx.core.array)) – Integer index or input array with integral type.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Axis along which to perform the take. If unspecified
the array is treated as a flattened 1-D vector.

Returns:
The indexed values of `a`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
