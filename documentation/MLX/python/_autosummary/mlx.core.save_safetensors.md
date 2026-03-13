---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.save_safetensors.html
---

# mlx.core.save_safetensors

**

- [.rst](../../_sources/python/_autosummary/mlx.core.save_safetensors.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.save_safetensors

 Table of contents 

## Contents

# mlx.core.save_safetensors

**save_safetensors(*file: file | str | Path*, *arrays: dict[str, array]*, *metadata: dict[str, str] | None = None*)**
: Save array(s) to a binary file in `.safetensors` format.
See the [Safetensors documentation](https://huggingface.co/docs/safetensors/index) for more
information on the format.

Parameters:

**file** (*file**, *[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) – File in which the array is saved.
**arrays** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)*(*[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[array](mlx.core.array.html#mlx.core.array)*)*) – The dictionary of names to arrays to
be saved.
**metadata** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)*(*[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[str](https://docs.python.org/3/library/stdtypes.html#str)*)**, **optional*) – The dictionary of
metadata to be saved.

** Contents
