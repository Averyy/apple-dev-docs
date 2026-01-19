---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.topk.html
---

# mlx.core.topk

**

- [.rst](../../_sources/python/_autosummary/mlx.core.topk.rst)
- **

.pdf

**

# mlx.core.topk

 Table of contents 

## Contents

# mlx.core.topk

**topk(*a: array*, */*, *k: int*, *axis: None | int = -1*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Returns the `k` largest elements from the input along a given axis.
The elements will not necessarily be in sorted order.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**k** ([int](https://docs.python.org/3/library/functions.html#int)) – `k` top elements to be returned
**axis** ([int](https://docs.python.org/3/library/functions.html#int)* or **None**, **optional*) – Optional axis to select over.
If `None`, this selects the top `k` elements over the
flattened array. If unspecified, it defaults to `-1`.

Returns:
The top `k` elements from the input.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
