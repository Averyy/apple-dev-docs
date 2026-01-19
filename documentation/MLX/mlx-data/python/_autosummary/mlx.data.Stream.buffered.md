---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Stream.buffered.html
---

# mlx.data.Stream.buffered

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Stream.buffered.rst)
- **

.pdf

**

# mlx.data.Stream.buffered

 Table of contents 

## Contents

# mlx.data.Stream.buffered

**Stream.buffered(*self: mlx.data._c.Stream, buffer_size: int, on_refill: Optional[Callable[[mlx::data::Buffer], mlx::data::Buffer]] = None, num_threads: int = 1*) → mlx.data._c.Stream**
: Gather a buffer of samples, apply a function on the buffer and
then iterate over the buffer samples.
This function can be used to implement any logic that requires
a buffer of samples. For instance it can be used for pseudo
shuffling by shuffling the buffer or sorting the buffer based
on sequence lengths to minimize padding and wasted computation.

Note
Shuffling the buffer is not the same as a shuffle buffer.
In a shuffle buffer of size 1000 the 500th element
is a random choice in the range 0-1500 while here it would
be a random choice in the range 0-1000. If you need a
shuffle buffer use [Stream.shuffle()](mlx.data.Stream.shuffle.html#mlx.data.Stream.shuffle) .

The following examples demonstrate the use of `buffered`.
# Pseudo shuffling
dset = dset.buffered(10000, lambda buff: buff.shuffle(), num_threads=8)

# Sort by the length of samples in order to minimize padding when batching.
# You might also want to check out `dynamic_batch`
def sort_by_length(buff):
    perm = sorted(range(len(buff)), key=len(buff[i]["x"]))
    return buff.perm(perm)
dset = dset.buffered(128 * batch_size, sort_by_length, num_threads=8)

Parameters:

**buffer_size** ([int](https://docs.python.org/3/library/functions.html#int)) – How big should the buffer be.
**on_refill** (*callable**, **optional*) – The function to apply to the buffer. (default: identity)
**num_threads** ([int](https://docs.python.org/3/library/functions.html#int)) – How many parallel threads to use when filling the buffer. (default: 1)

** Contents
