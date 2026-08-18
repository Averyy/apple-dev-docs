---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.arange.html
---

# mlx.core.arange

**

- [.rst](../../_sources/python/_autosummary/mlx.core.arange.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.core.arange

 Table of contents 

## Contents

# mlx.core.arange

**arange(*start: int | float*, *stop: None | int | float*, *step: None | int | float*, *dtype: Dtype | None = None*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Overloaded function.

`arange(start : int | float, stop : None | int | float, step : None | int | float, dtype: Dtype | None = None, *, stream: StreamOrDevice = None) -> array`

Generates ranges of numbers.
Generate numbers in the half-open interval `[start, stop)` in
increments of `step`.

Args:start (float or int, optional): Starting value which defaults to `0`.
stop (float or int, optional): Stopping value.
step (float or int, optional): Increment which defaults to `1`.
dtype (Dtype, optional): Specifies the data type of the output. If unspecified will default to `float32` if any of `start`, `stop`, or `step` are `float`. Otherwise will default to `int32`, or `int64` if any of `start`, `stop`, or `step` does not fit in `int32`.

Returns:array: The range of values.

Note:Following the Numpy convention the actual increment used to
generate numbers is `dtype(start + step) - dtype(start)`.
This can lead to unexpected results for example if start + step
is a fractional value and the dtype is integral.

`arange(stop : int | float, step : None | int | float = None, dtype: Dtype | None = None, *, stream: StreamOrDevice = None) -> array`

**arange(*stop: int | float*, *step: None | int | float = None*, *dtype: Dtype | None = None*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Overloaded function.

`arange(start : int | float, stop : None | int | float, step : None | int | float, dtype: Dtype | None = None, *, stream: StreamOrDevice = None) -> array`

Generates ranges of numbers.
Generate numbers in the half-open interval `[start, stop)` in
increments of `step`.

Args:start (float or int, optional): Starting value which defaults to `0`.
stop (float or int, optional): Stopping value.
step (float or int, optional): Increment which defaults to `1`.
dtype (Dtype, optional): Specifies the data type of the output. If unspecified will default to `float32` if any of `start`, `stop`, or `step` are `float`. Otherwise will default to `int32`, or `int64` if any of `start`, `stop`, or `step` does not fit in `int32`.

Returns:array: The range of values.

Note:Following the Numpy convention the actual increment used to
generate numbers is `dtype(start + step) - dtype(start)`.
This can lead to unexpected results for example if start + step
is a fractional value and the dtype is integral.

`arange(stop : int | float, step : None | int | float = None, dtype: Dtype | None = None, *, stream: StreamOrDevice = None) -> array`

** Contents
