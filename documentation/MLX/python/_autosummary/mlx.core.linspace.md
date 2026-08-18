---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linspace.html
---

# mlx.core.linspace

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linspace.rst)
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

# mlx.core.linspace

 Table of contents 

## Contents

# mlx.core.linspace

**linspace(*start: scalar*, *stop: scalar*, *num: int | None = 50*, *endpoint: bool = True*, *dtype: Dtype | None = float32*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate `num` evenly spaced numbers over interval `[start, stop]`.

Parameters:

**start** (*scalar*) – Starting value.
**stop** (*scalar*) – Stopping value.
**num** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Number of samples, defaults to `50`.
**endpoint** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, `stop` is the last
sample. Otherwise it is not included and the samples are spaced
over the half-open interval `[start, stop)`. Default: `True`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Specifies the data type of the output,
default to `float32`.

Returns:
The range of values.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
