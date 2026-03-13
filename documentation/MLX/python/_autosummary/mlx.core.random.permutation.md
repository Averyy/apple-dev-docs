---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.random.permutation.html
---

# mlx.core.random.permutation

**

- [.rst](../../_sources/python/_autosummary/mlx.core.random.permutation.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.random.permutation

 Table of contents 

## Contents

# mlx.core.random.permutation

**permutation(*x: int | array*, *axis: int = 0*, *key: array | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Generate a random permutation or permute the entries of an array.

Parameters:

**x** ([int](https://docs.python.org/3/library/functions.html#int)* or *[array](mlx.core.array.html#mlx.core.array)*, **optional*) – If an integer is provided a random
permtuation of `mx.arange(x)` is returned. Otherwise the entries
of `x` along the given axis are randomly permuted.
**axis** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The axis to permute along. Default: `0`.
**key** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A PRNG key. Default: `None`.

Returns:
The generated random permutation or randomly permuted input array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
