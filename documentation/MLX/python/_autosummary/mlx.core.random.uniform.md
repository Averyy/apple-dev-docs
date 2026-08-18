---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.uniform.html
---

# mlx.core.random.uniform

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.uniform.rst)
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

# mlx.core.random.uniform

 Table of contents 

## Contents

# mlx.core.random.uniform

**uniform(*low: scalar | array = 0*, *high: scalar | array = 1*, *shape: Sequence[int] = []*, *dtype: Dtype | None = float32*, *key: array | None = None*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate uniformly distributed random numbers.
The values are sampled uniformly in the half-open interval `[low, high)`.
The lower and upper bound can be scalars or arrays and must be
broadcastable to `shape`.

Parameters:

**low** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)*, **optional*) – Lower bound of the distribution.
Default: `0`.
**high** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)*, **optional*) – Upper bound of the distribution.
Default: `1`.
**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Shape of the output. Default:`()`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Type of the output. Default: `float32`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The output array random values.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
