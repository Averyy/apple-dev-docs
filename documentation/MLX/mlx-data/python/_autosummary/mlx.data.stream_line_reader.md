---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.stream_line_reader.html
---

# mlx.data.stream_line_reader

**

- [.rst](../../_sources/python/_autosummary/mlx.data.stream_line_reader.rst)
- **

.pdf

**

# mlx.data.stream_line_reader

 Table of contents 

## Contents

# mlx.data.stream_line_reader

**mlx.data.stream_line_reader(*file: object*, *key: str*, *unzip: bool = False*, ***, *local_prefix: str = ''*, *file_fetcher: mlx::data::core::FileFetcher = None*, *file_fetcher_handle: mlx::data::core::FileFetcherHandle = None*) → mlx.data._c.Stream**
: Stream lines from a file.
Similar to [stream_csv_reader()](mlx.data.stream_csv_reader.html#mlx.data.stream_csv_reader), a file can be a filename or a
python object with a `read()` and a `seek()`.

Note
The newline characters are **not** included in the samples.

Parameters:

**file** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or **python readable object*) – The file to read the csv from.
**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The destination key for the lines of the file.
**unzip** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Treat the file as a compressed stream and decompress it
on the fly. (default: False)
**local_prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use to read the files. (default: ‘’)
**file_fetcher** (*mlx.data.core.FileFetcher**, **optional*) – A file fetcher to
read the csv files possibly from a remote location.
**file_fetcher_handle** (*mlx.data.core.FileFetcherHandle**, **optional*) – A
handle to ensure that the file is kept on disk if a stream is
passed instead of a filename.

** Contents
