---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.load_file.html
---

# mlx.data.Buffer.load_file

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.load_file.rst)
- **

.pdf

**

# mlx.data.Buffer.load_file

 Table of contents 

## Contents

# mlx.data.Buffer.load_file

**Buffer.load_file(*self: mlx.data._c.Buffer*, *key: str*, *prefix: os.PathLike = ''*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Load the contents of a file.
It opens the file pointed by `key` in binary mode and reads its contents.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use when loading the files.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
