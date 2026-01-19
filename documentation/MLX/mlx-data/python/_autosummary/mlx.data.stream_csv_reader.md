---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.stream_csv_reader.html
---

# mlx.data.stream_csv_reader

**

- [.rst](../../_sources/python/_autosummary/mlx.data.stream_csv_reader.rst)
- **

.pdf

**

# mlx.data.stream_csv_reader

 Table of contents 

## Contents

# mlx.data.stream_csv_reader

**mlx.data.stream_csv_reader(*file: object*, *sep: str = '*, *'*, *quote: str = '"'*, ***, *local_prefix: str = ''*, *file_fetcher: mlx::data::core::FileFetcher = None*, *file_fetcher_handle: mlx::data::core::FileFetcherHandle = None*) → mlx.data._c.Stream**
: Stream samples from a csv file.
The file can be given as a filename or any python object that has a
`read()` and a `seek()` method. Optionally a file fetcher can be
passed to fetch the file from a remote location.
In the case that a file object was created from a file fetched by an MLX
file fetcher, then a handle can be passed (the return value of fetch) to
ensure that the file is kept on disk for the lifetime of the stream.

Parameters:

**file** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or **python readable object*) – The file to read the csv from.
**sep** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The field separator in the csv file. (default: ‘,’)
**quote** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The quotation character in the csv file. (default: ‘”’)
**local_prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use to read the files. (default: ‘’)
**file_fetcher** (*mlx.data.core.FileFetcher**, **optional*) – A file fetcher to
read the csv files possibly from a remote location.
**file_fetcher_handle** (*mlx.data.core.FileFetcherHandle**, **optional*) – A
handle to ensure that the file is kept on disk if a stream is
passed instead of a filename.

** Contents
