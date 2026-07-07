---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.compile.html
---

# mlx.core.compile

**

- [.rst](../../_sources/python/_autosummary/mlx.core.compile.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.compile

 Table of contents 

## Contents

# mlx.core.compile

**compile(*fun: Callable[P, R]*, *inputs: object | None = None*, *outputs: object | None = None*, *shapeless: bool = False*) → Callable[P, R]**
: Returns a compiled function which produces the same output as `fun`.

Parameters:

**fun** (*Callable*) – A function which takes a variable number of
[array](mlx.core.array.html#mlx.core.array) or trees of [array](mlx.core.array.html#mlx.core.array) and returns
a variable number of [array](mlx.core.array.html#mlx.core.array) or trees of [array](mlx.core.array.html#mlx.core.array).
**inputs** ([list](https://docs.python.org/3/library/stdtypes.html#list)* or *[dict](https://docs.python.org/3/library/stdtypes.html#dict)*, **optional*) – These inputs will be captured during
the function compilation along with the inputs to `fun`. The `inputs`
can be a [list](https://docs.python.org/3/library/stdtypes.html#list) or a [dict](https://docs.python.org/3/library/stdtypes.html#dict) containing arbitrarily nested
lists, dictionaries, or arrays. Leaf nodes that are not
[array](mlx.core.array.html#mlx.core.array) are ignored. Default: `None`
**outputs** ([list](https://docs.python.org/3/library/stdtypes.html#list)* or *[dict](https://docs.python.org/3/library/stdtypes.html#dict)*, **optional*) – These outputs will be captured and
updated in a compiled function. The `outputs` can be a
[list](https://docs.python.org/3/library/stdtypes.html#list) or a [dict](https://docs.python.org/3/library/stdtypes.html#dict) containing arbitrarily nested lists,
dictionaries, or arrays. Leaf nodes that are not [array](mlx.core.array.html#mlx.core.array) are ignored.
Default: `None`
**shapeless** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – A function compiled with the `shapeless`
option enabled will not be recompiled when the input shape changes. Not all
functions can be compiled with `shapeless` enabled. Attempting to compile
such functions with shapeless enabled will throw. Note, changing the number
of dimensions or type of any input will result in a recompilation even with
`shapeless` set to `True`. Default: `False`

Returns:
A compiled function which has the same input arguments
as `fun` and returns the same output(s).

Return type:
*Callable*

** Contents
