---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.multivariate_normal.html
---

# mlx.core.random.multivariate_normal

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.multivariate_normal.rst)
- **

.pdf

**

# mlx.core.random.multivariate_normal

 Table of contents 

## Contents

# mlx.core.random.multivariate_normal

**multivariate_normal(*mean: array*, *cov: array*, *shape: Sequence[int] = []*, *dtype: Dtype | None = float32*, *key: array | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate jointly-normal random samples given a mean and covariance.
The matrix `cov` must be positive semi-definite. The behavior is
undefined if it is not.  The only supported `dtype` is `float32`.

Parameters:

**mean** ([array](mlx.core.array.html#mlx.core.array)) – array of shape `(..., n)`, the mean of the
distribution.
**cov** ([array](mlx.core.array.html#mlx.core.array)) – array  of shape `(..., n, n)`, the covariance
matrix of the distribution. The batch shape `...` must be
broadcast-compatible with that of `mean`.
**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – The output shape must be
broadcast-compatible with `mean.shape[:-1]` and `cov.shape[:-2]`.
If empty, the result shape is determined by broadcasting the batch
shapes of `mean` and `cov`. Default: `[]`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The output type. Default: `float32`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The output array of random values.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
