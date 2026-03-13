---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.view.html
---

# mlx.core.view

**

- [.rst](../../_sources/python/_autosummary/mlx.core.view.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.view

 Table of contents 

## Contents

# mlx.core.view

**view(*a: scalar | array*, *dtype: Dtype*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: View the array as a different type.
The output shape changes along the last axis if the input array’s
type and the input `dtype` do not have the same size.
Note: the view op does not imply that the input and output arrays share
their underlying data. The view only gaurantees that the binary
representation of each element (or group of elements) is the same.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)) – The data type to change to.

Returns:
The array with the new type.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
