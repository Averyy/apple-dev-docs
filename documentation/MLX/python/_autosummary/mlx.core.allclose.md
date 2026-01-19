---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.allclose.html
---

# mlx.core.allclose

**

- [.rst](../../_sources/python/_autosummary/mlx.core.allclose.rst)
- **

.pdf

**

# mlx.core.allclose

 Table of contents 

## Contents

# mlx.core.allclose

**allclose(*a: array*, *b: array*, */*, *rtol: float = 1e-05*, *atol: float = 1e-08*, ***, *equal_nan: bool = False*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Approximate comparison of two arrays.
Infinite values are considered equal if they have the same sign, NaN values are not equal unless `equal_nan` is `True`.
The arrays are considered equal if:
all(abs(a - b) <= (atol + rtol * abs(b)))

Note unlike [array_equal()](mlx.core.array_equal.html#mlx.core.array_equal), this function supports numpy-style
broadcasting.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**rtol** ([float](https://docs.python.org/3/library/functions.html#float)) – Relative tolerance.
**atol** ([float](https://docs.python.org/3/library/functions.html#float)) – Absolute tolerance.
**equal_nan** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If `True`, NaNs are considered equal.
Defaults to `False`.

Returns:
The boolean output scalar indicating if the arrays are close.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
