---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.hamming.html
---

# mlx.core.hamming

**

- [.rst](../../_sources/python/_autosummary/mlx.core.hamming.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.hamming

 Table of contents 

## Contents

# mlx.core.hamming

**hamming(*M: int*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the Hamming window.
The Hamming window is a taper formed by using a weighted cosine.

\[w(n) = 0.54 - 0.46 \cos\left(\frac{2\pi n}{M-1}\right)
\qquad 0 \le n \le M-1\]

Parameters:
**M** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of points in the output window.

Returns:

The window, with the maximum value normalized to one (the value oneappears only if the number of samples is odd).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
