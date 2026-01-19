---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.solve.html
---

# mlx.core.linalg.solve

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.solve.rst)
- **

.pdf

**

# mlx.core.linalg.solve

 Table of contents 

## Contents

# mlx.core.linalg.solve

**solve(*a: array*, *b: array*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the solution to a system of linear equations `AX = B`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
The unique solution to the system `AX = B`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
