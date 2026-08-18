---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.laplace.html
---

# mlx.core.random.laplace

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.laplace.rst)
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

# mlx.core.random.laplace

 Table of contents 

## Contents

# mlx.core.random.laplace

**laplace(*shape: Sequence[int] = []*, *dtype: Dtype | None = float32*, *loc: float = 0.0*, *scale: float = 1.0*, *key: array | None = None*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Sample numbers from a Laplace distribution.

Parameters:

**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Shape of the output. Default: `()`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Type of the output. Default: `float32`.
**loc** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Mean of the distribution. Default: `0.0`.
**scale** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The scale “b” of the Laplace distribution.
Default:`1.0`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The output array of random values.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
