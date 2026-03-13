---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.AvgPool1d.html
---

# mlx.nn.AvgPool1d

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.AvgPool1d.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.AvgPool1d

 Table of contents 

## Contents

# mlx.nn.AvgPool1d

**class AvgPool1d(*kernel_size: int | Tuple[int]*, *stride: int | Tuple[int] | None = None*, *padding: int | Tuple[int] = 0*)**
: Applies 1-dimensional average pooling.
Spatially downsamples the input by taking the average of a sliding window
of size `kernel_size` and sliding stride `stride`.

Parameters:

**kernel_size** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)*) – The size of the pooling window kernel.
**stride** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – The stride of the pooling window.
Default: `kernel_size`.
**padding** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – How much zero padding to apply to
the input. The padding amount is applied to both sides of the spatial
axis. Default: `0`.

Examples
>>> import mlx.core as mx
>>> import mlx.nn.layers as nn
>>> x = mx.random.normal(shape=(4, 16, 5))
>>> pool = nn.AvgPool1d(kernel_size=2, stride=2)
>>> pool(x)

Methods

** Contents
