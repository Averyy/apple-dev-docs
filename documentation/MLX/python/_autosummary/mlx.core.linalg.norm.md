---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.norm.html
---

# mlx.core.linalg.norm

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.norm.rst)
- **

.pdf

**

# mlx.core.linalg.norm

 Table of contents 

## Contents

# mlx.core.linalg.norm

**norm(*a: array*, */*, *ord: None | int | float | str = None*, *axis: None | int | list[int] = None*, *keepdims: bool = False*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Matrix or vector norm.
This function computes vector or  matrix norms depending on the value of
the `ord` and `axis` parameters.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.  If `axis` is `None`, `a` must be 1-D or 2-D,
unless `ord` is `None`. If both `axis` and `ord` are `None`, the
2-norm of `a.flatten` will be returned.
**ord** ([int](https://docs.python.org/3/library/functions.html#int)*, *[float](https://docs.python.org/3/library/functions.html#float)* or *[str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Order of the norm (see table under `Notes`).
If `None`, the 2-norm (or Frobenius norm for matrices) will be computed
along the given `axis`.  Default: `None`.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – If `axis` is an integer, it specifies the
axis of `a` along which to compute the vector norms.  If `axis` is a
2-tuple, it specifies the axes that hold 2-D matrices, and the matrix
norms of these matrices are computed. If axis is `None` then
either a vector norm (when `a` is 1-D) or a matrix norm (when `a` is
2-D) is returned. Default: `None`.
**keepdims** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, the axes which are normed over are
left in the result as dimensions with size one. Default `False`.

Returns:
The output containing the norm(s).

Return type:
[array](mlx.core.array.html#mlx.core.array)

Notes
For values of `ord < 1`, the result is, strictly speaking, not a
mathematical norm, but it may still be useful for various numerical
purposes.
The following norms can be calculated:

ord
norm for matrices
norm for vectors

None
Frobenius norm
2-norm

‘fro’
Frobenius norm
–

‘nuc’
nuclear norm
–

inf
max(sum(abs(x), axis=1))
max(abs(x))

-inf
min(sum(abs(x), axis=1))
min(abs(x))

0
–
sum(x != 0)

1
max(sum(abs(x), axis=0))
as below

-1
min(sum(abs(x), axis=0))
as below

2
2-norm (largest sing. value)
as below

-2
smallest singular value
as below

other
–
sum(abs(x)**ord)**(1./ord)

The Frobenius norm is given by [[1]](#id2):

\(||A||_F = [\sum_{i,j} abs(a_{i,j})^2]^{1/2}\)

The nuclear norm is the sum of the singular values.
Both the Frobenius and nuclear norm orders are only defined for
matrices and raise a `ValueError` when `a.ndim != 2`.
References

[[1](#id1)]
G. H. Golub and C. F. Van Loan, *Matrix Computations*,
Baltimore, MD, Johns Hopkins University Press, 1985, pg. 15

Examples
>>> import mlx.core as mx
>>> from mlx.core import linalg as la
>>> a = mx.arange(9) - 4
>>> a
array([-4, -3, -2, ..., 2, 3, 4], dtype=int32)
>>> b = a.reshape((3,3))
>>> b
array([[-4, -3, -2],
       [-1,  0,  1],
       [ 2,  3,  4]], dtype=int32)
>>> la.norm(a)
array(7.74597, dtype=float32)
>>> la.norm(b)
array(7.74597, dtype=float32)
>>> la.norm(b, 'fro')
array(7.74597, dtype=float32)
>>> la.norm(a, float("inf"))
array(4, dtype=float32)
>>> la.norm(b, float("inf"))
array(9, dtype=float32)
>>> la.norm(a, -float("inf"))
array(0, dtype=float32)
>>> la.norm(b, -float("inf"))
array(2, dtype=float32)
>>> la.norm(a, 1)
array(20, dtype=float32)
>>> la.norm(b, 1)
array(7, dtype=float32)
>>> la.norm(a, -1)
array(0, dtype=float32)
>>> la.norm(b, -1)
array(6, dtype=float32)
>>> la.norm(a, 2)
array(7.74597, dtype=float32)
>>> la.norm(a, 3)
array(5.84804, dtype=float32)
>>> la.norm(a, -3)
array(0, dtype=float32)
>>> c = mx.array([[ 1, 2, 3],
...               [-1, 1, 4]])
>>> la.norm(c, axis=0)
array([1.41421, 2.23607, 5], dtype=float32)
>>> la.norm(c, axis=1)
array([3.74166, 4.24264], dtype=float32)
>>> la.norm(c, ord=1, axis=1)
array([6, 6], dtype=float32)
>>> m = mx.arange(8).reshape(2,2,2)
>>> la.norm(m, axis=(1,2))
array([3.74166, 11.225], dtype=float32)
>>> la.norm(m[0, :, :]), LA.norm(m[1, :, :])
(array(3.74166, dtype=float32), array(11.225, dtype=float32))

** Contents
