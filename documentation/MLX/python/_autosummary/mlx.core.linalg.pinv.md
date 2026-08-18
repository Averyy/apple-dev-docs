---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.linalg.pinv.html
---

# mlx.core.linalg.pinv

**

- [.rst](../../_sources/python/_autosummary/mlx.core.linalg.pinv.rst)
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

# mlx.core.linalg.pinv

 Table of contents 

## Contents

# mlx.core.linalg.pinv

**pinv(*a: array*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Compute the (Moore-Penrose) pseudo-inverse of a matrix.
This function calculates a generalized inverse of a matrix using its
singular-value decomposition. This function supports arrays with at least 2 dimensions.
When the input has more than two dimensions, the inverse is computed for each
matrix in the last two dimensions of `a`.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**stream** ([Stream](stream_class.html#mlx.core.Stream)*, **optional*) – Stream or device. Defaults to `None`
in which case the default stream of the default device is used.

Returns:
`aplus` such that `a @ aplus @ a = a`

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
