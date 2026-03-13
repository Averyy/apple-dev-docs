---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.export_to_dot.html
---

# mlx.core.export_to_dot

**

- [.rst](../../_sources/python/_autosummary/mlx.core.export_to_dot.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.export_to_dot

 Table of contents 

## Contents

# mlx.core.export_to_dot

**export_to_dot(*file: object*, **args*, ***kwargs*) → [None](https://docs.python.org/3/library/constants.html#None)**
: Export a graph to DOT format for visualization.
A variable number of output arrays can be provided for exporting
The graph exported will recursively include all unevaluated inputs of
the provided outputs.

Parameters:

**file** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The file path to export to.
***args** ([array](mlx.core.array.html#mlx.core.array)) – The output arrays.
****kwargs** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)*[*[str](https://docs.python.org/3/library/stdtypes.html#str)*, *[array](mlx.core.array.html#mlx.core.array)*]*) – Provide some names for arrays in the
graph to make the result easier to parse.

Example
>>> a = mx.array(1) + mx.array(2)
>>> mx.export_to_dot("graph.dot", a)
>>> x = mx.array(1)
>>> y = mx.array(2)
>>> mx.export_to_dot("graph.dot", x + y, x=x, y=y)

** Contents
