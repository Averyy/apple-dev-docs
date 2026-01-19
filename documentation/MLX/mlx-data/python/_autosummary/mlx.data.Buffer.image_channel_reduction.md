---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.image_channel_reduction.html
---

# mlx.data.Buffer.image_channel_reduction

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.image_channel_reduction.rst)
- **

.pdf

**

# mlx.data.Buffer.image_channel_reduction

 Table of contents 

## Contents

# mlx.data.Buffer.image_channel_reduction

**Buffer.image_channel_reduction(*self: mlx.data._c.Buffer*, *key: str*, *preset: str = 'default'*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Reduce an RGB image to gray-scale with various weights for red, green
and blue.

Preset Name
Red weight
Green weight
Blue weight

default/rec601
0.299
0.587
0.114

rec709
0.2126
0.7152
0.0722

rec2020
0.2627
0.678
0.0593

green
0
1
0

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**preset** (*default**|**rec601**|**rec709**|**rec2020**|**green*) – The preset defining the reduction weights to gray scale.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If it is not empty then write the result to this
key instead of overwriting `key`. (default: ‘’)

** Contents
