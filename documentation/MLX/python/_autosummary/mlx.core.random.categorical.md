---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.categorical.html
---

# mlx.core.random.categorical

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.categorical.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.random.categorical

 Table of contents 

## Contents

# mlx.core.random.categorical

**categorical(*logits: array*, *axis: int = -1*, *shape: Sequence[int] | None = None*, *num_samples: int | None = None*, *key: array | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Sample from a categorical distribution.
The values are sampled from the categorical distribution specified by
the unnormalized values in `logits`. Note, at most one of `shape`
or `num_samples` can be specified. If both are `None`, the output
has the same shape as `logits` with the `axis` dimension removed.

Parameters:

**logits** ([array](mlx.core.array.html#mlx.core.array)) – The *unnormalized* categorical distribution(s).
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The axis which specifies the distribution.
Default: `-1`.
**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – The shape of the output. This must
be broadcast compatible with `logits.shape` with the `axis`
dimension removed. Default: `None`
**num_samples** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of samples to draw from each
of the categorical distributions in `logits`. The output will have
`num_samples` in the last dimension. Default: `None`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The `shape`-sized output array with type `uint32`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
