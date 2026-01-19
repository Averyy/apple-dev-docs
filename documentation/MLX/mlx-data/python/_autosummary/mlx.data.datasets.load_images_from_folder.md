---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.datasets.load_images_from_folder.html
---

# mlx.data.datasets.load_images_from_folder

**

- [.rst](../../_sources/python/_autosummary/mlx.data.datasets.load_images_from_folder.rst)
- **

.pdf

**

# mlx.data.datasets.load_images_from_folder

 Table of contents 

## Contents

# mlx.data.datasets.load_images_from_folder

**mlx.data.datasets.load_images_from_folder(*image_folder*)**
: Load images from a folder.
For a directory structure like the following
image_folder/
...class_1/
......foo.jpg
......bar.png
...class_2/
......baz.jpg
......foo_again.png

this function will return a `Buffer` that contains samples
with the following keys

**folder**: the name of the category of this sample (e.g. class_1, class_2 etc)
**label**: an integer that corresponds to the sorted position of the folder
names (e.g. class_1 gets 0 and class_2 gets 1)
**file**: the path to the image relative to the provided root folder
**image**: the loaded image array

Parameters:
**image_folder** – (Path or str): The directory to load the images from.

** Contents
