---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.gather_qmm.html
---

# mlx.core.gather_qmm

**

- [.rst](../../_sources/python/_autosummary/mlx.core.gather_qmm.rst)
- **

.pdf

**

# mlx.core.gather_qmm

 Table of contents 

## Contents

# mlx.core.gather_qmm

**gather_qmm(*x: array*, *w: array*, */*, *scales: array*, *biases: array | None = None*, *lhs_indices: array | None = None*, *rhs_indices: array | None = None*, *transpose: bool = True*, *group_size: int | None = None*, *bits: int | None = None*, *mode: str = 'affine'*, ***, *sorted_indices: bool = False*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Perform quantized matrix multiplication with matrix-level gather.
This operation is the quantized equivalent to [gather_mm()](mlx.core.gather_mm.html#mlx.core.gather_mm).
Similar to [gather_mm()](mlx.core.gather_mm.html#mlx.core.gather_mm), the indices `lhs_indices` and
`rhs_indices` contain flat indices along the batch dimensions (i.e.
all but the last two dimensions) of `x` and `w` respectively.
Note that `scales` and `biases` must have the same batch dimensions
as `w` since they represent the same quantized matrix.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**w** ([array](mlx.core.array.html#mlx.core.array)) – Quantized matrix packed in unsigned integers
**scales** ([array](mlx.core.array.html#mlx.core.array)) – The scales to use per `group_size` elements of `w`
**biases** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – The biases to use per `group_size`
elements of `w`. Default: `None`.
**lhs_indices** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – Integer indices for `x`. Default: `None`.
**rhs_indices** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – Integer indices for `w`. Default: `None`.
**transpose** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Defines whether to multiply with the
transposed `w` or not, namely whether we are performing
`x @ w.T` or `x @ w`. Default: `True`.
**group_size** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The size of the group in `w` that shares a
scale and bias. See supported values and defaults in the
[table of quantization modes](mlx.core.quantize.html#quantize-modes). Default: `None`.
**bits** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of bits occupied by each element of
`w` in the quantized array. See supported values and defaults in the
[table of quantization modes](mlx.core.quantize.html#quantize-modes). Default: `None`.
**mode** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – The quantization mode. Default: `"affine"`.
**sorted_indices** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – May allow a faster implementation
if the passed indices are sorted. Default: `False`.

Returns:

The result of the multiplication of `x` with `w`after gathering using `lhs_indices` and `rhs_indices`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
