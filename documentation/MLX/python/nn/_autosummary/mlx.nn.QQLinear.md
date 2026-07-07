---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.QQLinear.html
---

# mlx.nn.QQLinear

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.QQLinear.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.QQLinear

 Table of contents 

## Contents

# mlx.nn.QQLinear

**class QQLinear(*input_dims: int*, *output_dims: int*, *group_size: int = None*, *bits: int = None*, *mode: str = 'nvfp4'*)**
: Quantizes the input and applies an affine transformation using quantized weights.
Two use cases are supported:

**Eval**:  The weights are frozen and stored in quantized form together with
their scales (`self.weight` is quantized and `self.scales` is provided).

**Train**: The weights are stored in higher precision and are quantized onthe fly during computation so that gradients with respect to the weights
can be computed.

To switch between the two cases, use `layer.eval()` and `layer.train()` respectively.
Compared to the [mlx.nn.QuantizedLinear](mlx.nn.QuantizedLinear.html#mlx.nn.QuantizedLinear) layer, this layer
quantizes the input as well and includes weights in gradient computations.
[QQLinear](#mlx.nn.QQLinear) also provides the class method `from_linear()` to
convert [mlx.nn.Linear](mlx.nn.Linear.html#mlx.nn.Linear) layers to [QQLinear](#mlx.nn.QQLinear) layers.
Note: This layer does not support a bias term yet.

Parameters:

**input_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the input features.
**output_dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the output features.
**group_size** (*Optional**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The group size to use for the quantized weight.
See [quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize). Default: `None`.
**bits** (*Optional**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The bit width to use for the quantized weight.
See [quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize). Default: `None`.
**mode** (*Optional**[*[str](https://docs.python.org/3/library/stdtypes.html#str)*]*) – The quantization method to use (see
[mlx.core.quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize)). Currently, only `"nvfp4"` and `"mxfp8"`
are supported. Default: `"nvfp4"`.

Methods

`dequantize`()

`from_linear`(linear_layer[, group_size, ...])
Create a [QQLinear](#mlx.nn.QQLinear) layer from a [Linear](mlx.nn.Linear.html#mlx.nn.Linear) layer.

`quantize`()

** Contents
