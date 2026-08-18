---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.conv1d.html
---

# mlx.core.conv1d

**

- [.rst](../../_sources/python/_autosummary/mlx.core.conv1d.rst)
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

# mlx.core.conv1d

 Table of contents 

## Contents

# mlx.core.conv1d

**conv1d(*input: array*, *weight: array*, */*, *stride: int = 1*, *padding: int = 0*, *dilation: int = 1*, *groups: int = 1*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: 1D convolution over an input with several channels

Parameters:

**input** ([array](mlx.core.array.html#mlx.core.array)) – Input array of shape `(N, L, C_in)`.
**weight** ([array](mlx.core.array.html#mlx.core.array)) – Weight array of shape `(C_out, K, C_in)`.
**stride** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Kernel stride. Default: `1`.
**padding** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Input padding. Default: `0`.
**dilation** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Kernel dilation. Default: `1`.
**groups** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Input feature groups. Default: `1`.

Returns:
The convolved array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
