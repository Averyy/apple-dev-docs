---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Stream.shuffle.html
---

# mlx.data.Stream.shuffle

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Stream.shuffle.rst)
- **

.pdf

**

# mlx.data.Stream.shuffle

 Table of contents 

## Contents

# mlx.data.Stream.shuffle

**Stream.shuffle(*self: mlx.data._c.Stream*, *buffer_size: int*) → mlx.data._c.Stream**
: Shuffle the contents of the stream using a shuffle buffer.
A buffer of size `buffer_size` is filled with samples and
then a random sample is returned from the buffer and replaced
with a new one from the stream.
This can achieve better shuffling than using
[Stream.buffered()](mlx.data.Stream.buffered.html#mlx.data.Stream.buffered) and then [Buffer.shuffle()](mlx.data.Buffer.shuffle.html#mlx.data.Buffer.shuffle) because
it is not bucketing the stream and a sample is a random sample
from the first to the current sample of the underlying stream.
To showcase the difference, the example below shuffles a stream
of 100 numbers with a buffer of size 10 and measures the
distance that a number moved from its original location.
import mlx.data as dx

numbers = dx.stream_python_iterable(lambda: (dict(x=i) for i in range(100)))
buffer_shuffle = numbers.buffered(10, lambda: buff.shuffle())
shuffle = numbers.shuffle(10)

numbers.reset()
print([abs(i-s["x"].item()) for i, s in enumerate(buffer_shuffle)])
# All printed numbers above are smaller than 10

numbers.reset()
print([abs(i-s["x"].item()) for i, s in enumerate(shuffle)])
# The numbers can be up to i+10 which means that the first
# element could even be yielded last!

Parameters:
**buffer_size** ([int](https://docs.python.org/3/library/functions.html#int)) – How big should the shuffle buffer be.

** Contents
