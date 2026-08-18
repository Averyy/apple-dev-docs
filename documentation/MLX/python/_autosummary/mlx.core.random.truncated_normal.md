---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.truncated_normal.html
---

# mlx.core.random.truncated_normal

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.truncated_normal.rst)
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

# mlx.core.random.truncated_normal

 Table of contents 

## Contents

# mlx.core.random.truncated_normal

**truncated_normal(*lower: scalar | array*, *upper: scalar | array*, *shape: Sequence[int] | None = None*, *dtype: Dtype | None = float32*, *key: array | None = None*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate values from a truncated normal distribution.
The values are sampled from the truncated normal distribution
on the domain `(lower, upper)`. The bounds `lower` and `upper`
can be scalars or arrays and must be broadcastable to `shape`.

Parameters:

**lower** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)) – Lower bound of the domain.
**upper** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)) – Upper bound of the domain.
**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – The shape of the output.
Default:`()`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the output.
Default: `float32`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The output array of random values.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
