---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Stream.csv_reader_from_key.html
---

# mlx.data.Stream.csv_reader_from_key

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Stream.csv_reader_from_key.rst)
- **

.pdf

**

# mlx.data.Stream.csv_reader_from_key

 Table of contents 

## Contents

# mlx.data.Stream.csv_reader_from_key

**Stream.csv_reader_from_key(*self: mlx.data._c.Stream*, *key: str*, *sep: str = '*, *'*, *quote: str = '"'*, *from_memory: bool = False*, *local_prefix: os.PathLike = ''*, *file_fetcher: mlx::data::core::FileFetcher = None*) → mlx.data._c.Stream**
: Read the csv file pointed to from the array at `key` and
yield the contents as separate samples in the stream.
This operation is similar to [stream_csv_reader()](mlx.data.stream_csv_reader.html#mlx.data.stream_csv_reader) but
applied once for every sample in the stream and the samples
from the resulting stream are returned until exhaustion.

Parameters:

**key** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key that contains the array we are operating on.
**sep** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The field separator in the csv file. (default: ‘,’)
**quote** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The quotation character in the csv file. (default: ‘”’)
**from_memory** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Read the csv from the contents of the
array rather than treating the array as a filename. (default: False)
**local_prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use to read the files. (default: ‘’)
**file_fetcher** (*mlx.data.core.FileFetcher**, **optional*) – A file fetcher to
read the csv files possibly from a remote location.

** Contents
