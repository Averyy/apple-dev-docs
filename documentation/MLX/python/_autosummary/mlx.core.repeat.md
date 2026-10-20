---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.repeat.html
---

# mlx.core.repeat

**repeat(*array: array*, *repeats: int*, *axis: int | None = None*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.md#mlx.core.array)**
: Repeat an array along a specified axis.

Parameters:

**array** ([array](mlx.core.array.md#mlx.core.array)) – Input array.
**repeats** ([int](https://docs.python.org/3/builtins/functions.html#int)) – The number of repetitions for each element.
**axis** ([int](https://docs.python.org/3/builtins/functions.html#int)*, **optional*) – The axis in which to repeat the array along. If
unspecified it uses the flattened array of the input and repeats
along axis 0.
**stream** ([Stream](stream_class.md#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`.

Returns:
The resulting repeated array.

Return type:
[array](mlx.core.array.md#mlx.core.array)
