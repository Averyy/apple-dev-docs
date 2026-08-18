---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.argpartition.html
---

# mlx.core.argpartition

**

- [.rst](../../_sources/python/_autosummary/mlx.core.argpartition.rst)
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

# mlx.core.argpartition

 Table of contents 

## Contents

# mlx.core.argpartition

**argpartition(*a: array*, */*, *kth: int*, *axis: None | int = -1*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Returns the indices that partition the array.
The ordering of the elements within a partition in given by the indices
is undefined.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**kth** ([int](https://docs.python.org/3/library/functions.html#int)) – Element index at the `kth` position in the output will
give the sorted position. All indices before the `kth` position
will be of elements less or equal to the element at the `kth`
index and all indices after will be of elements greater or equal
to the element at the `kth` index.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or **None**, **optional*) – Optional axis to partition over.
If `None`, this partitions over the flattened array.
If unspecified, it defaults to `-1`.

Returns:
The `uint32` array containing indices that partition the input.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
