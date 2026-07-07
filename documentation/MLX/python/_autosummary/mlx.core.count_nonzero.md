---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.count_nonzero.html
---

# mlx.core.count_nonzero

**

- [.rst](../../_sources/python/_autosummary/mlx.core.count_nonzero.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.count_nonzero

 Table of contents 

## Contents

# mlx.core.count_nonzero

**count_nonzero(*a: array*, */*, ***, *axis: None | int | Sequence[int] = None*, *keepdims: bool = False*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Count the number of non-zero elements along the given axis.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Axis or axes to count over.
Defaults to `None` in which case the whole array is counted.
**keepdims** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Keep the reduced axes as size one.
Default: `False`.

Returns:
The counts as an `int32` array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
