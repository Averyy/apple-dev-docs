---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.image_random_area_crop.html
---

# mlx.data.Buffer.image_random_area_crop

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.image_random_area_crop.rst)
- **

.pdf

**

# mlx.data.Buffer.image_random_area_crop

 Table of contents 

## Contents

# mlx.data.Buffer.image_random_area_crop

**Buffer.image_random_area_crop(*self: mlx.data._c.Buffer*, *key: str*, *area_range: Tuple[float, float]*, *aspect_ratio_range: Tuple[float, float]*, *num_trial: int = 10*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Crop the image randomly such that the result is a portion of the
original area and within the given aspect ratio range.
The random crop is found using rejection sampling, namely we sample a
random width within the range of possible widths, then a random height
within the range of possible heights. Finally, we check if the area and
aspect ratio constraints are met before cropping the image.
If we can’t sample a random crop that meets the constraints the
original image is returned.
Example:
# Extract a random square crop that is from 50% to 100% the original
# image area
dset = dset.image_random_area_crop("image", (0.5, 1.0), (1.0, 1.0))

# Extract a random crop that is 50% to 75% of the original area and
# from square to 3:2 aspect ratio.
dset = dset.image_random_area_crop("image", (0.5, 0.75), (1.0, 1.5))

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**area_range** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)* of **floats*) – A minimum and maximum area portion for the crop.
**aspect_ratio_range** ([tuple](https://docs.python.org/3/library/stdtypes.html#tuple)* of **floats*) – A minimum and maximum aspect
ratio for the crop. The aspect ratio is defined as the width
divided by the height of the image.
**num_trial** ([int](https://docs.python.org/3/library/functions.html#int)) – How many rejection sampling attempts to perform. (default: 10)
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If it is not empty then write the result to this
key instead of overwriting `key`. (default: ‘’)

** Contents
