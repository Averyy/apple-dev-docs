---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.load.html
---

# mlx.core.load

**

- [.rst](../../_sources/python/_autosummary/mlx.core.load.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.load

 Table of contents 

## Contents

# mlx.core.load

**load(*file: file | str | Path*, */*, *format: str | None = None*, *return_metadata: bool = False*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array) | [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [array](mlx.core.array.html#mlx.core.array)] | Tuple[[dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), [array](mlx.core.array.html#mlx.core.array)], [dict](https://docs.python.org/3/library/stdtypes.html#dict)[[str](https://docs.python.org/3/library/stdtypes.html#str), Any]]**
: Load array(s) from a binary file.
The supported formats are `.npy`, `.npz`, `.safetensors`, and
`.gguf`.

Parameters:

**file** (*file**, *[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) – File in which the array is saved.
**format** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – Format of the file. If `None`, the
format is inferred from the file extension. Supported formats:
`npy`, `npz`, and `safetensors`. Default: `None`.
**return_metadata** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Load the metadata for formats
which support matadata. The metadata will be returned as an
additional dictionary. Default: `False`.

Returns:
A single array if loading from a `.npy` file or a dict
mapping names to arrays if loading from a `.npz` or
`.safetensors` file. If `return_metadata` is `True` a
tuple `(arrays, metadata)` will be returned where the second
element is a dictionary containing the metadata.

Return type:
[array](mlx.core.array.html#mlx.core.array), [dict](https://docs.python.org/3/library/stdtypes.html#dict), or [tuple](https://docs.python.org/3/library/stdtypes.html#tuple)

Warning
When loading unsupported quantization formats from GGUF, tensors
will automatically cast to `mx.float16`

** Contents
