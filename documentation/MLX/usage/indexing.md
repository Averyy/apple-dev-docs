---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/usage/indexing.html
---

# Indexing Arrays

**

- [.rst](../_sources/usage/indexing.rst)
- **

.pdf

**

**
**
**

**

# Indexing Arrays

 Table of contents 

## Contents

# Indexing Arrays

For the most part, indexing an MLX [array](../python/_autosummary/mlx.core.array.html#mlx.core.array) works the same as indexing a
NumPy [numpy.ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray). See the [NumPy documentation](https://numpy.org/doc/stable/user/basics.indexing.md) for more details on
how that works.

For example, you can use regular integers and slices ([slice](../python/_autosummary/mlx.core.slice.html#mlx.core.slice)) to index arrays:

```
>>> arr = mx.arange(10)
>>> arr[3]
array(3, dtype=int32)
>>> arr[-2]  # negative indexing works
array(8, dtype=int32)
>>> arr[2:8:2] # start, stop, stride
array([2, 4, 6], dtype=int32)
```

For multi-dimensional arrays, the `...` or [Ellipsis](https://docs.python.org/3/library/constants.html#Ellipsis) syntax works as in NumPy:

```
>>> arr = mx.arange(8).reshape(2, 2, 2)
>>> arr[:, :, 0]
array(3, dtype=int32)
array([[0, 2],
       [4, 6]], dtype=int32
>>> arr[..., 0]
array([[0, 2],
       [4, 6]], dtype=int32
```

You can index with `None` to create a new axis:

```
>>> arr = mx.arange(8)
>>> arr.shape
[8]
>>> arr[None].shape
[1, 8]
```

You can also use an [array](../python/_autosummary/mlx.core.array.html#mlx.core.array) to index another [array](../python/_autosummary/mlx.core.array.html#mlx.core.array):

```
>>> arr = mx.arange(10)
>>> idx = mx.array([5, 7])
>>> arr[idx]
array([5, 7], dtype=int32)
```

Mixing and matching integers, [slice](../python/_autosummary/mlx.core.slice.html#mlx.core.slice), `...`, and [array](../python/_autosummary/mlx.core.array.html#mlx.core.array) indices
works just as in NumPy.

Other functions which may be useful for indexing arrays are [take()](../python/_autosummary/mlx.core.take.html#mlx.core.take) and
[take_along_axis()](../python/_autosummary/mlx.core.take_along_axis.html#mlx.core.take_along_axis).

## Differences from NumPy

Note

MLX indexing is different from NumPy indexing in two important ways:

- Indexing does not perform bounds checking. Indexing out of bounds is
undefined behavior.
- Boolean mask based indexing is supported for assignment only (see
[Boolean Mask Assignment](#boolean-mask-assignment)).

The reason for the lack of bounds checking is that exceptions cannot propagate
from the GPU. Performing bounds checking for array indices before launching the
kernel would be extremely inefficient.

Indexing with boolean masks is something that MLX may support in the future. In
general, MLX has limited support for operations for which output
*shapes* are dependent on input *data*. Other examples of these types of
operations which MLX does not yet support include [numpy.nonzero()](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero) and the
single input version of [numpy.where()](https://numpy.org/doc/stable/reference/generated/numpy.where.html#numpy.where).

## In Place Updates

In place updates to indexed arrays are possible in MLX. For example:

```
>>> a = mx.array([1, 2, 3])
>>> a[2] = 0
>>> a
array([1, 2, 0], dtype=int32)
```

Just as in NumPy, in place updates will be reflected in all references to the
same array:

```
>>> a = mx.array([1, 2, 3])
>>> b = a
>>> b[2] = 0
>>> b
array([1, 2, 0], dtype=int32)
>>> a
array([1, 2, 0], dtype=int32)
```

Note that unlike NumPy, slicing an array creates a copy, not a view. So
mutating it does not mutate the original array:

```
>>> a = mx.array([1, 2, 3])
>>> b = a[:]
>>> b[2] = 0
>>> b
array([1, 2, 0], dtype=int32)
>>> a
array([1, 2, 3], dtype=int32)
```

Also unlike NumPy, updates to the same location are nondeterministic:

```
>>> a = mx.array([1, 2, 3])
>>> a[[0, 0]] = mx.array([4, 5])
```

The first element of `a` could be `4` or `5`.

Transformations of functions which use in-place updates are allowed and work as
expected. For example:

```
def fun(x, idx):
    x[idx] = 2.0
    return x.sum()

dfdx = mx.grad(fun)(mx.array([1.0, 2.0, 3.0]), mx.array([1]))
print(dfdx)  # Prints: array([1, 0, 1], dtype=float32)
```

In the above `dfdx` will have the correct gradient, namely zeros at `idx`
and ones elsewhere.

## Boolean Mask Assignment

MLX supports boolean indices using NumPy syntax. A mask must already be
a `bool_` MLX [array](../python/_autosummary/mlx.core.array.html#mlx.core.array) or a NumPy `ndarray` with `dtype=bool`.
Other index types are routed through the standard scatter code.

```
>>> a = mx.array([1.0, 2.0, 3.0])
>>> mask = mx.array([True, False, True])
>>> updates = mx.array([5.0, 6.0])
>>> a[mask] = updates
>>> a
array([5.0, 2.0, 6.0], dtype=float32)
```

Scalar assignments broadcast to every `True` entry in `mask`. For non-scalar
assignments, `updates` must provide at least as many elements as there are
`True` entries in `mask`.

```
>>> a = mx.zeros((2, 3))
>>> mask = mx.array([[True, False, True],
                     [False, False, True]])
>>> a[mask] = 1.0
>>> a
array([[1.0, 0.0, 1.0],
       [0.0, 0.0, 1.0]], dtype=float32)
```

Boolean masks follow NumPy semantics:

- The mask shape must match the shape of the axes it indexes exactly. The only
exception is a scalar boolean mask, which broadcasts to the full array.
- Any axes not covered by the mask are taken in full.

```
>>> a = mx.arange(1000).reshape(10, 10, 10)
>>> a[mx.random.normal((10, 10)) > 0.0] = 0  # valid: mask covers axes 0 and 1
```

The mask of shape `(10, 10)` applies to the first two axes, so `a[mask]`
selects the 1-D slices `a[i, j, :]` where `mask[i, j]` is `True`.
Shapes such as `(1, 10, 10)` or `(10, 10, 1)` do not match the indexed
axes and therefore raise errors.

** Contents
