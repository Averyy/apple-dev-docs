---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Upsample.html
---

# mlx.nn.Upsample

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Upsample.rst)
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

# mlx.nn.Upsample

 Table of contents 

## Contents

# mlx.nn.Upsample

**class Upsample(*scale_factor: float | Tuple*, *mode: Literal['nearest', 'linear', 'cubic'] = 'nearest'*, *align_corners: bool = False*, *antialias: bool = False*)**
: Upsample the input signal spatially.
The spatial dimensions are by convention dimensions `1` to `x.ndim -
2`. The first is the batch dimension and the last is the feature
dimension.
For example, an audio signal would be 3D with 1 spatial dimension, an image
4D with 2 and so on and so forth.
There are three upsampling algorithms implemented nearest neighbor upsampling,
linear interpolation, and cubic interpolation. All can be applied to any number
of spatial dimensions. The linear interpolation will be bilinear, trilinear etc
when applied to more than one spatial dimension. And cubic interpolation will be
bicubic when there are 2 spatial dimensions.

Note
When using one of the linear or cubic interpolation modes the `align_corners`
argument changes how the corners are treated in the input image. If
`align_corners=True` then the top and left edge of the input and
output will be matching as will the bottom right edge.

Note
When `antialias=True` is used with `"linear"` or `"cubic"` mode,
an antialiased filter is applied during downsampling (scale factor < 1),
producing smoother results by avoiding aliasing artifacts. For 2D
integer-ratio downscales with `align_corners=False`, this matches the
behavior of PyTorch’s `F.interpolate(antialias=True)`. Non-integer
scale factors are supported but may differ from PyTorch because of
existing index-selection differences.
For `"cubic"` mode, enabling `antialias` also changes the cubic
kernel coefficient from `a=-0.75` (OpenCV convention) to `a=-0.5`
(PIL/Pillow convention), matching PyTorch’s behavior. This affects the
interpolant shape, not just the filter width.
`antialias=True` with `align_corners=True` is not supported and
will raise a `ValueError`.

Parameters:

**scale_factor** ([float](https://docs.python.org/3/library/functions.html#float)* or *[tuple](https://docs.python.org/3/library/stdtypes.html#tuple)) – The multiplier for the spatial size.
If a `float` is provided, it is the multiplier for all spatial dimensions.
Otherwise, the number of scale factors provided must match the
number of spatial dimensions.
**mode** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – The upsampling algorithm, either `"nearest"`,
`"linear"` or `"cubic"`. Default: `"nearest"`.
**align_corners** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Changes the way the corners are treated
during `"linear"` and `"cubic"` upsampling.  See the note above and the
examples below for more details.  Default: `False`.
**antialias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True`, apply an antialiasing filter
when downsampling with `"linear"` or `"cubic"` mode. For
`"cubic"` mode this also switches the kernel coefficient to
`a=-0.5`. Not supported with `"nearest"` mode or with
`align_corners=True`. Default: `False`.

Examples
>>> import mlx.core as mx
>>> import mlx.nn as nn
>>> x = mx.arange(1, 5).reshape((1, 2, 2, 1))
>>> x
array([[[[1],
         [2]],
        [[3],
         [4]]]], dtype=int32)
>>> n = nn.Upsample(scale_factor=2, mode='nearest')
>>> n(x).squeeze()
array([[1, 1, 2, 2],
       [1, 1, 2, 2],
       [3, 3, 4, 4],
       [3, 3, 4, 4]], dtype=int32)
>>> b = nn.Upsample(scale_factor=2, mode='linear')
>>> b(x).squeeze()
array([[1, 1.25, 1.75, 2],
       [1.5, 1.75, 2.25, 2.5],
       [2.5, 2.75, 3.25, 3.5],
       [3, 3.25, 3.75, 4]], dtype=float32)
>>> b = nn.Upsample(scale_factor=2, mode='linear', align_corners=True)
>>> b(x).squeeze()
array([[1, 1.33333, 1.66667, 2],
       [1.66667, 2, 2.33333, 2.66667],
       [2.33333, 2.66667, 3, 3.33333],
       [3, 3.33333, 3.66667, 4]], dtype=float32)

Methods

** Contents
