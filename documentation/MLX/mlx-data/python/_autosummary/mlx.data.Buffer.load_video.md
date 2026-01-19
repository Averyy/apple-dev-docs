---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.load_video.html
---

# mlx.data.Buffer.load_video

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.load_video.rst)
- **

.pdf

**

# mlx.data.Buffer.load_video

 Table of contents 

## Contents

# mlx.data.Buffer.load_video

**Buffer.load_video(*self: mlx.data._c.Buffer*, *key: str*, *prefix: str = ''*, *info: bool = False*, *from_memory: bool = False*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Load a video file.
Decodes a video file to memory from a file or from memory. If `info`
is true then it, instead, reads the information of the video, namely
width, height and number of frames.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use when loading the files. (default: ‘’)
**info** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True load the video width, height and frames instead
of the video data. (default: False)
**from_memory** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true assume the file contents are in the array
instead of the file name. (default: False)
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
