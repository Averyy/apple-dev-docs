---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.isdtype.html
---

# mlx.core.isdtype

**

- [.rst](../../_sources/python/_autosummary/mlx.core.isdtype.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.isdtype

 Table of contents 

## Contents

# mlx.core.isdtype

**isdtype(*dtype: Dtype*, *kind: Dtype | str | tuple[Dtype | str, ...]*) → [bool](https://docs.python.org/3/library/functions.html#bool)**
: Test whether a dtype belongs to one or more data type kinds.

Parameters:

**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)) – The dtype to test.
**kind** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, *[str](https://docs.python.org/3/library/stdtypes.html#str)*, or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)) – A dtype, a kind string, or a tuple
of dtypes and kind strings. Supported kind strings are
`"bool"`, `"signed integer"`, `"unsigned integer"`,
`"integral"`, `"real floating"`, `"complex floating"`,
and `"numeric"`.

Returns:
`True` if `dtype` matches any of the given kinds.

Return type:
[bool](https://docs.python.org/3/library/functions.html#bool)

** Contents
