---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.partition.html
---

# mlx.core.partition

**

- [.rst](../../_sources/python/_autosummary/mlx.core.partition.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.partition

 Table of contents 

## Contents

# mlx.core.partition

**partition(*a: array*, */*, *kth: int*, *axis: None | int = -1*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Returns a partitioned copy of the array such that the smaller `kth`
elements are first.
The ordering of the elements in partitions is undefined.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**kth** ([int](https://docs.python.org/3/library/functions.html#int)) – Element at the `kth` index will be in its sorted
position in the output. All elements before the kth index will
be less or equal to the `kth` element and all elements after
will be greater or equal to the `kth` element in the output.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or **None**, **optional*) – Optional axis to partition over.
If `None`, this partitions over the flattened array.
If unspecified, it defaults to `-1`.

Returns:
The partitioned array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
