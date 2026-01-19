---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.vjp.html
---

# mlx.core.vjp

**

- [.rst](../../_sources/python/_autosummary/mlx.core.vjp.rst)
- **

.pdf

**

# mlx.core.vjp

 Table of contents 

## Contents

# mlx.core.vjp

**vjp(*fun: Callable*, *primals: list[array]*, *cotangents: list[array]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[array](mlx.core.array.html#mlx.core.array)], [list](https://docs.python.org/3/library/stdtypes.html#list)[[array](mlx.core.array.html#mlx.core.array)]]**
: Compute the vector-Jacobian product.
Computes the product of the `cotangents` with the Jacobian of a
function `fun` evaluated at `primals`.

Parameters:

**fun** (*Callable*) – A function which takes a variable number of [array](mlx.core.array.html#mlx.core.array)
and returns a single [array](mlx.core.array.html#mlx.core.array) or list of [array](mlx.core.array.html#mlx.core.array).
**primals** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[array](mlx.core.array.html#mlx.core.array)*)*) – A list of [array](mlx.core.array.html#mlx.core.array) at which to
evaluate the Jacobian.
**cotangents** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[array](mlx.core.array.html#mlx.core.array)*)*) – A list of [array](mlx.core.array.html#mlx.core.array) which are the
“vector” in the vector-Jacobian product. The `cotangents` should be the
same in number, shape, and type as the outputs of `fun`.

Returns:
A tuple with the outputs of
`fun` in the first position and the vector-Jacobian products
in the second position.

Return type:
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([list](https://docs.python.org/3/library/stdtypes.html#list)([array](mlx.core.array.html#mlx.core.array)), [list](https://docs.python.org/3/library/stdtypes.html#list)([array](mlx.core.array.html#mlx.core.array)))

Example
import mlx.core as mx

outs, vjps = mx.vjp(mx.sin, (mx.array(1.0),), (mx.array(1.0),))

** Contents
