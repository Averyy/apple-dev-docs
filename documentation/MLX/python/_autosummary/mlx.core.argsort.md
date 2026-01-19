---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.argsort.html
---

# mlx.core.argsort

**

- [.rst](../../_sources/python/_autosummary/mlx.core.argsort.rst)
- **

.pdf

**

# mlx.core.argsort

 Table of contents 

## Contents

# mlx.core.argsort

**argsort(*a: array*, */*, *axis: None | int = -1*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Returns the indices that sort the array.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or **None**, **optional*) – Optional axis to sort over.
If `None`, this sorts over the flattened array.
If unspecified, it defaults to -1 (sorting over the last axis).

Returns:
The `uint32` array containing indices that sort the input.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
