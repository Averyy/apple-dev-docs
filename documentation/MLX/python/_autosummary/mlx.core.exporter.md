---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.exporter.html
---

# mlx.core.exporter

**

- [.rst](../../_sources/python/_autosummary/mlx.core.exporter.rst)
- **

.pdf

**

# mlx.core.exporter

 Table of contents 

## Contents

# mlx.core.exporter

**exporter(*file: str*, *fun: Callable*, ***, *shapeless: bool = False*) → mlx.core.FunctionExporter**
: Make a callable object to export multiple traces of a function to a file.

Warning
This is part of an experimental API which is likely to
change in future versions of MLX. Functions exported with older
versions of MLX may not be compatible with future versions.

Parameters:

**file** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – File path to export the function to.
**shapeless** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether or not the function allows
inputs with variable shapes. Default: `False`.

Example
def fun(*args):
    return sum(args)

with mx.exporter("fun.mlxfn", fun) as exporter:
    exporter(mx.array(1))
    exporter(mx.array(1), mx.array(2))
    exporter(mx.array(1), mx.array(2), mx.array(3))

** Contents
