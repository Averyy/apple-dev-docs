---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.MaxPool2d.html
---

# mlx.nn.MaxPool2d

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.MaxPool2d.rst)
- **

.pdf

**

# mlx.nn.MaxPool2d

 Table of contents 

## Contents

# mlx.nn.MaxPool2d

**class MaxPool2d(*kernel_size: int | Tuple[int, int]*, *stride: int | Tuple[int, int] | None = None*, *padding: int | Tuple[int, int] | None = 0*)**
: Applies 2-dimensional max pooling.
Spatially downsamples the input by taking the maximum of a sliding window
of size `kernel_size` and sliding stride `stride`.
The parameters `kernel_size`, `stride`, and `padding` can either be:

a single `int` – in which case the same value is used for both the
height and width axis.
a `tuple` of two `int` s – in which case, the first `int` is
used for the height axis, the second `int` for the width axis.

Parameters:

**kernel_size** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*)*) – The size of the pooling window.
**stride** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – The stride of the pooling
window. Default: `kernel_size`.
**padding** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*, *[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – How much negative infinity
padding to apply to the input. The padding is applied on both sides
of the height and width axis. Default: `0`.

Examples
>>> import mlx.core as mx
>>> import mlx.nn.layers as nn
>>> x = mx.random.normal(shape=(8, 32, 32, 4))
>>> pool = nn.MaxPool2d(kernel_size=2, stride=2)
>>> pool(x)

Methods

** Contents
