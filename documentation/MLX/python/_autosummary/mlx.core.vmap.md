---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.vmap.html
---

# mlx.core.vmap

**

- [.rst](../../_sources/python/_autosummary/mlx.core.vmap.rst)
- **

.pdf

**

# mlx.core.vmap

 Table of contents 

## Contents

# mlx.core.vmap

**vmap(*fun: Callable*, *in_axes: object = 0*, *out_axes: object = 0*) → Callable**
: Returns a vectorized version of `fun`.

Parameters:

**fun** (*Callable*) – A function which takes a variable number of
[array](mlx.core.array.html#mlx.core.array) or a tree of [array](mlx.core.array.html#mlx.core.array) and returns
a variable number of [array](mlx.core.array.html#mlx.core.array) or a tree of [array](mlx.core.array.html#mlx.core.array).
**in_axes** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – An integer or a valid prefix tree of the
inputs to `fun` where each node specifies the vmapped axis. If
the value is `None` then the corresponding input(s) are not vmapped.
Defaults to `0`.
**out_axes** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – An integer or a valid prefix tree of the
outputs of `fun` where each node specifies the vmapped axis. If
the value is `None` then the corresponding outputs(s) are not vmapped.
Defaults to `0`.

Returns:
The vectorized function.

Return type:
*Callable*

** Contents
