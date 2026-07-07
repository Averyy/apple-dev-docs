---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.from_dlpack.html
---

# mlx.core.from_dlpack

**

- [.rst](../../_sources/python/_autosummary/mlx.core.from_dlpack.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.from_dlpack

 Table of contents 

## Contents

# mlx.core.from_dlpack

**from_dlpack(*x: DLPackCompatible*, */*, ***, *copy: bool | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Create an array from an object that supports DLPack.

Parameters:

**x** – Input object implementing `__dlpack__` and
`__dlpack_device__`.
**copy** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether to copy the input. If `True`,
always copy. If `False`, never copy. If `None`, share memory
when possible and copy otherwise. Zero-copy imports preserve the
DLPack strides.

Returns:
An array containing the input data.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
