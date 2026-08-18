---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.quantized_matmul.html
---

# mlx.core.quantized_matmul

**

- [.rst](../../_sources/python/_autosummary/mlx.core.quantized_matmul.rst)
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

# mlx.core.quantized_matmul

 Table of contents 

## Contents

# mlx.core.quantized_matmul

**quantized_matmul(*x: array*, *w: array*, */*, *scales: array*, *biases: array | None = None*, *transpose: bool = True*, *group_size: int | None = None*, *bits: int | None = None*, *mode: str = 'affine'*, ***, *stream: StreamOrDevice = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Perform the matrix multiplication with the quantized matrix `w`. The
quantization uses one floating point scale and bias per `group_size` of
elements. Each element in `w` takes `bits` bits and is packed in an
unsigned 32 bit integer.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array
**w** ([array](mlx.core.array.html#mlx.core.array)) – Quantized matrix packed in unsigned integers
**scales** ([array](mlx.core.array.html#mlx.core.array)) – The scales to use per `group_size` elements of `w`
**biases** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – The biases to use per `group_size`
elements of `w`. Default: `None`.
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

Returns:
The result of the multiplication of `x` with `w`.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
