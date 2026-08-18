---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Dropout2d.html
---

# mlx.nn.Dropout2d

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Dropout2d.rst)
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

# mlx.nn.Dropout2d

 Table of contents 

## Contents

# mlx.nn.Dropout2d

**class Dropout2d(*p: float = 0.5*)**
: Apply 2D channel-wise dropout during training.
Randomly zero out entire channels independently with probability \(p\).
This layer expects the channels to be last, i.e. the input shape should be
`NHWC` or `HWC` where:`N` is the batch dimension,``H`` is the input
image height,``W`` is the input image width, and``C`` is the number of
input channels
The remaining channels are scaled by \(\frac{1}{1-p}\) to
maintain the expected value of each element. Unlike traditional dropout,
which zeros individual entries, this layer zeros entire channels. This is
beneficial for early convolution layers where adjacent pixels are
correlated. In such case, traditional dropout may not effectively
regularize activations. For more details, see [1].
[1]: Thompson, J., Goroshin, R., Jain, A., LeCun, Y. and Bregler C., 2015.
Efficient Object Localization Using Convolutional Networks. CVPR 2015.

Parameters:
**p** ([float](https://docs.python.org/3/library/functions.html#float)) – Probability of zeroing a channel during training.
Default: `0.5`.

Methods

** Contents
