---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.rms_norm.html
---

# mlx.core.fast.rms_norm

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fast.rms_norm.rst)
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

# mlx.core.fast.rms_norm

 Table of contents 

## Contents

# mlx.core.fast.rms_norm

**rms_norm(*x: array*, *weight: array | None*, *eps: float*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Root Mean Square normalization (RMS norm).
The normalization is with respect to the last axis of the input `x`.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**weight** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – A multiplicative weight to scale the result by.
The `weight` should be one-dimensional with the same size
as the last axis of `x`. If set to `None` then no scaling happens.
**eps** ([float](https://docs.python.org/3/library/functions.html#float)) – A small additive constant for numerical stability.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
