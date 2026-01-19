---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.roll.html
---

# mlx.core.roll

**

- [.rst](../../_sources/python/_autosummary/mlx.core.roll.rst)
- **

.pdf

**

# mlx.core.roll

 Table of contents 

## Contents

# mlx.core.roll

**roll(*a: array*, *shift: int | Tuple[int]*, *axis: None | int | Tuple[int] = None*, */*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Roll array elements along a given axis.
Elements that are rolled beyond the end of the array are introduced at
the beggining and vice-versa.
If the axis is not provided the array is flattened, rolled and then the
shape is restored.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**shift** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – The number of places by which elements
are shifted. If positive the array is rolled to the right, if
negative it is rolled to the left. If an int is provided but the
axis is a tuple then the same value is used for all axes.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – The axis or axes along which to
roll the elements.

** Contents
