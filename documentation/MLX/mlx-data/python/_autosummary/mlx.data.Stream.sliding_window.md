---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Stream.sliding_window.html
---

# mlx.data.Stream.sliding_window

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Stream.sliding_window.rst)
- **

.pdf

**

# mlx.data.Stream.sliding_window

 Table of contents 

## Contents

# mlx.data.Stream.sliding_window

**Stream.sliding_window(*self: mlx.data._c.Stream*, *key: str*, *size: int*, *stride: int*, *dim: int = -1*, *index_key: str = ''*) → mlx.data._c.Stream**
: Creates sample by sliding a window over the array at `key`.
Commonly used in sequence processing pipelines to deal with
very larger documents.
import mlx.data as dx

dset = dx.buffer_from_vector({"x": np.arange(10), "unchanged_keys": 10}).to_stream()

for sample in dset.sliding_window("x", 3, 2):
    print(sample["x"])

# prints
# [0, 1, 2]
# [2, 3, 4]
# [4, 5, 6]
# [6, 7, 8]
# [8, 9]

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**size** ([int](https://docs.python.org/3/library/functions.html#int)) – The size of the sliding window.
**stride** ([int](https://docs.python.org/3/library/functions.html#int)) – The stride of the sliding window.
**dim** ([int](https://docs.python.org/3/library/functions.html#int)) – Which dimension are we sliding the window over. (default: -1)
**index_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – If provided, store the index of the sliding window in
that key. (default: “”)

** Contents
