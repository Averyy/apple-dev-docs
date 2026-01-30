---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.value_and_grad.html
---

# mlx.core.value_and_grad

**

- [.rst](../../_sources/python/_autosummary/mlx.core.value_and_grad.rst)
- **

.pdf

**

# mlx.core.value_and_grad

 Table of contents 

## Contents

# mlx.core.value_and_grad

**value_and_grad(*fun: Callable[P, R]*, *argnums: int | Sequence[int] | None = None*, *argnames: str | Sequence[str] = []*) → Callable[P, Tuple[R, Any]]**
: Returns a function which computes the value and gradient of `fun`.
The function passed to [value_and_grad()](#mlx.core.value_and_grad) should return either
a scalar loss or a tuple in which the first element is a scalar
loss and the remaining elements can be anything.
import mlx.core as mx

def mse(params, inputs, targets):
    outputs = forward(params, inputs)
    lvalue = (outputs - targets).square().mean()
    return lvalue

# Returns lvalue, dlvalue/dparams
lvalue, grads = mx.value_and_grad(mse)(params, inputs, targets)

def lasso(params, inputs, targets, a=1.0, b=1.0):
    outputs = forward(params, inputs)
    mse = (outputs - targets).square().mean()
    l1 = mx.abs(outputs - targets).mean()

    loss = a*mse + b*l1

    return loss, mse, l1

(loss, mse, l1), grads = mx.value_and_grad(lasso)(params, inputs, targets)

Parameters:

**fun** (*Callable*) – A function which takes a variable number of
[array](mlx.core.array.html#mlx.core.array) or trees of [array](mlx.core.array.html#mlx.core.array) and returns
a scalar output [array](mlx.core.array.html#mlx.core.array) or a tuple the first element
of which should be a scalar [array](mlx.core.array.html#mlx.core.array).
**argnums** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Specify the index (or indices)
of the positional arguments of `fun` to compute the gradient
with respect to. If neither `argnums` nor `argnames` are
provided `argnums` defaults to `0` indicating `fun`’s first
argument.
**argnames** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[str](https://docs.python.org/3/library/stdtypes.html#str)*)**, **optional*) – Specify keyword arguments of
`fun` to compute gradients with respect to. It defaults to [] so
no gradients for keyword arguments by default.

Returns:
A function which returns a tuple where the first element
is the output of fun and the second element is the gradients w.r.t.
the loss.

Return type:
*Callable*

** Contents
