---
source: MLX-Data
framework: MLX
url: https://ml-explore.github.io/mlx-data/build/html/python/_autosummary/mlx.data.files_from_tar.html
---

# mlx.data.files_from_tar

**

- [.rst](../../_sources/python/_autosummary/mlx.data.files_from_tar.rst)
- **

.pdf

**

# mlx.data.files_from_tar

 Table of contents 

## Contents

# mlx.data.files_from_tar

**mlx.data.files_from_tar(*tarfile: str*, *nested: bool = False*, *num_threads: int = 1*) → mlx.data._c.Buffer**
: Return the list of files contained in a tar archive.
If `nested` is true then the archive is indexed recursively ie
archives contained in the file are also indexed. Moreover in that case
the indexing can be parallelized using the argument `num_threads`

Parameters:

**tarfile** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The path to the tar archive to be indexed.
**nested** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Enable recursive indexing of archives in archives.
(default: False)
**num_threads** ([int](https://docs.python.org/3/library/functions.html#int)) – If nested archives are enabled then index the
nested archives in parallel using `num_threads` threads. (default: 1)

** Contents
