---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.save_gguf.html
---

# mlx.core.save_gguf

**

- [.rst](../../_sources/python/_autosummary/mlx.core.save_gguf.rst)
- **

.pdf

**

# mlx.core.save_gguf

 Table of contents 

## Contents

# mlx.core.save_gguf

**save_gguf(*file: file | str | Path*, *arrays: dict[str, array]*, *metadata: dict[str, array | str | list[str]]*)**
: Save array(s) to a binary file in `.gguf` format.
See the [GGUF documentation](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md) for
more information on the format.

Parameters:

**file** (*file**, *[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) – File in which the array is saved.
**arrays** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)*(*[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[array](mlx.core.array.html#mlx.core.array)*)*) – The dictionary of names to arrays to
be saved.
**metadata** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)*(*[str](https://docs.python.org/3/library/stdtypes.html#str)*, **Union**[*[array](mlx.core.array.html#mlx.core.array)*, *[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[str](https://docs.python.org/3/library/stdtypes.html#str)*)**]**)*) – The dictionary
of metadata to be saved. The values can be a scalar or 1D
obj:array, a [str](https://docs.python.org/3/library/stdtypes.html#str), or a [list](https://docs.python.org/3/library/stdtypes.html#list) of [str](https://docs.python.org/3/library/stdtypes.html#str).

** Contents
