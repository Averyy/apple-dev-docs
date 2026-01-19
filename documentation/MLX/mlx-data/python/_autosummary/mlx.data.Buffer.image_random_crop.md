---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.image_random_crop.html
---

# mlx.data.Buffer.image_random_crop

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.image_random_crop.rst)
- **

.pdf

**

# mlx.data.Buffer.image_random_crop

 Table of contents 

## Contents

# mlx.data.Buffer.image_random_crop

**Buffer.image_random_crop(*self: mlx.data._c.Buffer*, *key: str*, *w: int*, *h: int*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Extract a random crop of the requested size.
This operation will fail if the image is smaller than the requested
width and height.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**w** ([int](https://docs.python.org/3/library/functions.html#int)) – The width of the result.
**h** ([int](https://docs.python.org/3/library/functions.html#int)) – The height of the result.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If it is not empty then write the result to this
key instead of overwriting `key`. (default: ‘’)

** Contents
