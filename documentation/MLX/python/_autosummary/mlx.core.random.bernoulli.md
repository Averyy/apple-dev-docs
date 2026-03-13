---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.bernoulli.html
---

# mlx.core.random.bernoulli

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.bernoulli.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.random.bernoulli

 Table of contents 

## Contents

# mlx.core.random.bernoulli

**bernoulli(*p: scalar | array = 0.5*, *shape: Sequence[int] | None = None*, *key: array | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate Bernoulli random values.
The values are sampled from the bernoulli distribution with parameter
`p`. The parameter `p` can be a [float](https://docs.python.org/3/library/functions.html#float) or [array](https://docs.python.org/3/library/array.html#module-array) and
must be broadcastable to `shape`.

Parameters:

**p** ([float](https://docs.python.org/3/library/functions.html#float)* or *[array](mlx.core.array.html#mlx.core.array)*, **optional*) – Parameter of the Bernoulli
distribution. Default: `0.5`.
**shape** ([list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – Shape of the output.
Default: `p.shape`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The array of random integers.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
