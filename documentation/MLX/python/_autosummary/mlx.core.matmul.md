---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.matmul.html
---

# mlx.core.matmul

**

- [.rst](../../_sources/python/_autosummary/mlx.core.matmul.rst)
- **

.pdf

**

# mlx.core.matmul

 Table of contents 

## Contents

# mlx.core.matmul

**matmul(*a: array*, *b: array*, */*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Matrix multiplication.
Perform the (possibly batched) matrix multiplication of two arrays. This function supports
broadcasting for arrays with more than two dimensions.

If the first array is 1-D then a 1 is prepended to its shape to make it
a matrix. Similarly if the second array is 1-D then a 1 is appended to its
shape to make it a matrix. In either case the singleton dimension is removed
from the result.
A batched matrix multiplication is performed if the arrays have more than
2 dimensions.  The matrix dimensions for the matrix product are the last
two dimensions of each input.
All but the last two dimensions of each input are broadcast with one another using
standard numpy-style broadcasting semantics.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.

Returns:
The matrix product of `a` and `b`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
