---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.can_cast.html
---

# mlx.core.can_cast

**

- [.rst](../../_sources/python/_autosummary/mlx.core.can_cast.rst)
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

# mlx.core.can_cast

 Table of contents 

## Contents

# mlx.core.can_cast

**can_cast(*from_: array | Dtype*, *to: Dtype*) → [bool](https://docs.python.org/3/library/functions.html#bool)**
: Determine if one data type can be cast to another according to type
promotion rules.
`from_` can be cast to `to` if promoting the two together gives
back `to`.

Parameters:

**from** ([array](mlx.core.array.html#mlx.core.array)* or *[Dtype](mlx.core.Dtype.html#mlx.core.Dtype)) – The source array or dtype.
**to** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)) – The destination dtype.

Returns:
Whether the cast can be performed.

Return type:
[bool](https://docs.python.org/3/library/functions.html#bool)

** Contents
