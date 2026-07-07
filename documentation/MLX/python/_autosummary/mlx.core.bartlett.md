---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.bartlett.html
---

# mlx.core.bartlett

**

- [.rst](../../_sources/python/_autosummary/mlx.core.bartlett.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.bartlett

 Table of contents 

## Contents

# mlx.core.bartlett

**bartlett(*M: int*, ***, *stream: Stream | mlx.core.ThreadLocalStream | Device | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the Bartlett window.
The Bartlett window is a taper formed by using a weighted cosine.

\[w(n) = 1 - \frac{2|n - (M-1)/2|}{M-1}
 \qquad 0 \le n \le M-1\]

Parameters:
**M** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of points in the output window.

Returns:

The window, with the maximum value normalized to one (the value oneappears only if the number of samples is odd).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
