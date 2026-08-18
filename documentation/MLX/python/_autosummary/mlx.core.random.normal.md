---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.normal.html
---

# mlx.core.random.normal

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.normal.rst)
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

# mlx.core.random.normal

 Table of contents 

## Contents

# mlx.core.random.normal

**normal(*shape: Sequence[int] = []*, *dtype: Dtype | None = float32*, *loc: scalar | array | None = None*, *scale: scalar | array | None = None*, *key: array | None = None*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate normally distributed random numbers.
If `loc` and `scale` are not provided the “standard” normal
distribution is used. That means $x sim mathcal{N}(0, 1)$ for
real numbers and $text{Re}(x),text{Im}(x) sim mathcal{N}(0,
frac{1}{2})$ for complex numbers.

Parameters:

**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Shape of the output. Default: `()`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Type of the output. Default: `float32`.
**loc** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)*, **optional*) – Mean of the distribution.
Default: `None`.
**scale** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)*, **optional*) – Standard deviation of the
distribution. Default: `None`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The output array of random values.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
