---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.slice_update.html
---

# mlx.core.slice_update

**

- [.rst](../../_sources/python/_autosummary/mlx.core.slice_update.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.slice_update

 Table of contents 

## Contents

# mlx.core.slice_update

**slice_update(*a: array*, *update: array*, *start_indices: array*, *axes: Sequence[int]*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Update a sub-array of the input array.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array to update
**update** ([array](mlx.core.array.html#mlx.core.array)) – The update array.
**start_indices** ([array](mlx.core.array.html#mlx.core.array)) – The index location to start the slice at.
**axes** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – The axes corresponding to the indices in `start_indices`.

Returns:
The output array with the same shape and type as the input.

Return type:
[array](mlx.core.array.html#mlx.core.array)

Example
>>> a = mx.zeros((3, 3))
>>> mx.slice_update(a, mx.ones((1, 2)), start_indices=mx.array(1, 1), axes=(0, 1))
array([[0, 0, 0],
       [0, 1, 0],
       [0, 1, 0]], dtype=float32)

** Contents
