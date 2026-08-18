---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.eye.html
---

# mlx.core.eye

**

- [.rst](../../_sources/python/_autosummary/mlx.core.eye.rst)
- **

.pdf

**

**
**
**

- **System Settings
- **Light
- **Dark

**

# mlx.core.eye

 Table of contents 

## Contents

# mlx.core.eye

**eye(*n: int*, *m: int | None = None*, *k: int = 0*, *dtype: Dtype | None = float32*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Create an identity matrix or a general diagonal matrix.

Parameters:

**n** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of rows in the output.
**m** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of columns in the output. Defaults to n.
**k** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Index of the diagonal. Defaults to 0 (main diagonal).
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – Data type of the output array. Defaults to float32.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to None.

Returns:
An array where all elements are equal to zero, except for the k-th diagonal, whose values are equal to one.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
