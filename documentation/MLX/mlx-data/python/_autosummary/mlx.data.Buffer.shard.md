---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.shard.html
---

# mlx.data.Buffer.shard

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.shard.rst)
- **

.pdf

**

# mlx.data.Buffer.shard

 Table of contents 

## Contents

# mlx.data.Buffer.shard

**Buffer.shard(*self: mlx.data._c.Buffer*, *key: str*, *num_shards: int*, *output_key: str = ''*) → mlx.data._c.Buffer**
: Split the first dimension in `num_shards`.
This operation performs the following numpy style reshape:
def shard(x):
  shape = x.shape
  return x.reshape(num_shards, -1, *shape[1:])

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**num_shards** ([int](https://docs.python.org/3/library/functions.html#int)) – The size of the first dimension of the reshaped array.
**output_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If it is not empty then write the result to this
key instead of overwriting `key`. (default: ‘’)

** Contents
