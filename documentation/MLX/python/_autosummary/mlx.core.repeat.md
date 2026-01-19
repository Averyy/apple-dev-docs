---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.repeat.html
---

# mlx.core.repeat

**

- [.rst](../../_sources/python/_autosummary/mlx.core.repeat.rst)
- **

.pdf

**

# mlx.core.repeat

 Table of contents 

## Contents

# mlx.core.repeat

**repeat(*array: array*, *repeats: int*, *axis: int | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Repeat an array along a specified axis.

Parameters:

**array** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**repeats** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of repetitions for each element.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The axis in which to repeat the array along. If
unspecified it uses the flattened array of the input and repeats
along axis 0.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`.

Returns:
The resulting repeated array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
