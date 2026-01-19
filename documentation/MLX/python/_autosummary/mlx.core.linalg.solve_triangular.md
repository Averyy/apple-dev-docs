---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.solve_triangular.html
---

# mlx.core.linalg.solve_triangular

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.solve_triangular.rst)
- **

.pdf

**

# mlx.core.linalg.solve_triangular

 Table of contents 

## Contents

# mlx.core.linalg.solve_triangular

**solve_triangular(*a: array*, *b: array*, ***, *upper: bool = False*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Computes the solution of a triangular system of linear equations `AX = B`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**upper** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether the array is upper or lower
triangular. Default: `False`.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The unique solution to the system `AX = B`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
