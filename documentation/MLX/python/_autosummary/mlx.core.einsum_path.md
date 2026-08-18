---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.einsum_path.html
---

# mlx.core.einsum_path

**

- [.rst](../../_sources/python/_autosummary/mlx.core.einsum_path.rst)
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

# mlx.core.einsum_path

 Table of contents 

## Contents

# mlx.core.einsum_path

**einsum_path(*subscripts: str*, **operands*)**
: Compute the contraction order for the given Einstein summation.

Parameters:

**subscripts** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The Einstein summation convention equation.
***operands** ([array](mlx.core.array.html#mlx.core.array)) – The input arrays.

Returns:
The einsum path and a string containing information about the
chosen path.

Return type:
[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([list](https://docs.python.org/3/library/stdtypes.html#list)([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)([int](https://docs.python.org/3/library/functions.html#int), [int](https://docs.python.org/3/library/functions.html#int))), [str](https://docs.python.org/3/library/stdtypes.html#str))

** Contents
