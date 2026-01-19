---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.clip.html
---

# mlx.core.clip

**

- [.rst](../../_sources/python/_autosummary/mlx.core.clip.rst)
- **

.pdf

**

# mlx.core.clip

 Table of contents 

## Contents

# mlx.core.clip

**clip(*a: array*, */*, *a_min: scalar | array | None*, *a_max: scalar | array | None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Clip the values of the array between the given minimum and maximum.
If either `a_min` or `a_max` are `None`, then corresponding edge
is ignored. At least one of `a_min` and `a_max` cannot be `None`.
The input `a` and the limits must broadcast with one another.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**a_min** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)* or **None*) – Minimum value to clip to.
**a_max** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)* or **None*) – Maximum value to clip to.

Returns:
The clipped array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
