---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.slice.html
---

# mlx.core.slice

**

- [.rst](../../_sources/python/_autosummary/mlx.core.slice.rst)
- **

.pdf

**

# mlx.core.slice

 Table of contents 

## Contents

# mlx.core.slice

**slice(*a: array*, *start_indices: array*, *axes: Sequence[int]*, *slice_size: Sequence[int]*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Extract a sub-array from the input array.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**start_indices** ([array](mlx.core.array.html#mlx.core.array)) – The index location to start the slice at.
**axes** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – The axes corresponding to the indices in `start_indices`.
**slice_size** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – The size of the slice.

Returns:
The sliced output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

Example
>>> a = mx.array([[1, 2, 3], [4, 5, 6]])
>>> mx.slice(a, start_indices=mx.array(1), axes=(0,), slice_size=(1, 2))
array([[4, 5]], dtype=int32)
>>>
>>> mx.slice(a, start_indices=mx.array(1), axes=(1,), slice_size=(2, 1))
array([[2],
       [5]], dtype=int32)

** Contents
