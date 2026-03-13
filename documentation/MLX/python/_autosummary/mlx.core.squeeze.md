---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.squeeze.html
---

# mlx.core.squeeze

**

- [.rst](../../_sources/python/_autosummary/mlx.core.squeeze.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.squeeze

 Table of contents 

## Contents

# mlx.core.squeeze

**squeeze(*a: array*, */*, *axis: None | int | Sequence[int] = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Remove length one axes from an array.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Axes to remove. Defaults
to `None` in which case all size one axes are removed.

Returns:
The output array with size one axes removed.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
