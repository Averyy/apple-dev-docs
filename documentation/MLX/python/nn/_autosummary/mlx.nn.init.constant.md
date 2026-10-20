---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.constant.html
---

# mlx.nn.init.constant

**constant(*value: float*, *dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.md#mlx.core.array)], [array](../../_autosummary/mlx.core.array.md#mlx.core.array)]**
: An initializer that returns an array filled with `value`.

Parameters:

**value** ([float](https://docs.python.org/3/builtins/functions.html#float)) – The value to fill the array with.
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.md#mlx.core.Dtype)*, **optional*) – The data type of the array. Default:
`float32`.

Returns:
An initializer that returns an array with the
same shape as the input, filled with `value`.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.md#mlx.core.array)], [array](../../_autosummary/mlx.core.array.md#mlx.core.array)]

Example

  ```
  >>> init_fn = nn.init.constant(0.5)
  >>> init_fn(mx.zeros((2, 2)))
  array([[0.5, 0.5],
         [0.5, 0.5]], dtype=float32)
  ```
