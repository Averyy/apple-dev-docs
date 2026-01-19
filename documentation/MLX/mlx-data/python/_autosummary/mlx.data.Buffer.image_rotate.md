---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.image_rotate.html
---

# mlx.data.Buffer.image_rotate

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.image_rotate.rst)
- **

.pdf

**

# mlx.data.Buffer.image_rotate

 Table of contents 

## Contents

# mlx.data.Buffer.image_rotate

**Buffer.image_rotate(*self: mlx.data._c.Buffer*, *key: str*, *angle: float*, *crop: bool = False*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Rotate an image around its center point.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**angle** ([float](https://docs.python.org/3/library/functions.html#float)) – The angle of rotation in degrees.
**crop** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether to crop the result to the original image’s size.
(default: False)
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If it is not empty then write the result to this
key instead of overwriting `key`. (default: ‘’)

** Contents
