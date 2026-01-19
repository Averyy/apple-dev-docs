---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.gumbel.html
---

# mlx.core.random.gumbel

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.gumbel.rst)
- **

.pdf

**

# mlx.core.random.gumbel

 Table of contents 

## Contents

# mlx.core.random.gumbel

**gumbel(*shape: Sequence[int] = []*, *dtype: Dtype | None = float32*, *key: array | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Sample from the standard Gumbel distribution.
The values are sampled from a standard Gumbel distribution
which CDF `exp(-exp(-x))`.

Parameters:

**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – The shape of the output.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the output.
Default: `float32`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The `array` with shape `shape` and distributed according
to the Gumbel distribution.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
