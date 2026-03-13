---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.issubdtype.html
---

# mlx.core.issubdtype

**

- [.rst](../../_sources/python/_autosummary/mlx.core.issubdtype.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.issubdtype

 Table of contents 

## Contents

# mlx.core.issubdtype

**issubdtype(*arg1: Dtype | DtypeCategory*, *arg2: Dtype | DtypeCategory*) → [bool](https://docs.python.org/3/library/functions.html#bool)**
: Check if a [Dtype](mlx.core.Dtype.html#mlx.core.Dtype) or [DtypeCategory](mlx.core.DtypeCategory.html#mlx.core.DtypeCategory) is a subtype
of another.

Parameters:

**(****Union****[****Dtype** (*arg2*) – First dtype or category.
**DtypeCategory****]** – First dtype or category.
**(****Union****[****Dtype** – Second dtype or category.
**DtypeCategory****]** – Second dtype or category.

Returns:
A boolean indicating if the first input is a subtype of the
second input.

Return type:
[bool](https://docs.python.org/3/library/functions.html#bool)

Example
>>> ints = mx.array([1, 2, 3], dtype=mx.int32)
>>> mx.issubdtype(ints.dtype, mx.integer)
True
>>> mx.issubdtype(ints.dtype, mx.floating)
False

>>> floats = mx.array([1, 2, 3], dtype=mx.float32)
>>> mx.issubdtype(floats.dtype, mx.integer)
False
>>> mx.issubdtype(floats.dtype, mx.floating)
True

Similar types of different sizes are not subdtypes of each other:
>>> mx.issubdtype(mx.float64, mx.float32)
False
>>> mx.issubdtype(mx.float32, mx.float64)
False

but both are subtypes of floating:
>>> mx.issubdtype(mx.float64, mx.floating)
True
>>> mx.issubdtype(mx.float32, mx.floating)
True

For convenience, dtype-like objects are allowed too:
>>> mx.issubdtype(mx.float32, mx.inexact)
True
>>> mx.issubdtype(mx.signedinteger, mx.floating)
False

** Contents
