---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.blackman.html
---

# mlx.core.blackman

**

- [.rst](../../_sources/python/_autosummary/mlx.core.blackman.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.blackman

 Table of contents 

## Contents

# mlx.core.blackman

**blackman(*M: int*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the Blackman window.
The Blackman window is a taper formed by using the first three terms of a summation of cosines.

\[w(n) = 0.42 - 0.5 \cos\left(\frac{2\pi n}{M-1}\right) + 0.08 \cos\left(\frac{4\pi n}{M-1}\right)
 \qquad 0 \le n \le M-1\]

Parameters:
**M** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of points in the output window.

Returns:

The window, with the maximum value normalized to one (the value oneappears only if the number of samples is odd).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
