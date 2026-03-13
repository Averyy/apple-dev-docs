---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.cummin.html
---

# mlx.core.cummin

**

- [.rst](../../_sources/python/_autosummary/mlx.core.cummin.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.cummin

 Table of contents 

## Contents

# mlx.core.cummin

**cummin(*a: array*, */*, *axis: int | None = None*, ***, *reverse: bool = False*, *inclusive: bool = True*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the cumulative minimum of the elements along the given axis.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Optional axis to compute the cumulative minimum
over. If unspecified the cumulative minimum of the flattened array is
returned.
**reverse** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Perform the cumulative minimum in reverse.
**inclusive** ([bool](https://docs.python.org/3/library/functions.html#bool)) – The i-th element of the output includes the i-th
element of the input.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
