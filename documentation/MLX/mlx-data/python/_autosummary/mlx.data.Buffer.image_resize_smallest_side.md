---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.image_resize_smallest_side.html
---

# mlx.data.Buffer.image_resize_smallest_side

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.image_resize_smallest_side.rst)
- **

.pdf

**

# mlx.data.Buffer.image_resize_smallest_side

 Table of contents 

## Contents

# mlx.data.Buffer.image_resize_smallest_side

**Buffer.image_resize_smallest_side(*self: mlx.data._c.Buffer*, *key: str*, *size: int*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Resize the image such that its smallest side is `size`.
This operation combined with a center crop or a random area crop is the
backbone of many image pipelines.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**size** ([int](https://docs.python.org/3/library/functions.html#int)) – The size of the smallest side of the result.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If it is not empty then write the result to this
key instead of overwriting `key`. (default: ‘’)

** Contents
