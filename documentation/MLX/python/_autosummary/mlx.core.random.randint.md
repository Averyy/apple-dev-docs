---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.randint.html
---

# mlx.core.random.randint

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.randint.rst)
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

# mlx.core.random.randint

 Table of contents 

## Contents

# mlx.core.random.randint

**randint(*low: scalar | array*, *high: scalar | array*, *shape: Sequence[int] = []*, *dtype: Dtype | None = int32*, *key: array | None = None*, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate random integers from the given interval.
The values are sampled with equal probability from the integers in
half-open interval `[low, high)`. The lower and upper bound can be
scalars or arrays and must be broadcastable to `shape`.

Note
The samples are drawn from a `float32` uniform and clamped to
`[low, high - 1]`, so not every integer in the range is reachable
once the bounds or the width of the interval go beyond the
`2**24` integer resolution of `float32`.

Parameters:

**low** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)) – Lower bound of the interval.
**high** (*scalar** or *[array](mlx.core.array.html#mlx.core.array)) – Upper bound of the interval.
**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Shape of the output. Default: `()`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Type of the output. Default: `int32`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The array of random integers.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
