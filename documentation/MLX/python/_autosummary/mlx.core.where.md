---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.where.html
---

# mlx.core.where

**

- [.rst](../../_sources/python/_autosummary/mlx.core.where.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.where

 Table of contents 

## Contents

# mlx.core.where

**where(*condition: scalar | array*, *x: scalar | array*, *y: scalar | array*, */*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Select from `x` or `y` according to `condition`.
The condition and input arrays must be the same shape or
broadcastable with each another.

Parameters:

**condition** ([array](mlx.core.array.html#mlx.core.array)) – The condition array.
**x** ([array](mlx.core.array.html#mlx.core.array)) – The input selected from where condition is `True`.
**y** ([array](mlx.core.array.html#mlx.core.array)) – The input selected from where condition is `False`.

Returns:
The output containing elements selected from
`x` and `y`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
