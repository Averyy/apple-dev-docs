---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.import_function.html
---

# mlx.core.import_function

**

- [.rst](../../_sources/python/_autosummary/mlx.core.import_function.rst)
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

# mlx.core.import_function

 Table of contents 

## Contents

# mlx.core.import_function

**import_function(*file: str*, *return_metadata: bool = False*) → Callable | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)[Callable, [str](https://docs.python.org/3/library/stdtypes.html#str)]**
: Import a function from a file.
The imported function can be called either with `*args` and
`**kwargs` or with a tuple of arrays and/or dictionary of string
keys with array values. Imported functions always return a tuple of
arrays.

Warning
This is part of an experimental API which is likely to
change in future versions of MLX. Functions exported with older
versions of MLX may not be compatible with future versions.

Parameters:

**file** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The file path to import the function from.
**return_metadata** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True` also return the
metadata string saved with the function. Default: `False`.

Returns:
The imported function. If `return_metadata` is `True` a
tuple of the imported function and the metadata string is
returned instead.

Return type:
*Callable* or [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)

Example
>>> fn = mx.import_function("function.mlxfn")
>>> out = fn(a, b, x=x, y=y)[0]
>>>
>>> out = fn((a, b), {"x": x, "y": y})[0]

** Contents
