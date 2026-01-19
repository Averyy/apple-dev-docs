---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.pad.html
---

# mlx.core.pad

**

- [.rst](../../_sources/python/_autosummary/mlx.core.pad.rst)
- **

.pdf

**

# mlx.core.pad

 Table of contents 

## Contents

# mlx.core.pad

**pad(*a: array*, *pad_width: int | tuple[int] | tuple[int, int] | list[tuple[int, int]]*, *mode: Literal['constant', 'edge'] = 'constant'*, *constant_values: scalar | array = 0*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Pad an array with a constant value

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**pad_width** ([int](https://docs.python.org/3/library/functions.html#int)*, *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*) or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*)**)*) – Number of padded
values to add to the edges of each axis:`((before_1, after_1),
(before_2, after_2), ..., (before_N, after_N))`. If a single pair
of integers is passed then `(before_i, after_i)` are all the same.
If a single integer or tuple with a single integer is passed then
all axes are extended by the same number on each side.
**mode** – Padding mode. One of the following strings:
“constant” (default): Pads with a constant value.
“edge”: Pads with the edge values of array.
**constant_value** ([array](mlx.core.array.html#mlx.core.array)* or **scalar**, **optional*) – Optional constant value
to pad the edges of the array with.

Returns:
The padded array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
