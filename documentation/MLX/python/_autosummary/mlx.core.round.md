---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.round.html
---

# mlx.core.round

**

- [.rst](../../_sources/python/_autosummary/mlx.core.round.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.round

 Table of contents 

## Contents

# mlx.core.round

**round(*a: array*, */*, *decimals: int = 0*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Round to the given number of decimals.
Basically performs:
s = 10**decimals
x = round(x * s) / s

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**decimals** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of decimal places to round to. (default: 0)

Returns:
An array of the same type as `a` rounded to the
given number of decimals.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
