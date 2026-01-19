---
source: MLX-Data
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.stream_csv_reader_from_string.html
---

# mlx.data.stream_csv_reader_from_string

**

- [.rst](../../_sources/python/_autosummary/mlx.data.stream_csv_reader_from_string.rst)
- **

.pdf

**

# mlx.data.stream_csv_reader_from_string

 Table of contents 

## Contents

# mlx.data.stream_csv_reader_from_string

**mlx.data.stream_csv_reader_from_string(*content: str*, *sep: str = ','*, *quote: str = '"'*) → mlx.data._c.Stream**
: Stream samples from a csv file provided as a string.
The same can be achieved with [stream_csv_reader()](mlx.data.stream_csv_reader.html#mlx.data.stream_csv_reader) and using an
`io.StringIO` object as follows:
from io import StringIO
import mlx.data as dx

# dset1 and dset2 are exactly the same.
my_csv_string = "... csv content here ..."
dset1 = dx.stream_csv_reader_from_string(my_csv_string)
dset2 = dx.stream_csv_reader(StringIO(my_csv_string))

Parameters:

**content** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The string containing the content of a csv file.
**sep** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The field separator in the csv file. (default: ‘,’)
**quote** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The quotation character in the csv file. (default: ‘”’)

** Contents
