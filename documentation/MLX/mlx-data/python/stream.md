---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/stream.html
---

# Stream

**

- [.rst](../_sources/python/stream.rst)
- **

.pdf

**

# Stream

 Table of contents 

## Contents

# Stream

Using a `Stream` in python should feel like accessing an iterator of
samples. Only the next sample can be fetched and the iteration may be restarted
depending on the underlying source of the data (some trully online sources are
not resettable).

```
import mlx.data as dx

# The samples are never all instantiated
numbers = dx.stream_python_iterable(lambda: ({"x": i} for i in range(10**10)))

# Filtering is done with transforms returning an empty sample
evens = numbers.sample_transform(lambda s: s if s["x"] % 2 == 0 else dict())

print(next(numbers))
# prints {'x': array(0)}
print(next(numbers))
# prints {'x': array(1)}

# Streams are pointers to the streams so evens is using numbers under the
# hood. Since numbers was advanced now evens is advanced as well.
print(next(evens))
# prints {'x': array(2)}
print(next(evens))
# prints {'x': array(4)}
print(next(numbers))
# prints {'x': array(5)}

# Streams can be reset.
evens.reset()
print(next(evens))
print(next(evens))
print(next(numbers))
# prints {'x': array(0)}
#        {'x': array(2)}
#        {'x': array(3)}
```

## Factory methods

We provide the following factory methods to create a stream. When used from
python the most interesting one is probably [stream_python_iterable()](_autosummary/mlx.data.stream_python_iterable.html#mlx.data.stream_python_iterable). Of
course another good strategy is to start from a `Buffer` that you then
cast to a stream using [Buffer.to_stream()](_autosummary/mlx.data.Buffer.to_stream.html#mlx.data.Buffer.to_stream).

| stream_csv_reader(file, sep, quote, *, ...) | Stream samples from a csv file. |
| --- | --- |
| stream_csv_reader_from_string(content[, ...]) | Stream samples from a csv file provided as a string. |
| stream_line_reader(file, key, unzip, *, ...) | Stream lines from a file. |
| stream_python_iterable(iterable_factory) | Stream samples from a python iterable. |

## Stream specific API

`Stream` has a more powerful API than `Buffer`. It does not allow
for random access, however, it allows for stream composing and prefetching.
Stream composing is when a sample becomes the beginning of a new stream that
can have arbitrary length.

Streams also allow for filtering using the provided functions or a
`Stream.sample_transform()` that returns an empty dictionary (an empty
Sample).

| Stream.csv_reader_from_key(self, key, sep, ...) | Read the csv file pointed to from the array atkeyand yield the contents as separate samples in the stream. |
| --- | --- |
| Stream.line_reader_from_key(self, key, ...) | Read the file pointed to from the array atkeyand yield the lines as separate samples in the stream in thedst_key. |
| Stream.dynamic_batch(self, buffer_size, key) | Dynamic batching returns batches with approximately the same number of total elements. |
| Stream.partition(self, num_partitions, partition) | For everynum_partitionsconsecutive samples return thepartition-th. |
| Stream.buffered(self, buffer_size, ...) | Gather a buffer of samples, apply a function on the buffer and then iterate over the buffer samples. |
| Stream.repeat(self, num_time) | Reset the streamnum_timetimes before declaring it exhausted. |
| Stream.shuffle(self, buffer_size) | Shuffle the contents of the stream using a shuffle buffer. |
| Stream.sliding_window(self, key, size, stride) | Creates sample by sliding a window over the array atkey. |
| Stream.prefetch(self, prefetch_size, num_threads) | Fetch samples in background threads. |

** Contents
