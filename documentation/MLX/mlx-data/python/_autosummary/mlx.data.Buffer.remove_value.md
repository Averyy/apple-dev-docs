---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.remove_value.html
---

# mlx.data.Buffer.remove_value

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.remove_value.rst)
- **

.pdf

**

# mlx.data.Buffer.remove_value

 Table of contents 

## Contents

# mlx.data.Buffer.remove_value

**Buffer.remove_value(*self: mlx.data._c.Buffer*, *key: str*, *size_key: str*, *dim: int*, *value: float*, *pad: float = 0*) → mlx.data._c.Buffer**
: Remove instances of a certain value from an array and shift the whole
array to the left.
The size of the array remains unchanged and the end is replaced with
pad values. Moreover, the length array is updated to match the number
of values present.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**size_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array with the valid
sizes of the array at `key`.
**dim** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimension the sizes correspond to and the one to be
filtered.
**value** (*double*) – The value to look for and remove.
**pad** (*double*) – The pad value to use.

** Contents
