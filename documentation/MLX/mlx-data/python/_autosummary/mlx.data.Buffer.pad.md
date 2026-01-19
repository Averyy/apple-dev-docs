---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.pad.html
---

# mlx.data.Buffer.pad

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.pad.rst)
- **

.pdf

**

# mlx.data.Buffer.pad

 Table of contents 

## Contents

# mlx.data.Buffer.pad

**Buffer.pad(*self: mlx.data._c.Buffer*, *key: str*, *dim: int*, *lpad: int*, *rpad: int*, *pad_value: float*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Pad the array at `key`.
The following example inserts a space character at the beginning of the
array at key ‘text’.
dset = dset.pad("text", 0, 1, 0, ord(" "))

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**dim** ([int](https://docs.python.org/3/library/functions.html#int)) – Which dimension of the array to pad.
**lpad** ([int](https://docs.python.org/3/library/functions.html#int)) – How many positions to pad on the left (beginning) of the array.
**rpad** ([int](https://docs.python.org/3/library/functions.html#int)) – How many positions to pad on the right (end) of the array.
**pad_value** ([float](https://docs.python.org/3/library/functions.html#float)) – What to pad with.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
