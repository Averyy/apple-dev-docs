---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.tri.html
---

# mlx.core.tri

**

- [.rst](../../_sources/python/_autosummary/mlx.core.tri.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.tri

 Table of contents 

## Contents

# mlx.core.tri

**tri(*n: int*, *m: int*, *k: int*, *dtype: Dtype | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: An array with ones at and below the given diagonal and zeros elsewhere.

Parameters:

**n** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of rows in the output.
**m** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of cols in the output. Defaults to `None`.
**k** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The diagonal of the 2-D array. Defaults to `0`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Data type of the output array. Defaults to `float32`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`.

Returns:
Array with its lower triangle filled with ones and zeros elsewhere

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
