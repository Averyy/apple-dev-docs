---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Stream.line_reader_from_key.html
---

# mlx.data.Stream.line_reader_from_key

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Stream.line_reader_from_key.rst)
- **

.pdf

**

# mlx.data.Stream.line_reader_from_key

 Table of contents 

## Contents

# mlx.data.Stream.line_reader_from_key

**Stream.line_reader_from_key(*self: mlx.data._c.Stream*, *key: str*, *dst_key: str*, *from_memory: bool = False*, *unzip: bool = False*, *local_prefix: os.PathLike = ''*, *file_fetcher: mlx::data::core::FileFetcher = None*) → mlx.data._c.Stream**
: Read the file pointed to from the array at `key` and yield
the lines as separate samples in the stream in the `dst_key`.
This operation is similar to [stream_line_reader()](mlx.data.stream_line_reader.html#mlx.data.stream_line_reader) but
applied once for every sample in the stream and the samples
from the resulting stream are returned until exhaustion.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**dst_key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The key to put the lines into.
**from_memory** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Read the lines from the contents of the
array rather than treating the array as a filename. (default: False)
**unzip** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Treat the file or memory stream as a compressed
stream and decompress it on the fly. (default: false)
**local_prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use to read the files. (default: ‘’)
**file_fetcher** (*mlx.data.core.FileFetcher**, **optional*) – A file fetcher to
read the text files possibly from a remote location.

** Contents
