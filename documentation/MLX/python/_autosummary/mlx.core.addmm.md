---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.addmm.html
---

# mlx.core.addmm

**

- [.rst](../../_sources/python/_autosummary/mlx.core.addmm.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.addmm

 Table of contents 

## Contents

# mlx.core.addmm

**addmm(*c: array*, *a: array*, *b: array*, */*, *alpha: float = 1.0*, *beta: float = 1.0*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Matrix multiplication with addition and optional scaling.
Perform the (possibly batched) matrix multiplication of two arrays and add to the result
with optional scaling factors.

Parameters:

**c** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**alpha** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Scaling factor for the
matrix product of `a` and `b` (default: `1`)
**beta** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Scaling factor for `c` (default: `1`)

Returns:
`alpha * (a @ b)  + beta * c`

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
