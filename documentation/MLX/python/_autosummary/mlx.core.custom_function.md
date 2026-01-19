---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.custom_function.html
---

# mlx.core.custom_function

**

- [.rst](../../_sources/python/_autosummary/mlx.core.custom_function.rst)
- **

.pdf

**

# mlx.core.custom_function

 Table of contents 

## Contents

# mlx.core.custom_function

**class custom_function(**args*, ***kwargs*)**
: Set up a function for custom gradient and vmap definitions.
This class is meant to be used as a function decorator. Instances are
callables that behave identically to the wrapped function. However, when
a function transformation is used (e.g. computing gradients using
[value_and_grad()](mlx.core.value_and_grad.html#mlx.core.value_and_grad)) then the functions defined via
`custom_function.vjp()`, `custom_function.jvp()` and
`custom_function.vmap()` are used instead of the default transformation.
Note, all custom transformations are optional. Undefined transformations
fall back to the default behaviour.
Example
import mlx.core as mx

@mx.custom_function
def f(x, y):
    return mx.sin(x) * y

@f.vjp
def f_vjp(primals, cotangent, output):
    x, y = primals
    return cotan * mx.cos(x) * y, cotan * mx.sin(x)

@f.jvp
def f_jvp(primals, tangents):
  x, y = primals
  dx, dy = tangents
  return dx * mx.cos(x) * y + dy * mx.sin(x)

@f.vmap
def f_vmap(inputs, axes):
  x, y = inputs
  ax, ay = axes
  if ay != ax and ax is not None:
      y = y.swapaxes(ay, ax)
  return mx.sin(x) * y, (ax or ay)

All `custom_function` instances behave as pure functions. Namely, any
variables captured will be treated as constants and no gradients will be
computed with respect to the captured arrays. For instance:

import mlx.core as mx

def g(x, y):
  @mx.custom_function
  def f(x):
    return x * y

  @f.vjp
  def f_vjp(x, dx, fx):
    # Note that we have only x, dx and fx and nothing with respect to y
    raise ValueError("Abort!")

  return f(x)

x = mx.array(2.0)
y = mx.array(3.0)
print(g(x, y))                     # prints 6.0
print(mx.grad(g)(x, y))            # Raises exception
print(mx.grad(g, argnums=1)(x, y)) # prints 0.0

__init__(*self*, *f: Callable*)

Methods

[__init__](#mlx.core.custom_function.__init__)(self, f)

`jvp`(self, f)
Define a custom jvp for the wrapped function.

`vjp`(self, f)
Define a custom vjp for the wrapped function.

`vmap`(self, f)
Define a custom vectorization transformation for the wrapped function.

** Contents
