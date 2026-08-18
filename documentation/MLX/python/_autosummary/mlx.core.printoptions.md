---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.printoptions.html
---

# mlx.core.printoptions

**

- [.rst](../../_sources/python/_autosummary/mlx.core.printoptions.rst)
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

# mlx.core.printoptions

 Table of contents 

## Contents

# mlx.core.printoptions

**printoptions(*precision: int = -1*) → mlx.core._PrintOptionsContext**
: Context manager for setting print options temporarily.
Example
>>> print(x)  # Uses default precision
>>> with mx.printoptions(precision=3):
>>>     print(x)  # Uses precision of 3
>>> print(x)  # Back to default precision

Parameters:
**precision** ([int](https://docs.python.org/3/library/functions.html#int)) – Number of decimal places. Use -1 for default

** Contents
