---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.squeeze.html
---

# mlx.data.Buffer.squeeze

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.squeeze.rst)
- **

.pdf

**

# mlx.data.Buffer.squeeze

 Table of contents 

## Contents

# mlx.data.Buffer.squeeze

**Buffer.squeeze(*self: mlx.data._c.Buffer*, *key: str*, *dim: int | List[int] | None = None*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Squeeze singleton dimensions.
If no dimension is provided squeeze all singleton dimensions.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**dim** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)* of **ints**, **optional*) – The dimensions to squeeze. If
not provided squeeze all the singleton dimensions. (default: None)
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If it is not empty then write the result to this
key instead of overwriting `key`. (default: ‘’)

** Contents
