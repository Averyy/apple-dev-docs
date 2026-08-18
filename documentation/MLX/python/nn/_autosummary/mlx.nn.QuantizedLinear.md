---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.QuantizedLinear.html
---

# mlx.nn.QuantizedLinear

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.QuantizedLinear.rst)
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

# mlx.nn.QuantizedLinear

 Table of contents 

## Contents

# mlx.nn.QuantizedLinear

**class QuantizedLinear(*input_dims: int*, *output_dims: int*, *bias: bool = True*, *group_size: int = None*, *bits: int = None*, *mode: str = 'affine'*)**
: Applies an affine transformation to the input using a quantized weight matrix.
It is the quantized equivalent of [mlx.nn.Linear](mlx.nn.Linear.html#mlx.nn.Linear). For now its
parameters are frozen and will not be included in any gradient computation
but this will probably change in the future.
[QuantizedLinear](#mlx.nn.QuantizedLinear) also provides a classmethod `from_linear()` to
convert linear layers to [QuantizedLinear](#mlx.nn.QuantizedLinear) layers.

Parameters:

**input_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the input features.
**output_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the output features.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If set to `False` then the layer will not use
a bias. Default: `True`.
**group_size** (*Optional**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The group size to use for the quantized
weight. See [quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize). Default: `None`.
**bits** (*Optional**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The bit width to use for the quantized weight.
See [quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize). Default: `None`.
**mode** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The quantization method to use (see
[mlx.core.quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize)). Default: `"affine"`.

Methods

`from_linear`(linear_layer[, group_size, ...])
Create a [QuantizedLinear](#mlx.nn.QuantizedLinear) layer from a [Linear](mlx.nn.Linear.html#mlx.nn.Linear) layer.

** Contents
