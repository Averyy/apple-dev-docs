---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.batch.html
---

# mlx.data.Buffer.batch

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.batch.rst)
- **

.pdf

**

# mlx.data.Buffer.batch

 Table of contents 

## Contents

# mlx.data.Buffer.batch

**Buffer.batch(*self: mlx.data._c.Buffer*, *batch_size: int | List[int]*, *pad: Dict[str, float] = {}*, *dim: Dict[str, int] = {}*) → mlx.data._c.Buffer**
: Creates batches from `batch_size` consecutive samples.
When two samples have arrays that are not the same shape, the
batch shape is the smallest shape that contains all samples in
each dimension. The places that do not have values are filled
with `pad` values.
When a batch dimension is not provided, the arrays are stacked.
If it is provided, the arrays are concatenated along that
dimension.
The following example showcases the use the `dim` argument.
import mlx.data as dx
import numpy as np

dset = dx.buffer_from_vector([{"x": np.random.randn(10, i+1)} for i in range(10)])

print(dset.batch(4)[0]["x"].shape)  # prints (4, 10, 4)
print(dset.batch(4)[1]["x"].shape)  # prints (4, 10, 8)

print(dset.batch(4, dim=dict(x=0))[0]["x"].shape)  # prints (40, 4)
print(dset.batch(4, dim=dict(x=0))[1]["x"].shape)  # prints (40, 8)

print(dset.batch(4, dim=dict(x=1))[0]["x"].shape)  # prints (10, 10)
print(dset.batch(4, dim=dict(x=1))[1]["x"].shape)  # prints (10, 26)

Parameters:

**batch_size** ([int](https://docs.python.org/3/library/functions.html#int)) – How many samples to gather in a batch.
**pad** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – The values to use for padding for each key in the samples.
**dim** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – The dimension to concatenate over.

** Contents
