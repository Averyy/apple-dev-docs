---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.std.html
---

# mlx.core.std

**

- [.rst](../../_sources/python/_autosummary/mlx.core.std.rst)
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

# mlx.core.std

 Table of contents 

## Contents

# mlx.core.std

**std(*a: array*, */*, *axis: None | int | Sequence[int] = None*, *keepdims: bool = False*, *ddof: int = 0*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the standard deviation(s) over the given axes.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Optional axis or
axes to reduce over. If unspecified this defaults
to reducing over the entire array.
**keepdims** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Keep reduced axes as
singleton dimensions, defaults to False.
**ddof** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The divisor to compute the variance
is `N - ddof`, defaults to 0.

Returns:
The output array of standard deviations.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
