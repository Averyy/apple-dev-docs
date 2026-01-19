---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/data_types.html
---

# Data Types

**

- [.rst](../_sources/python/data_types.rst)
- **

.pdf

**

# Data Types

 Table of contents 

# Data Types

The default floating point type is `float32` and the default integer type is
`int32`. The table below shows supported values for [Dtype](_autosummary/mlx.core.Dtype.html#mlx.core.Dtype).

| Type | Bytes | Description |
| --- | --- | --- |
| bool_ | 1 | Boolean (True,False) data type |
| uint8 | 1 | 8-bit unsigned integer |
| uint16 | 2 | 16-bit unsigned integer |
| uint32 | 4 | 32-bit unsigned integer |
| uint64 | 8 | 64-bit unsigned integer |
| int8 | 1 | 8-bit signed integer |
| int16 | 2 | 16-bit signed integer |
| int32 | 4 | 32-bit signed integer |
| int64 | 8 | 64-bit signed integer |
| bfloat16 | 2 | 16-bit brain float (e8, m7) |
| float16 | 2 | 16-bit IEEE float (e5, m10) |
| float32 | 4 | 32-bit float |
| float64 | 8 | 64-bit double |
| complex64 | 8 | 64-bit complex float |

Note

Arrays with type `float64` only work with CPU operations. Using
`float64` arrays on the GPU will result in an exception.

Data type are aranged in a hierarchy. See the [DtypeCategory](_autosummary/mlx.core.DtypeCategory.html#mlx.core.DtypeCategory) object
documentation for more information. Use [issubdtype()](_autosummary/mlx.core.issubdtype.html#mlx.core.issubdtype) to determine if one
`dtype` (or category) is a subtype of another category.

| Dtype | An object to hold the type of aarray. |
| --- | --- |
| DtypeCategory(*values) | Type to hold categories ofdtypes. |
| issubdtype(arg1, arg2) | Check if aDtypeorDtypeCategoryis a subtype of another. |
| finfo(*args, **kwargs) | Get information on floating-point types. |
