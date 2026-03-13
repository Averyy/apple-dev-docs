---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/usage/using_streams.html
---

# Using Streams

**

- [.rst](../_sources/usage/using_streams.rst)
- **

.pdf

**

**
**
**

**

# Using Streams

 Table of contents 

## Contents

# Using Streams

## Specifying theStream

All operations (including random number generation) take an optional
keyword argument `stream`. The `stream` kwarg specifies which
[Stream](../python/_autosummary/stream_class.html#mlx.core.Stream) the operation should run on. If the stream is unspecified then
the operation is run on the default stream of the default device:
`mx.default_stream(mx.default_device())`.  The `stream` kwarg can also
be a [Device](../python/_autosummary/mlx.core.Device.html#mlx.core.Device) (e.g. `stream=my_device`) in which case the operation is
run on the default stream of the provided device
`mx.default_stream(my_device)`.

** Contents
