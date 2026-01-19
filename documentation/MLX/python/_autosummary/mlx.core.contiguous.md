---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.contiguous.html
---

# mlx.core.contiguous

**

- [.rst](../../_sources/python/_autosummary/mlx.core.contiguous.rst)
- **

.pdf

**

# mlx.core.contiguous

 Table of contents 

## Contents

# mlx.core.contiguous

**contiguous(*a: array*, */*, *allow_col_major: bool = False*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Force an array to be row contiguous. Copy if necessary.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input to make contiguous
**allow_col_major** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Consider column major as contiguous and don’t copy

Returns:
The row or col contiguous output.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
