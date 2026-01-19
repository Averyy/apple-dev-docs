---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.trace.html
---

# mlx.core.trace

**

- [.rst](../../_sources/python/_autosummary/mlx.core.trace.rst)
- **

.pdf

**

# mlx.core.trace

 Table of contents 

## Contents

# mlx.core.trace

**trace(*a: array*, */*, *offset: int = 0*, *axis1: int = 0*, *axis2: int = 1*, *dtype: Dtype | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the sum along a specified diagonal in the given array.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**offset** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Offset of the diagonal from the main diagonal.
Can be positive or negative. Default: `0`.
**axis1** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The first axis of the 2-D sub-arrays from which
the diagonals should be taken. Default: `0`.
**axis2** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The second axis of the 2-D sub-arrays from which
the diagonals should be taken. Default: `1`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Data type of the output array. If
unspecified the output type is inferred from the input array.

Returns:
Sum of specified diagonal.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
