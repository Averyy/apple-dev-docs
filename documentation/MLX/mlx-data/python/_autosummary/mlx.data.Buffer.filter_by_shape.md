---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.filter_by_shape.html
---

# mlx.data.Buffer.filter_by_shape

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.filter_by_shape.rst)
- **

.pdf

**

# mlx.data.Buffer.filter_by_shape

 Table of contents 

## Contents

# mlx.data.Buffer.filter_by_shape

**Buffer.filter_by_shape(*self: mlx.data._c.Buffer*, *key: str*, *dim: int*, *low: int = -1*, *high: int = -1*) → mlx.data._c.Buffer**
: Filter samples based on the shape of the array.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**dim** ([int](https://docs.python.org/3/library/functions.html#int)) – The shape dimension based on which we are filtering.
**low** ([int](https://docs.python.org/3/library/functions.html#int)) – Minimum acceptable size for the dimension (inclusive).
**high** ([int](https://docs.python.org/3/library/functions.html#int)) – Maximum acceptable size for the dimension (inclusive). If
negative size is given then it is assumed we have no upper limit.

** Contents
