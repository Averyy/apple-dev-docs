---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.init.sparse.html
---

# mlx.nn.init.sparse

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.init.sparse.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.init.sparse

 Table of contents 

## Contents

# mlx.nn.init.sparse

**sparse(*sparsity: float*, *mean: float = 0.0*, *std: float = 1.0*, *dtype: Dtype = mlx.core.float32*) → [Callable](https://docs.python.org/3/library/typing.html#typing.Callable)[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]**
: An initializer that returns a sparse matrix.
Sparsity is applied along each row: every row has the same fraction of its
entries set to zero. With a weight matrix applied as `x @ w.T`, this
limits each output feature to at most a `1 - sparsity` fraction of the
input features, following the sparse initialization of Martens, J. (2010),
“Deep learning via Hessian-free optimization”.

Parameters:

**sparsity** ([float](https://docs.python.org/3/library/functions.html#float)) – The fraction of elements in each row to be set to
zero.
**mean** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Mean of the normal distribution. Default:
`0.0`.
**std** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – Standard deviation of the normal distribution.
Default: `1.0`.
**dtype** ([Dtype](../../_autosummary/mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the array. Default:
`float32`.

Returns:
An initializer that returns an array with the
same shape as the input, filled with samples from a normal distribution.

Return type:
*Callable*[[[array](../../_autosummary/mlx.core.array.html#mlx.core.array)], [array](../../_autosummary/mlx.core.array.html#mlx.core.array)]

Example
>>> init_fn = nn.init.sparse(sparsity=0.5)
>>> init_fn(mx.zeros((2, 2)))
array([[-1.91187, 0],

[0, -0.117483]], dtype=float32)

** Contents
