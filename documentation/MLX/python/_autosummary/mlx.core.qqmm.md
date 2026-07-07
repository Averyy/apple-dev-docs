---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.qqmm.html
---

# mlx.core.qqmm

**

- [.rst](../../_sources/python/_autosummary/mlx.core.qqmm.rst)
- **

.pdf

**

**
**
**

**

# mlx.core.qqmm

 Table of contents 

## Contents

# mlx.core.qqmm

**qqmm(*x: array*, *w: array*, *scales: array | None = None*, *group_size: int | None = None*, *bits: int | None = None*, *mode: str = 'nvfp4'*, *global_scale_x: array | None = None*, *global_scale_w: array | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Perform a matrix multiplication using a possibly quantized weight matrix
`w` and a non-quantized input `x`. The input `x` is quantized on the
fly. The weight matrix `w` is used as-is if it is already quantized;
otherwise, it is quantized on the fly.
If `w` is quantized, `scales` must be provided, and `group_size`,
`bits`, and `mode` must match the parameters that were used to quantize
`w`.
Notes
If `w` is expected to receive gradients, it must be provided in
non-quantized form.
If `x` and w` are not quantized, their data types must be `float32`,
`float16`, or `bfloat16`.
If `w` is quantized, it must be packed in unsigned integers.
`global_scale_x` and `global_scale_w` are only used for `nvfp4` quantization.

Parameters:

**x** ([array](mlx.core.array.html#mlx.core.array)) – Input array.
**w** ([array](mlx.core.array.html#mlx.core.array)) – Weight matrix. If quantized, it is packed in unsigned integers.
**scales** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – The scales to use per `group_size` elements of
`w` if `w` is quantized. Default: `None`.
**group_size** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Number of elements in `x` and `w` that
share a scale. See supported values and defaults in the
[table of quantization modes](mlx.core.quantize.html#quantize-modes). Default: `None`.
**bits** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – Number of bits used to represent each element of
`x` and `w`. See supported values and defaults in the
[table of quantization modes](mlx.core.quantize.html#quantize-modes). Default: `None`.
**mode** ([str](https://docs.python.org/3/library/stdtypes.html#str)*, **optional*) – The quantization mode. Default: `"nvfp4"`.
Supported modes are `nvfp4` and `mxfp8`. See the
[table of quantization modes](mlx.core.quantize.html#quantize-modes) for details.
**global_scale** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – The per-input float32 scale used for x
with `"nvfp4"` quantization. Default: `None`.
**global_scale_w** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – The per-input float32 scale used for w
with `"nvfp4"` quantization. Default: `None`.

Returns:
The result of the multiplication of quantized `x` with quantized `w`.
needed).

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
