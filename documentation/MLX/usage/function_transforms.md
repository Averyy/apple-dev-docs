---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/usage/function_transforms.html
---

# Function Transforms

**

- [.rst](../_sources/usage/function_transforms.rst)
- **

.pdf

**

# Function Transforms

 Table of contents 

## Contents

# Function Transforms

MLX uses composable function transformations for automatic differentiation,
vectorization, and compute graph optimizations. To see the complete list of
function transformations check-out the [API documentation](../python/transforms.html#transforms).

The key idea behind composable function transformations is that every
transformation returns a function which can be further transformed.

Here is a simple example:

```
>>> dfdx = mx.grad(mx.sin)
>>> dfdx(mx.array(mx.pi))
array(-1, dtype=float32)
>>> mx.cos(mx.array(mx.pi))
array(-1, dtype=float32)
```

The output of [grad()](../python/_autosummary/mlx.core.grad.html#mlx.core.grad) on [sin()](../python/_autosummary/mlx.core.sin.html#mlx.core.sin) is simply another function. In this
case it is the gradient of the sine function which is exactly the cosine
function. To get the second derivative you can do:

```
>>> d2fdx2 = mx.grad(mx.grad(mx.sin))
>>> d2fdx2(mx.array(mx.pi / 2))
array(-1, dtype=float32)
>>> mx.sin(mx.array(mx.pi / 2))
array(1, dtype=float32)
```

Using [grad()](../python/_autosummary/mlx.core.grad.html#mlx.core.grad) on the output of [grad()](../python/_autosummary/mlx.core.grad.html#mlx.core.grad) is always ok. You keep
getting higher order derivatives.

Any of the MLX function transformations can be composed in any order to any
depth. See the following sections for more information on [automatic
differentiation](#auto-diff) and [automatic vectorization](#vmap).
For more information on [compile()](../python/_autosummary/mlx.core.compile.html#mlx.core.compile) see the [compile documentation](compile.html#compile).

## Automatic Differentiation

Automatic differentiation in MLX works on functions rather than on implicit
graphs.

Note

If you are coming to MLX from PyTorch, you no longer need functions like
`backward`, `zero_grad`, and `detach`, or properties like
`requires_grad`.

The most basic example is taking the gradient of a scalar-valued function as we
saw above. You can use the [grad()](../python/_autosummary/mlx.core.grad.html#mlx.core.grad) and [value_and_grad()](../python/_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad) function to
compute gradients of more complex functions. By default these functions compute
the gradient with respect to the first argument:

```
def loss_fn(w, x, y):
   return mx.mean(mx.square(w * x - y))

w = mx.array(1.0)
x = mx.array([0.5, -0.5])
y = mx.array([1.5, -1.5])

# Computes the gradient of loss_fn with respect to w:
grad_fn = mx.grad(loss_fn)
dloss_dw = grad_fn(w, x, y)
# Prints array(-1, dtype=float32)
print(dloss_dw)

# To get the gradient with respect to x we can do:
grad_fn = mx.grad(loss_fn, argnums=1)
dloss_dx = grad_fn(w, x, y)
# Prints array([-1, 1], dtype=float32)
print(dloss_dx)
```

One way to get the loss and gradient is to call `loss_fn` followed by
`grad_fn`, but this can result in a lot of redundant work. Instead, you
should use [value_and_grad()](../python/_autosummary/mlx.core.value_and_grad.html#mlx.core.value_and_grad). Continuing the above example:

```
# Computes the gradient of loss_fn with respect to w:
loss_and_grad_fn = mx.value_and_grad(loss_fn)
loss, dloss_dw = loss_and_grad_fn(w, x, y)

# Prints array(1, dtype=float32)
print(loss)

# Prints array(-1, dtype=float32)
print(dloss_dw)
```

You can also take the gradient with respect to arbitrarily nested Python
containers of arrays (specifically any of [list](https://docs.python.org/3/library/stdtypes.html#list), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple), or
[dict](https://docs.python.org/3/library/stdtypes.html#dict)).

Suppose we wanted a weight and a bias parameter in the above example. A nice
way to do that is the following:

```
def loss_fn(params, x, y):
   w, b = params["weight"], params["bias"]
   h = w * x + b
   return mx.mean(mx.square(h - y))

params = {"weight": mx.array(1.0), "bias": mx.array(0.0)}
x = mx.array([0.5, -0.5])
y = mx.array([1.5, -1.5])

# Computes the gradient of loss_fn with respect to both the
# weight and bias:
grad_fn = mx.grad(loss_fn)
grads = grad_fn(params, x, y)

# Prints
# {'weight': array(-1, dtype=float32), 'bias': array(0, dtype=float32)}
print(grads)
```

Notice the tree structure of the parameters is preserved in the gradients.

In some cases you may want to stop gradients from propagating through a
part of the function. You can use the [stop_gradient()](../python/_autosummary/mlx.core.stop_gradient.html#mlx.core.stop_gradient) for that.

## Automatic Vectorization

Use [vmap()](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap) to automate vectorizing complex functions. Here we’ll go
through a basic and contrived example for the sake of clarity, but [vmap()](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap)
can be quite powerful for more complex functions which are difficult to optimize
by hand.

Warning

Some operations are not yet supported with [vmap()](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap). If you encounter an error
like: `ValueError: Primitive's vmap not implemented.` file an [issue](https://github.com/ml-explore/mlx/issues) and include your function.
We will prioritize including it.

A naive way to add the elements from two sets of vectors is with a loop:

```
xs = mx.random.uniform(shape=(4096, 100))
ys = mx.random.uniform(shape=(100, 4096))

def naive_add(xs, ys):
    return [xs[i] + ys[:, i] for i in range(xs.shape[0])]
```

Instead you can use [vmap()](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap) to automatically vectorize the addition:

```
# Vectorize over the second dimension of x and the
# first dimension of y
vmap_add = mx.vmap(lambda x, y: x + y, in_axes=(0, 1))
```

The `in_axes` parameter can be used to specify which dimensions of the
corresponding input to vectorize over. Similarly, use `out_axes` to specify
where the vectorized axes should be in the outputs.

Let’s time these two different versions:

```
import timeit

print(timeit.timeit(lambda: mx.eval(naive_add(xs, ys)), number=100))
print(timeit.timeit(lambda: mx.eval(vmap_add(xs, ys)), number=100))
```

On an M1 Max the naive version takes in total `5.639` seconds whereas the
vectorized version takes only `0.024` seconds, more than 200 times faster.

Of course, this operation is quite contrived. A better approach is to simply do
`xs + ys.T`, but for more complex functions [vmap()](../python/_autosummary/mlx.core.vmap.html#mlx.core.vmap) can be quite handy.

** Contents
