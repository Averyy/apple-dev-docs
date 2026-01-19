---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.rope.html
---

# mlx.core.fast.rope

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fast.rope.rst)
- **

.pdf

**

# mlx.core.fast.rope

 Table of contents 

## Contents

# mlx.core.fast.rope

**rope(*a: array*, *dims: int*, ***, *traditional: bool*, *base: float | None*, *scale: float*, *offset: int | array*, *freqs: array | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Apply rotary positional encoding to the input.

The input is expected to be at least 3D with shape `(B, *, T, D)` where:
`B` is the batch size.
`T` is the sequence length.
`D` is the feature dimension.

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – The input array.
**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The feature dimensions to be rotated. If the input feature
is larger than dims then the rest is left unchanged.
**traditional** ([bool](https://docs.python.org/3/library/functions.html#bool)) – If set to `True` choose the traditional
implementation which rotates consecutive dimensions.
**base** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The base used to compute angular frequency for
each dimension in the positional encodings. Exactly one of `base` and
`freqs` must be `None`.
**scale** ([float](https://docs.python.org/3/library/functions.html#float)) – The scale used to scale the positions.
**offset** ([int](https://docs.python.org/3/library/functions.html#int)* or *[array](mlx.core.array.html#mlx.core.array)) – The position offset to start at. If an
[array](https://docs.python.org/3/library/array.html#module-array) is given it can be a scalar or vector of `B`
offsets for each example in the batch.
**freqs** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – Optional frequencies to use with RoPE.
If set, the `base` parameter must be `None`. Default: `None`.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
