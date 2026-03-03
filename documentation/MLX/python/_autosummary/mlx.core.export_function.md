---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.export_function.html
---

# mlx.core.export_function

**

- [.rst](../../_sources/python/_autosummary/mlx.core.export_function.rst)
- **

.pdf

**

# mlx.core.export_function

 Table of contents 

## Contents

# mlx.core.export_function

**export_function(*file_or_callback: str | Callable*, *fun: Callable*, **args*, *shapeless: bool = False*, ***kwargs*) → [None](https://docs.python.org/3/library/constants.html#None)**
: Export an MLX function.
Example input arrays must be provided to export a function. The example
inputs can be variable `*args` and `**kwargs` or a tuple of arrays
and/or dictionary of string keys with array values.

Warning
This is part of an experimental API which is likely to
change in future versions of MLX. Functions exported with older
versions of MLX may not be compatible with future versions.

Parameters:

**file_or_callback** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or **Callable*) – Either a file path to export
the function to or a callback.
**fun** (*Callable*) – A function which takes as input zero or more
[array](mlx.core.array.html#mlx.core.array) and returns one or more [array](mlx.core.array.html#mlx.core.array).
***args** ([array](mlx.core.array.html#mlx.core.array)) – Example array inputs to the function.
**shapeless** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether or not the function allows
inputs with variable shapes. Default: `False`.
****kwargs** ([array](mlx.core.array.html#mlx.core.array)) – Additional example keyword array inputs to the
function.

Example
def fun(x, y):
    return x + y

x = mx.array(1)
y = mx.array([1, 2, 3])
mx.export_function("fun.mlxfn", fun, x, y=y)

** Contents
