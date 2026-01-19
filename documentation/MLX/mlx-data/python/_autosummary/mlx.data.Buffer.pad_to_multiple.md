---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.pad_to_multiple.html
---

# mlx.data.Buffer.pad_to_multiple

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.pad_to_multiple.rst)
- **

.pdf

**

# mlx.data.Buffer.pad_to_multiple

 Table of contents 

## Contents

# mlx.data.Buffer.pad_to_multiple

**Buffer.pad_to_multiple(*self: mlx.data._c.Buffer*, *key: str*, *dim: int*, *pad_multiple: int*, *pad_value: float*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Pad the end of an array such that its size is a multiple of `pad_multiple`.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**dim** ([int](https://docs.python.org/3/library/functions.html#int)) – Which dimension of the array to pad.
**pad_multiple** ([int](https://docs.python.org/3/library/functions.html#int)) – The result should be a multiple of `pad_multiple`.
**pad_value** ([float](https://docs.python.org/3/library/functions.html#float)) – What to pad with.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
