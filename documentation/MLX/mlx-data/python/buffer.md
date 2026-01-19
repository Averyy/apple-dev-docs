---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/buffer.html
---

# Buffer

**

- [.rst](../_sources/python/buffer.rst)
- **

.pdf

**

# Buffer

 Table of contents 

## Contents

# Buffer

As also mentioned in [Buffers, Streams and Samples](../buffers_streams_samples.html#buffers-streams-samples)
a `Buffer` is an indexable container of
samples. Using a buffer in python should feel very similar to accessing a list
of samples.

```
import mlx.data as dx

numbers = dx.buffer_from_vector([{"x": i} for i in range(10)])
evens = numbers.key_transform("x", lambda x: 2*x)

print(evens)
# prints Buffer(size=10, keys={'x'})

print(evens[3])
# prints {'x': array(6)}

print(len(evens))
# prints 10
```

## Factory methods

We provide the following factory methods to create a buffer.

| buffer_from_vector(data) | Make a buffer from a list of dictionaries. |
| --- | --- |
| files_from_tar(tarfile[, nested, num_threads]) | Return the list of files contained in a tar archive. |

## Buffer specific API

The random access characteristics of a `Buffer` allow us to define some
transformations that cannot be implemented or do not make sense for a
`Stream`.

| Buffer.ordered_prefetch(self, prefetch_size, ...) | Fetch samples in background threads, while preserving original ordering. |
| --- | --- |
| Buffer.partition(self, num_partitions, partition) | Equivalent to slicing the buffer with a step equal tonum_partitionsand starting offset ofpartition. |
| Buffer.perm(self, perm) | Arbitrarily reorder the buffer with the provided indices. |
| Buffer.shuffle(self) | Create a random permutation of equal size to the buffer and apply it thus shuffling the buffer. |
| Buffer.to_stream(self) | Make a stream that yields the elements of the buffer. |

** Contents
