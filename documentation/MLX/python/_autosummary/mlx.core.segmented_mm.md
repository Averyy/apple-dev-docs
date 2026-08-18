---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.segmented_mm.html
---

# mlx.core.segmented_mm

**

- [.rst](../../_sources/python/_autosummary/mlx.core.segmented_mm.rst)
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

# mlx.core.segmented_mm

 Table of contents 

## Contents

# mlx.core.segmented_mm

**segmented_mm(*a: array*, *b: array*, */*, *segments: array*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Perform a matrix multiplication but segment the inner dimension and
save the result for each segment separately.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array of shape `MxK`.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array of shape `KxN`.
**segments** ([array](mlx.core.array.html#mlx.core.array)) – The offsets into the inner dimension for each segment.

Returns:
The result per segment of shape `MxN`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
