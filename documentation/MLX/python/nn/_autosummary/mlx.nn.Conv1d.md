---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Conv1d.html
---

# mlx.nn.Conv1d

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Conv1d.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.Conv1d

 Table of contents 

## Contents

# mlx.nn.Conv1d

**class Conv1d(*in_channels: int*, *out_channels: int*, *kernel_size: int*, *stride: int = 1*, *padding: int = 0*, *dilation: int = 1*, *groups: int = 1*, *bias: bool = True*)**
: Applies a 1-dimensional convolution over the multi-channel input sequence.
The channels are expected to be last i.e. the input shape should be `NLC` where:

`N` is the batch dimension
`L` is the sequence length
`C` is the number of input channels

Parameters:

**in_channels** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of input channels
**out_channels** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of output channels
**kernel_size** ([int](https://docs.python.org/3/library/functions.html#int)) – The size of the convolution filters
**stride** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The stride when applying the filter.
Default: `1`.
**padding** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – How many positions to 0-pad the input with.
Default: `0`.
**dilation** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The dilation of the convolution.
Default: `1`.
**groups** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of groups for the convolution.
Default: `1`.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True` add a learnable bias to the output.
Default: `True`

Methods

** Contents
