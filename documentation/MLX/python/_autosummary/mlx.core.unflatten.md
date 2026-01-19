---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.unflatten.html
---

# mlx.core.unflatten

**

- [.rst](../../_sources/python/_autosummary/mlx.core.unflatten.rst)
- **

.pdf

**

# mlx.core.unflatten

 Table of contents 

## Contents

# mlx.core.unflatten

**unflatten(*a: array*, */*, *axis: int*, *shape: Sequence[int]*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Unflatten an axis of an array to a shape.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)) – The axis to unflatten.
**shape** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – The shape to unflatten to. At most one
entry can be `-1` in which case the corresponding size will be
inferred.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The unflattened array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

Example
>>> a = mx.array([1, 2, 3, 4])
>>> mx.unflatten(a, 0, (2, -1))
array([[1, 2], [3, 4]], dtype=int32)

** Contents
