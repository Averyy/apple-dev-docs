---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.layer_norm.html
---

# mlx.core.fast.layer_norm

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fast.layer_norm.rst)
- **

.pdf

**

# mlx.core.fast.layer_norm

 Table of contents 

## Contents

# mlx.core.fast.layer_norm

**layer_norm(*x: array*, *weight: array | None*, *bias: array | None*, *eps: float*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Layer normalization.
The normalization is with respect to the last axis of the input `x`.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**weight** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A multiplicative weight to scale the result by.
The `weight` should be one-dimensional with the same size
as the last axis of `x`. If set to `None` then no scaling happens.
**bias** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – An additive offset to be added to the result.
The `bias` should be one-dimensional with the same size
as the last axis of `x`. If set to `None` then no translation happens.
**eps** ([float](https://docs.python.org/3/library/functions.html#float)) – A small additive constant for numerical stability.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
