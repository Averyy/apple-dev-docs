---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.hanning.html
---

# mlx.core.hanning

**

- [.rst](../../_sources/python/_autosummary/mlx.core.hanning.rst)
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

# mlx.core.hanning

 Table of contents 

## Contents

# mlx.core.hanning

**hanning(*M: int*, ***, *stream: Stream | ThreadLocalStream | Device | mlx.core.DeviceType | None = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Return the Hanning window.
The Hanning window is a taper formed by using a weighted cosine.

\[w(n) = 0.5 - 0.5 \cos\left(\frac{2\pi n}{M-1}\right)
 \qquad 0 \le n \le M-1\]

Parameters:
**M** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of points in the output window.

Returns:

The window, with the maximum value normalized to one (the value oneappears only if the number of samples is odd).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
