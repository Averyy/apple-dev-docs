---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Conv3d.html
---

# mlx.nn.Conv3d

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Conv3d.rst)
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

# mlx.nn.Conv3d

 Table of contents 

## Contents

# mlx.nn.Conv3d

**class Conv3d(*in_channels: int*, *out_channels: int*, *kernel_size: int | tuple*, *stride: int | tuple = 1*, *padding: int | tuple = 0*, *dilation: int | tuple = 1*, *bias: bool = True*)**
: Applies a 3-dimensional convolution over the multi-channel input image.
The channels are expected to be last i.e. the input shape should be `NDHWC` where:

`N` is the batch dimension
`D` is the input image depth
`H` is the input image height
`W` is the input image width
`C` is the number of input channels

Parameters:

**in_channels** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of input channels.
**out_channels** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of output channels.
**kernel_size** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)) – The size of the convolution filters.
**stride** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*, **optional*) – The size of the stride when
applying the filter. Default: `1`.
**padding** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*, **optional*) – How many positions to 0-pad
the input with. Default: `0`.
**dilation** ([int](https://docs.python.org/3/library/functions.html#int)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)*, **optional*) – The dilation of the convolution.
Default: `1`.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True` add a learnable bias to the
output. Default: `True`

Methods

** Contents
