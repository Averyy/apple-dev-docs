---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.load_image.html
---

# mlx.data.Buffer.load_image

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.load_image.rst)
- **

.pdf

**

# mlx.data.Buffer.load_image

 Table of contents 

## Contents

# mlx.data.Buffer.load_image

**Buffer.load_image(*self: mlx.data._c.Buffer*, *key: str*, *prefix: str = ''*, *info: bool = False*, *format: str = 'RGB'*, *from_memory: bool = False*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Load an image file.
Loads an image from an image file on disk or in memory. It can also
load the image info instead.

Note
The format is ignored for now.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use when loading the files. (default: ‘’)
**info** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True load the image width and height instead of the
image data. (default: False)
**format** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Currently ignored but in the future it should decide
whether to load the alpha channel or map the channels to some other
space (e.g. YCbCr) (default: RGB).
**from_memory** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true assume the file contents are in the array
instead of the file name. (default: False)
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
