---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.cummax.html
---

# mlx.core.cummax

**

- [.rst](../../_sources/python/_autosummary/mlx.core.cummax.rst)
- **

.pdf

**

# mlx.core.cummax

 Table of contents 

## Contents

# mlx.core.cummax

**cummax(*a: array*, */*, *axis: int | None = None*, ***, *reverse: bool = False*, *inclusive: bool = True*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the cumulative maximum of the elements along the given axis.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Optional axis to compute the cumulative maximum
over. If unspecified the cumulative maximum of the flattened array is
returned.
**reverse** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Perform the cumulative maximum in reverse.
**inclusive** ([bool](https://docs.python.org/3/library/functions.html#bool)) – The i-th element of the output includes the i-th
element of the input.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
