---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.cumsum.html
---

# mlx.core.cumsum

**

- [.rst](../../_sources/python/_autosummary/mlx.core.cumsum.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.cumsum

 Table of contents 

## Contents

# mlx.core.cumsum

**cumsum(*a: array*, */*, *axis: int | None = None*, ***, *reverse: bool = False*, *inclusive: bool = True*, *dtype: Dtype | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the cumulative sum of the elements along the given axis.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Optional axis to compute the cumulative sum
over. If unspecified the cumulative sum of the flattened array is
returned.
**reverse** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Perform the cumulative sum in reverse.
**inclusive** ([bool](https://docs.python.org/3/library/functions.html#bool)) – The i-th element of the output includes the i-th
element of the input.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Cast the input to this type before summing.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
