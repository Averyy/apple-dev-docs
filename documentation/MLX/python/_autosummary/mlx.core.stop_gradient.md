---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.stop_gradient.html
---

# mlx.core.stop_gradient

**

- [.rst](../../_sources/python/_autosummary/mlx.core.stop_gradient.rst)
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

# mlx.core.stop_gradient

 Table of contents 

## Contents

# mlx.core.stop_gradient

**stop_gradient(*a: array*, */*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Stop gradients from being computed.
The operation is the identity but it prevents gradients from flowing
through the array.

Parameters:
**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.

Returns:
The unchanged input `a` but without gradient flowing
through it.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
