---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.hadamard_transform.html
---

# mlx.core.hadamard_transform

**

- [.rst](../../_sources/python/_autosummary/mlx.core.hadamard_transform.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.hadamard_transform

 Table of contents 

## Contents

# mlx.core.hadamard_transform

**hadamard_transform(*a: array*, *scale: float | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Perform the Walsh-Hadamard transform along the final axis.
Equivalent to:
from scipy.linalg import hadamard

y = (hadamard(len(x)) @ x) * scale

Supports sizes `n = m*2^k` for `m` in `(1, 12, 20, 28)` and `2^k
<= 8192` for float32 and `2^k <= 16384` for float16/bfloat16.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**scale** ([float](https://docs.python.org/3/library/functions.html#float)) – Scale the output by this factor.
Defaults to `1/sqrt(a.shape[-1])` so that the Hadamard matrix is orthonormal.

Returns:
The transformed array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
