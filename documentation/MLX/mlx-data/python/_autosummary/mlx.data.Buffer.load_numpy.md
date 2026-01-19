---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.load_numpy.html
---

# mlx.data.Buffer.load_numpy

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.load_numpy.rst)
- **

.pdf

**

# mlx.data.Buffer.load_numpy

 Table of contents 

## Contents

# mlx.data.Buffer.load_numpy

**Buffer.load_numpy(*self: mlx.data._c.Buffer*, *key: str*, *prefix: str = ''*, *from_memory: bool = False*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Load an array from a .npy file.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use when loading the files. (default: ‘’)
**from_memory** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true assume the file contents are in the array
instead of the file name. (default: False)
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
