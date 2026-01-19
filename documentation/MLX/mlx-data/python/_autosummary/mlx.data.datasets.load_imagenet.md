---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.datasets.load_imagenet.html
---

# mlx.data.datasets.load_imagenet

**

- [.rst](../../_sources/python/_autosummary/mlx.data.datasets.load_imagenet.rst)
- **

.pdf

**

# mlx.data.datasets.load_imagenet

 Table of contents 

## Contents

# mlx.data.datasets.load_imagenet

**mlx.data.datasets.load_imagenet(*root=None*, *split='train'*, *quiet=False*, *validate_download=True*, *tar_index_threads=None*)**
: Load the ImageNet dataset from the downloaded archives.
ImageNet cannot be automatically downloaded so you have to manually
download it from [http://image-net.org/](http://image-net.org/) . You need the split you want to
load and the devkit for tasks 1 and 2.

Parameters:

**root** (*Path** or *[str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – The directory to load the data from. If
none is given then `~/.cache/mlx.data/imagenet` is used. However,
if the data is not there it *cannot* be downloaded automatically.
**split** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The split to use. It must be either ‘train’ or ‘val’.
**quiet** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true do not show progress bars.
**validate_download** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true validate the download if it isn’t
already validated.
**tar_index_threads** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – How many threads to use to index the
nested tar file for the imagenet training set. This is not used for
the validation set or if the tar file is extracted.

** Contents
