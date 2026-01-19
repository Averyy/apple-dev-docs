---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.Buffer.read_from_tar.html
---

# mlx.data.Buffer.read_from_tar

**

- [.rst](../../_sources/python/_autosummary/mlx.data.Buffer.read_from_tar.rst)
- **

.pdf

**

# mlx.data.Buffer.read_from_tar

 Table of contents 

## Contents

# mlx.data.Buffer.read_from_tar

**Buffer.read_from_tar(*self: mlx.data._c.Buffer*, *tarkey: str*, *ikey: str*, *okey: str*, *prefix: os.PathLike = ''*, *tar_prefix: os.PathLike = ''*, *from_key: bool = False*, *file_fetcher: mlx::data::core::FileFetcher = None*, *nested: bool = False*, *num_threads: int = 1*) → mlx.data._c.Buffer**
: Read data from tarfiles.
This function reads whole files from one or many tarfiles. It is
commonly used to read the data in memory before decoding them with
`load_image` or `load_video`.
`tarkey` can refer to a filename or a sample key that defines the tar
file name to load from. This function first indexes the whole tar so it
is most efficient when reading many files from each tar archive.
When reading nested tar archives (ie tar archives that contain tar
archives), we can parallelize the indexing process using the
`num_threads` argument.

Parameters:

**tarkey** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The path to the tar file or the sample key containing
the path to the tarfile based on the value of `from_key`.
**ikey** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key containing the file name to read from the
tar archive.
**okey** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The sample key to write the data to.
**prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use when **loading the files
from the tar archive**. (default: ‘’)
**tar_prefix** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The filepath prefix to use for the tar archive.
(default: ‘’)
**from_key** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True treat the sample value at `tarkey` as a
filename, otherwise treat `tarkey` as a filename. (default: False)
**file_fetcher** (*mlx.data.core.FileFetcher**, **optional*) – A file fetcher to
read the tar files possibly from a remote location.
**nested** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If True then process nested tar files as folder and
expand them inline. (default: False)
**num_threads** ([int](https://docs.python.org/3/library/functions.html#int)) – When `nested` is True use that many parallel
threads to index the nested archives. (default: 1)

** Contents
