---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.jvp.html
---

# mlx.core.jvp

**

- [.rst](../../_sources/python/_autosummary/mlx.core.jvp.rst)
- **

.pdf

**

# mlx.core.jvp

 Table of contents 

## Contents

# mlx.core.jvp

**jvp(*fun: Callable*, *primals: list[array]*, *tangents: list[array]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[[list](https://docs.python.org/3/library/stdtypes.html#list)[[array](mlx.core.array.html#mlx.core.array)], [list](https://docs.python.org/3/library/stdtypes.html#list)[[array](mlx.core.array.html#mlx.core.array)]]**
: Compute the Jacobian-vector product.
This computes the product of the Jacobian of a function `fun` evaluated
at `primals` with the `tangents`.

Parameters:

**fun** (*Callable*) – A function which takes a variable number of [array](mlx.core.array.html#mlx.core.array)
and returns a single [array](mlx.core.array.html#mlx.core.array) or list of [array](mlx.core.array.html#mlx.core.array).
**primals** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[array](mlx.core.array.html#mlx.core.array)*)*) – A list of [array](mlx.core.array.html#mlx.core.array) at which to
evaluate the Jacobian.
**tangents** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[array](mlx.core.array.html#mlx.core.array)*)*) – A list of [array](mlx.core.array.html#mlx.core.array) which are the
“vector” in the Jacobian-vector product. The `tangents` should be the
same in number, shape, and type as the inputs of `fun` (i.e. the `primals`).

Returns:
A tuple with the outputs of
`fun` in the first position and the Jacobian-vector products
in the second position.

Return type:
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([list](https://docs.python.org/3/library/stdtypes.html#list)([array](mlx.core.array.html#mlx.core.array)), [list](https://docs.python.org/3/library/stdtypes.html#list)([array](mlx.core.array.html#mlx.core.array)))

Example
import mlx.core as mx

outs, jvps = mx.jvp(mx.sin, (mx.array(1.0),), (mx.array(1.0),))

** Contents
