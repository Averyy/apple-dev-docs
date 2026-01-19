---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.sample_transform.html
---

# mlx.data.Buffer.sample_transform

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.sample_transform.rst)
- **

.pdf

**

# mlx.data.Buffer.sample_transform

 Table of contents 

## Contents

# mlx.data.Buffer.sample_transform

**Buffer.sample_transform(*self: mlx.data._c.Buffer*, *func: Callable[[dict], dict]*) → mlx.data._c.Buffer**
: Apply the python function `func` on whole samples.
The function should return a dictionary of arrays or values that can be
cast to arrays (buffers, scalars etc). When used with `Stream`
it can also be used to skip samples by returning an empty dictionary.
This transformation is very powerful but it should be used with caution
given that python is slightly plagued by the global interpreter lock.
See the [Quick Start](../../quick_start.html#about-the-gil) for more.

Parameters:
**func** (*callable*) – The function to apply.

** Contents
