---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.key_transform.html
---

# mlx.data.Buffer.key_transform

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.key_transform.rst)
- **

.pdf

**

# mlx.data.Buffer.key_transform

 Table of contents 

## Contents

# mlx.data.Buffer.key_transform

**Buffer.key_transform(*self: mlx.data._c.Buffer*, *key: str*, *func: Callable[[numpy.ndarray], numpy.ndarray]*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Apply the python function `func` on the arrays in the selected `key`.
The function should return a value that can be cast to an array ie
something implementing the buffer protocol.
An example use of the transformation is shown below:
from mlx.data.datasets import load_mnist

mnist = (
    load_mnist()
    .key_transform("image", lambda x: x.astype("float32") / 255)
)

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**func** (*callable*) – The function to apply.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to store the result in. If it is an empty
string then overwrite the input. (default: ‘’)

** Contents
