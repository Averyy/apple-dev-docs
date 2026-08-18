---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Dropout3d.html
---

# mlx.nn.Dropout3d

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Dropout3d.rst)
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

# mlx.nn.Dropout3d

 Table of contents 

## Contents

# mlx.nn.Dropout3d

**class Dropout3d(*p: float = 0.5*)**
: Apply 3D channel-wise dropout during training.
Randomly zero out entire channels independently with probability \(p\).
This layer expects the channels to be last, i.e., the input shape should be
NDHWC or DHWC where: N is the batch dimension, D is the depth,
H is the input image height, W is the input image width, and C is
the number of input channels.
The remaining channels are scaled by \(\frac{1}{1-p}\) to
maintain the expected value of each element. Unlike traditional dropout,
which zeros individual entries, this layer zeros entire channels. This is
often beneficial for convolutional layers processing 3D data, like in
medical imaging or video processing.

Parameters:
**p** ([float](https://docs.python.org/3/library/functions.html#float)) – Probability of zeroing a channel during training.
Default: `0.5`.

Methods

** Contents
