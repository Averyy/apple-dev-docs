---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.diag.html
---

# mlx.core.diag

**

- [.rst](../../_sources/python/_autosummary/mlx.core.diag.rst)
- **

.pdf

**

# mlx.core.diag

 Table of contents 

## Contents

# mlx.core.diag

**diag(*a: array*, */*, *k: int = 0*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Extract a diagonal or construct a diagonal matrix.
If `a` is 1-D then a diagonal matrix is constructed with `a` on the
\(k\)-th diagonal. If `a` is 2-D then the \(k\)-th diagonal is
returned.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – 1-D or 2-D input array.
**k** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The diagonal to extract or construct.
Default: `0`.

Returns:
The extracted diagonal or the constructed diagonal matrix.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
