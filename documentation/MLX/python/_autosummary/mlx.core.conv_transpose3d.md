---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.conv_transpose3d.html
---

# mlx.core.conv_transpose3d

**

- [.rst](../../_sources/python/_autosummary/mlx.core.conv_transpose3d.rst)
- **

.pdf

**

# mlx.core.conv_transpose3d

 Table of contents 

## Contents

# mlx.core.conv_transpose3d

**conv_transpose3d(*input: array*, *weight: array*, */*, *stride: int | Tuple[int, int, int] = 1*, *padding: int | Tuple[int, int, int] = 0*, *dilation: int | Tuple[int, int, int] = 1*, *output_padding: int | Tuple[int, int, int] = 0*, *groups: int = 1*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: 3D transposed convolution over an input with several channels
Note: Only the default `groups=1` is currently supported.

Parameters:

**input** ([array](mlx.core.array.html#mlx.core.array)) – Input array of shape `(N, D, H, W, C_in)`.
**weight** ([array](mlx.core.array.html#mlx.core.array)) – Weight array of shape `(C_out, KD, KH, KW, C_in)`.
**stride** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – [tuple](https://docs.python.org/3/library/stdtypes.html#tuple) of size 3 with
kernel strides. All spatial dimensions get the same stride if
only one number is specified. Default: `1`.
**padding** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – [tuple](https://docs.python.org/3/library/stdtypes.html#tuple) of size 3 with
symmetric input padding. All spatial dimensions get the same
padding if only one number is specified. Default: `0`.
**dilation** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – [tuple](https://docs.python.org/3/library/stdtypes.html#tuple) of size 3 with
kernel dilation. All spatial dimensions get the same dilation
if only one number is specified. Default: `1`
**output_padding** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – [tuple](https://docs.python.org/3/library/stdtypes.html#tuple) of size 3 with
output padding. All spatial dimensions get the same output
padding if only one number is specified. Default: `0`.
**groups** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – input feature groups. Default: `1`.

Returns:
The convolved array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
