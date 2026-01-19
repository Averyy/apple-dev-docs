---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.full.html
---

# mlx.core.full

**

- [.rst](../../_sources/python/_autosummary/mlx.core.full.rst)
- **

.pdf

**

# mlx.core.full

 Table of contents 

## Contents

# mlx.core.full

**full(*shape: int | Sequence[int]*, *vals: scalar | array*, *dtype: Dtype | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Construct an array with the given value.
Constructs an array of size `shape` filled with `vals`. If `vals`
is an [array](mlx.core.array.html#mlx.core.array) it must be broadcastable to the given `shape`.

Parameters:

**shape** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – The shape of the output array.
**vals** ([float](https://docs.python.org/3/library/functions.html#float)* or *[int](https://docs.python.org/3/library/functions.html#int)* or *[array](mlx.core.array.html#mlx.core.array)) – Values to fill the array with.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Data type of the output array. If
unspecified the output type is inferred from `vals`.

Returns:
The output array with the specified shape and values.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
