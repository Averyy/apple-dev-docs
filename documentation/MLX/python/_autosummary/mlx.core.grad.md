---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.grad.html
---

# mlx.core.grad

**

- [.rst](../../_sources/python/_autosummary/mlx.core.grad.rst)
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

# mlx.core.grad

 Table of contents 

## Contents

# mlx.core.grad

**grad(*fun: Callable[P, R]*, *argnums: int | Sequence[int] | None = None*, *argnames: str | Sequence[str] = []*) → Callable[P, Any]**
: Returns a function which computes the gradient of `fun`.

Parameters:

**fun** (*Callable*) – A function which takes a variable number of
[array](mlx.core.array.html#mlx.core.array) or trees of [array](mlx.core.array.html#mlx.core.array) and returns
a scalar output [array](mlx.core.array.html#mlx.core.array).
**argnums** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Specify the index (or indices)
of the positional arguments of `fun` to compute the gradient
with respect to. If neither `argnums` nor `argnames` are
provided `argnums` defaults to `0` indicating `fun`’s first
argument.
**argnames** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[str](https://docs.python.org/3/library/stdtypes.html#str)*)**, **optional*) – Specify keyword arguments of
`fun` to compute gradients with respect to. It defaults to [] so
no gradients for keyword arguments by default.

Returns:
A function which has the same input arguments as `fun` and
returns the gradient(s).

Return type:
*Callable*

** Contents
