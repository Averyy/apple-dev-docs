---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.flatten.html
---

# mlx.core.flatten

**

- [.rst](../../_sources/python/_autosummary/mlx.core.flatten.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.core.flatten

 Table of contents 

## Contents

# mlx.core.flatten

**flatten(*a: array*, */*, *start_axis: int = 0*, *end_axis: int = -1*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Flatten an array.
The axes flattened will be between `start_axis` and `end_axis`,
inclusive. Negative axes are supported. After converting negative axis to
positive, axes outside the valid range will be clamped to a valid value,
`start_axis` to `0` and `end_axis` to `ndim - 1`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**start_axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The first dimension to flatten. Defaults to `0`.
**end_axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The last dimension to flatten. Defaults to `-1`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The flattened array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

Example
>>> a = mx.array([[1, 2], [3, 4]])
>>> mx.flatten(a)
array([1, 2, 3, 4], dtype=int32)
>>>
>>> mx.flatten(a, start_axis=0, end_axis=-1)
array([1, 2, 3, 4], dtype=int32)

** Contents
