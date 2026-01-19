---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/buffers_streams_samples.html
---

# Buffers, Streams and Samples

**

- [.rst](_sources/buffers_streams_samples.rst)
- **

.pdf

**

# Buffers, Streams and Samples

 Table of contents 

## Contents

# Buffers, Streams and Samples

In MLX data there are three main concepts that you need to know about buffers,
streams and samples. For instance, [buffer_from_vector()](python/_autosummary/mlx.data.buffer_from_vector.html#mlx.data.buffer_from_vector) and
[stream_csv_reader()](python/_autosummary/mlx.data.stream_csv_reader.html#mlx.data.stream_csv_reader) return a buffer and stream respectively and
are often the beginning of a data pipeline written in MLX data.

## Samples

Before describing the buffers and streams we should mention what it is they
contain. In MLX data **samples** are dictionaries that map string keys to array
values. In C++ they are simply instances of `std::unordered_map<std::string,
std::shared_ptr<mlx::data::Array>>` or simply `mlx::data::Sample` and in
Python they are a dictionary from strings to anything that implements the
[buffer protocol](https://docs.python.org/3/c-api/buffer.md).

```
# This is a valid sample
sample = {"hello": np.array(0)}

# So is this because scalars are cast to scalar arrays
sample = {"scalar": 42}

# Strings can also be used, however, they will be represented in unicode.
sample = {"key": "value"}

# Most likely you would want to write it as bytes in the sample as follows
sample = {"key": b"path/to/my/file"}
sample = {"key": "value".encode("ascii")}
```

## Buffers

Buffers are an indexable container of samples. They have a known length and
they can be shuffled or accessed in random order. They can of course also be
iterated upon.

Buffers allow to define operations on their samples that create other buffers
lazily evaluated. For instance if we have a `Buffer` that
contains samples of image filenames, calling [Buffer.load_image()](python/_autosummary/mlx.data.Buffer.load_image.html#mlx.data.Buffer.load_image)
would create a buffer that loads the images **when accessed** and not in
advance in memory. For a full list of supported operations check out
`Buffer`.

The API of `Buffer` is mirrored in C++ and Python and it would be trivial to
port a pipeline from one to the other.

The easiest way to make a buffer is to use [buffer_from_vector()](python/_autosummary/mlx.data.buffer_from_vector.html#mlx.data.buffer_from_vector) which
makes a `Buffer` from a list of samples. It can be used for instance to
make a buffer from a list of files as follows:

```
from pathlib import Path

import mlx.data as dx

def files_and_classes(root: Path):
    """Load the files and classes from an image dataset that contains one folder per class."""
    images = list(root.rglob("*.jpg"))
    categories = [p.relative_to(root).parent.name for p in images]
    category_set = set(categories)
    category_map = {c: i for i, c in enumerate(sorted(category_set))}

    return [
        {
            "image": str(p.relative_to(root)).encode("ascii"),
            "category": c,
            "label": category_map[c]
        }
        for c, p in zip(categories, images)
    ]

dset = dx.buffer_from_vector(files_and_classes(Path("path/to/dataset)))
# We can now apply transformations to the dataset
```

## Streams

Often datasets are too big, stored remotely or are nested in ways that prevent
random access. This is what streams are for. A `Stream` is a potentially
infinite iterable of samples.

Similar to buffers, streams allow to define operations on their samples that
will be executed when the sample is accessed. Contrary to buffers, streams
allow nesting of streams. For instance, from a strem of filenames pointing to
csv files we can read these files line by line and return these in the stream.
This would be impossible to implement with a `Buffer` as we don’t know
how many lines each file would have prior to reading it.

Once again, the API of `Stream` is mirrored in C++ and Python and it would be
trivial to port a pipeline from one to the other.

The easiest way to make a stream is from file using [stream_csv_reader()](python/_autosummary/mlx.data.stream_csv_reader.html#mlx.data.stream_csv_reader)
and [stream_line_reader()](python/_autosummary/mlx.data.stream_line_reader.html#mlx.data.stream_line_reader) or from a `Buffer` by calling its
[Buffer.to_stream()](python/_autosummary/mlx.data.Buffer.to_stream.html#mlx.data.Buffer.to_stream) method.

Notably streams enable prefetching ([Stream.prefetch()](python/_autosummary/mlx.data.Stream.prefetch.html#mlx.data.Stream.prefetch)) for efficient
iteration. This prefetching is not deterministic. Continuing the example from above:

```
# We can define the rest of the processing pipeline using streams.
# 1. First shuffle the buffer
# 2. Make a stream
# 3. Batch and then prefetch
dset = (
    dset
    .shuffle()
    .to_stream()  # <-- making a stream from the shuffled buffer
    .batch(32)
    .prefetch(8, 4)  # <-- prefetch 8 batches using 4 threads
)

# Now we can iterate over dset
sample = next(dset)
```

If deterministic prefetching is required, [Buffer.ordered_prefetch()](python/_autosummary/mlx.data.Buffer.ordered_prefetch.html#mlx.data.Buffer.ordered_prefetch) can replace
[Buffer.to_stream()](python/_autosummary/mlx.data.Buffer.to_stream.html#mlx.data.Buffer.to_stream).

```
# We can define the rest of the processing pipeline using streams.
# 1. First shuffle the buffer
# 2. Make a stream
# 3. Batch and then prefetch
dset = (
    dset
    .shuffle()
    .batch(32)
    .ordered_prefetch(8, 4)  # <-- prefetch 8 batches in a stream using 4 threads
)

# Now we can iterate over dset
sample = next(dset)
```

** Contents
