---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.buffer_from_vector.html
---

# mlx.data.buffer_from_vector

**

- [.rst](../../_sources/python/_autosummary/mlx.data.buffer_from_vector.rst)
- **

.pdf

**

# mlx.data.buffer_from_vector

 Table of contents 

## Contents

# mlx.data.buffer_from_vector

**mlx.data.buffer_from_vector(*data: list*) → mlx.data._c.Buffer**
: Make a buffer from a list of dictionaries.
This is the main factory method for making buffers to process data
using MLX Data. For instance the following code makes a buffer of
filenames and then lazily loads images from these filenames.
import mlx.data as dx

def list_files(root: Path):
    files = list(root.rglob("*.jpg"))
    classes = sorted(set(f.parent.name for f in files))
    classes = dict((v, i) for i, v in enumerate(classes))
    return [
      {"file": str(f.relative_to(root)).encode(), "label": classes[f.parent.name]}
      for f in files
    ]

root = Path("/path/to/image/dataset")
dset = (
  dx.buffer_from_vector(list_files(root))
  .load_image("file", prefix=str(root), output_key="image")
)

Parameters:
**data** ([list](https://docs.python.org/3/library/stdtypes.html#list)* of **dicts*) – The list of samples to make a buffer out of.

** Contents
