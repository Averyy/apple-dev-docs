---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.rename_key.html
---

# mlx.data.Buffer.rename_key

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.rename_key.rst)
- **

.pdf

**

# mlx.data.Buffer.rename_key

 Table of contents 

## Contents

# mlx.data.Buffer.rename_key

**Buffer.rename_key(*self: mlx.data._c.Buffer*, *key: str*, *output_key: str*) → mlx.data._c.Buffer**
: Rename a sample key.
This is equivalent to
def rename_key(s):
  s[output_key] = s[key]
  del s[key]
  return s

dset = dset.sample_transform(rename_key)

but more efficient and with better error reporting.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to rename.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The value to set `key` to.

** Contents
