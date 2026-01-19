---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Stream.dynamic_batch.html
---

# mlx.data.Stream.dynamic_batch

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Stream.dynamic_batch.rst)
- **

.pdf

**

# mlx.data.Stream.dynamic_batch

 Table of contents 

## Contents

# mlx.data.Stream.dynamic_batch

**Stream.dynamic_batch(*self: mlx.data._c.Stream*, *buffer_size: int*, *key: str*, *max_data_size: int = -1*, *pad: Dict[str, float] = {}*, *dim: Dict[str, int] = {}*, *shuffle: bool = False*, *num_threads: int = 1*) → mlx.data._c.Stream**
: Dynamic batching returns batches with approximately the same
number of total elements.
This is used to minimize padding and waste of computation when
dealing with samples that can have large variance in sizes.
For instance if we have a stream with a key ‘tokens’ and we
want batches that contain approximately 16k tokens but the
sample sizes vary from 64 to 1024 we can use dynamic batching
to group together smaller samples to reduce padding but keep
the total amount of work approximately constant.
import mlx.data as dx

def random_sample():
    N = int(np.random.rand() * (1024 - 64) + 64)
    return {"tokens": np.random.rand(N), "length": N}

def count_padding(sample):
    return (sample["tokens"].shape[-1] - sample["length"]).sum()

dset = dx.buffer_from_vector([random_sample() for _ in range(10_000)])

# Compute the average padding size with naive batching
naive_padding = sum(count_padding(s) for s in dset.to_stream().batch(16))

# And with dynamic padding. Keep in mind that this also
# ensures that the number of tokens in a batch are
# approximately constant.
dynbatch_padding = sum(count_padding(s) for s in dset.to_stream().dynamic_batch(500, "tokens", 16*1024))

# Count the total valid tokens
valid_tokens = sum(d["length"] for d in dset)

print("Simple batching: ", naive_padding / (valid_tokens + naive_padding), " of tokens were padding")
print("Dynamic batching: ", dynbatch_padding / (valid_tokens + dynbatch_padding), " of tokens were padding")

# prints approximately 40% of tokens were padding in the first case
# and 5% of tokens in the second case

Parameters:

**buffer_size** ([int](https://docs.python.org/3/library/functions.html#int)) – How many buffers to consider when computing the dynamic batching
**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – Which array’s size to use for the dynamic batching
**max_data_size** ([int](https://docs.python.org/3/library/functions.html#int)) – How many elements of the array at
`key` should each batch have. If less or equal to 0 then
batch the whole buffer in which case dynamic batching behaves
similar to `batch`. (default: -1)
**pad** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – The values to use for padding for each key in the samples.
**dim** ([dict](https://docs.python.org/3/library/stdtypes.html#dict)) – The dimension to concatenate over.
**shuffle** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If true shuffle the batches before returning
them. Otherwise the larger batch sizes with smaller samples
will be first and so on. (default: False)
**num_threads** ([int](https://docs.python.org/3/library/functions.html#int)) – How many parallel threads to use to fill the buffer. (default: 1)

** Contents
