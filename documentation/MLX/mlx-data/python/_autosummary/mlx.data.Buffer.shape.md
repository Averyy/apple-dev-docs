---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.shape.html
---

# mlx.data.Buffer.shape

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.shape.rst)
- **

.pdf

**

# mlx.data.Buffer.shape

 Table of contents 

## Contents

# mlx.data.Buffer.shape

**Buffer.shape(*self: mlx.data._c.Buffer*, *key: str*, *output_key: str*, *dim: int | None = None*) → mlx.data._c.Buffer**
: Extracts the shape of an array in the sample.
If a dimension is provided then only the size of that dimension is extracted.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to write the output at. It is required on
this operation as it is very unlikely that we will want to replace
the original key.
**dim** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The dimension to report the size for. If not
provided then the full size of the array is returned. (default: None)

** Contents
