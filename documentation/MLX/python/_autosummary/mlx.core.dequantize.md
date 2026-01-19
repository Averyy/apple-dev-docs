---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.dequantize.html
---

# mlx.core.dequantize

**

- [.rst](../../_sources/python/_autosummary/mlx.core.dequantize.rst)
- **

.pdf

**

# mlx.core.dequantize

 Table of contents 

## Contents

# mlx.core.dequantize

**dequantize(*w: array*, */*, *scales: array*, *biases: array | None = None*, *group_size: int | None = None*, *bits: int | None = None*, *mode: str = 'affine'*, *dtype: Dtype | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Dequantize the matrix `w` using quantization parameters.

Parameters:

**w** ([array](mlx.core.array.html#mlx.core.array)) – Matrix to be dequantized
**scales** ([array](mlx.core.array.html#mlx.core.array)) – The scales to use per `group_size` elements of `w`.
**biases** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – The biases to use per `group_size`
elements of `w`. Default: `None`.
**group_size** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The size of the group in `w` that shares a
scale and bias. See supported values and defaults in the
[table of quantization modes](mlx.core.quantize.html#quantize-modes). Default: `None`.
**bits** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of bits occupied by each element of
`w` in the quantized array. See supported values and defaults in the
[table of quantization modes](mlx.core.quantize.html#quantize-modes). Default: `None`.
**dtype** ([Dtype](mlx.core.Dtype.html#mlx.core.Dtype)*, **optional*) – The data type of the dequantized output. If
`None` the return type is inferred from the scales and biases
when possible and otherwise defaults to `bfloat16`.
Default: `None`.
**mode** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – The quantization mode. Default: `"affine"`.

Returns:
The dequantized version of `w`

Return type:
[array](mlx.core.array.html#mlx.core.array)

Notes
The currently supported quantization modes are `"affine"`,
`"mxfp4`, `"mxfp8"`, and `"nvfp4"`.
For `affine` quantization, given the notation in [quantize()](mlx.core.quantize.html#mlx.core.quantize),
we compute \(w_i\) from \(\hat{w_i}\) and corresponding \(s\)
and \(\beta\) as follows

\[w_i = s \hat{w_i} + \beta\]

** Contents
