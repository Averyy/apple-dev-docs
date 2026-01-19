---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.async_eval.html
---

# mlx.core.async_eval

**

- [.rst](../../_sources/python/_autosummary/mlx.core.async_eval.rst)
- **

.pdf

**

# mlx.core.async_eval

 Table of contents 

## Contents

# mlx.core.async_eval

**async_eval(**args*)**
: Asynchronously evaluate an [array](mlx.core.array.html#mlx.core.array) or tree of [array](mlx.core.array.html#mlx.core.array).

Note
This is an experimental API and may change in future versions.

Parameters:
***args** (*arrays** or **trees** of **arrays*) – Each argument can be a single array
or a tree of arrays. If a tree is given the nodes can be a Python
[list](https://docs.python.org/3/library/stdtypes.html#list), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple) or [dict](https://docs.python.org/3/library/stdtypes.html#dict). Leaves which are not
arrays are ignored.

Example
>>> x = mx.array(1.0)
>>> y = mx.exp(x)
>>> mx.async_eval(y)
>>> print(y)
>>>
>>> y = mx.exp(x)
>>> mx.async_eval(y)
>>> z = y + 3
>>> mx.async_eval(z)
>>> print(z)

** Contents
