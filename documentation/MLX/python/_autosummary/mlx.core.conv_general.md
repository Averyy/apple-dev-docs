---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.conv_general.html
---

# mlx.core.conv_general

**

- [.rst](../../_sources/python/_autosummary/mlx.core.conv_general.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.conv_general

 Table of contents 

## Contents

# mlx.core.conv_general

**conv_general(*input: array*, *weight: array*, */*, *stride: int | Sequence[int] = 1*, *padding: int | Sequence[int] | tuple[Sequence[int], Sequence[int]] = 0*, *kernel_dilation: int | Sequence[int] = 1*, *input_dilation: int | Sequence[int] = 1*, *groups: int = 1*, *flip: bool = False*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: General convolution over an input with several channels

Parameters:

**input** ([array](mlx.core.array.html#mlx.core.array)) – Input array of shape `(N, ..., C_in)`.
**weight** ([array](mlx.core.array.html#mlx.core.array)) – Weight array of shape `(C_out, ..., C_in)`.
**stride** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – [list](https://docs.python.org/3/library/stdtypes.html#list) with kernel strides.
All spatial dimensions get the same stride if
only one number is specified. Default: `1`.
**padding** ([int](https://docs.python.org/3/library/functions.html#int)*, *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*(*[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**)**, **optional*) – [list](https://docs.python.org/3/library/stdtypes.html#list) with input padding. All spatial dimensions get the same
padding if only one number is specified. Default: `0`.
**kernel_dilation** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – [list](https://docs.python.org/3/library/stdtypes.html#list) with
kernel dilation. All spatial dimensions get the same dilation
if only one number is specified. Default: `1`
**input_dilation** ([int](https://docs.python.org/3/library/functions.html#int)* or *[list](https://docs.python.org/3/library/stdtypes.html#list)*(*[int](https://docs.python.org/3/library/functions.html#int)*)**, **optional*) – [list](https://docs.python.org/3/library/stdtypes.html#list) with
input dilation. All spatial dimensions get the same dilation
if only one number is specified. Default: `1`
**groups** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Input feature groups. Default: `1`.
**flip** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Flip the order in which the spatial dimensions of
the weights are processed. Performs the cross-correlation operator when
`flip` is `False` and the convolution operator otherwise.
Default: `False`.

Returns:
The convolved array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
