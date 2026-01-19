---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.pad_to_size.html
---

# mlx.data.Buffer.pad_to_size

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.pad_to_size.rst)
- **

.pdf

**

# mlx.data.Buffer.pad_to_size

 Table of contents 

## Contents

# mlx.data.Buffer.pad_to_size

**Buffer.pad_to_size(*self: mlx.data._c.Buffer*, *key: str*, *dim: int*, *size: int*, *pad_value: float*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Pad the end of an array such that its size is `size`.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**dim** ([int](https://docs.python.org/3/library/functions.html#int)) – Which dimension of the array to pad.
**size** ([int](https://docs.python.org/3/library/functions.html#int)) – The resulting size of the array at dimension `dim`.
**pad_value** ([float](https://docs.python.org/3/library/functions.html#float)) – What to pad with.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
