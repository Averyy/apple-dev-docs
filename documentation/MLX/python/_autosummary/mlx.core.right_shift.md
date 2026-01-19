---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.right_shift.html
---

# mlx.core.right_shift

**

- [.rst](../../_sources/python/_autosummary/mlx.core.right_shift.rst)
- **

.pdf

**

# mlx.core.right_shift

 Table of contents 

## Contents

# mlx.core.right_shift

**right_shift(*a: scalar | array*, *b: scalar | array*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Element-wise right shift.
Shift the bits of the first input to the right by the second using
numpy-style broadcasting semantics. Either or both input arrays can
also be scalars.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.

Returns:
The bitwise right shift `a >> b`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
