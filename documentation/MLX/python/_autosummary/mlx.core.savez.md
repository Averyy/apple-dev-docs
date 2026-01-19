---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.savez.html
---

# mlx.core.savez

**

- [.rst](../../_sources/python/_autosummary/mlx.core.savez.rst)
- **

.pdf

**

# mlx.core.savez

 Table of contents 

## Contents

# mlx.core.savez

**savez(*file: file | str | Path*, **args*, ***kwargs*)**
: Save several arrays to a binary file in uncompressed `.npz`
format.
import mlx.core as mx

x = mx.ones((10, 10))
mx.savez("my_path.npz", x=x)

import mlx.nn as nn
from mlx.utils import tree_flatten

model = nn.TransformerEncoder(6, 128, 4)
flat_params = tree_flatten(model.parameters())
mx.savez("model.npz", **dict(flat_params))

Parameters:

**file** (*file**, *[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[Path](https://docs.python.org/3/library/pathlib.html#pathlib.Path)) – Path to file to which the arrays are saved.
***args** (*arrays*) – Arrays to be saved.
****kwargs** (*arrays*) – Arrays to be saved. Each array will be saved
with the associated keyword as the output file name.

** Contents
