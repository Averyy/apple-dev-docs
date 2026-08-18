---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.array_equal.html
---

# mlx.core.array_equal

**

- [.rst](../../_sources/python/_autosummary/mlx.core.array_equal.rst)
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

# mlx.core.array_equal

 Table of contents 

## Contents

# mlx.core.array_equal

**array_equal(*a: scalar | array*, *b: scalar | array*, *equal_nan: bool = False*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Array equality check.
Compare two arrays for equality. Returns `True` if and only if the arrays
have the same shape and their values are equal. The arrays need not have
the same type to be considered equal.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**equal_nan** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If `True`, NaNs are considered equal.
Defaults to `False`.

Returns:
A scalar boolean array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
