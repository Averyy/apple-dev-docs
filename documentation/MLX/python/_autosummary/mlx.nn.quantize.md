---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.nn.quantize.html
---

# mlx.nn.quantize

**

- [.rst](../../_sources/python/_autosummary/mlx.nn.quantize.rst)
- **

.pdf

**

# mlx.nn.quantize

 Table of contents 

## Contents

# mlx.nn.quantize

**quantize(*model: Module*, *group_size: int = None*, *bits: int = None*, ***, *mode: str = 'affine'*, *quantize_input: bool = False*, *class_predicate: Callable[[str, Module], bool | dict] | None = None*)**
: Quantize the sub-modules of a module according to a predicate.
By default all layers that define a `to_quantized()` method will be
quantized. Both [Linear](../nn/_autosummary/mlx.nn.Linear.html#mlx.nn.Linear) and [Embedding](../nn/_autosummary/mlx.nn.Embedding.html#mlx.nn.Embedding) layers will be
quantized. The module is updated in-place.

Note
`quantize_input=True` is only supported for `"nvfp4"` and `"mxfp8"`
modes and [Linear](../nn/_autosummary/mlx.nn.Linear.html#mlx.nn.Linear) layers.

Parameters:

**model** ([Module](../nn/module.html#mlx.nn.Module)) – The model whose leaf modules may be quantized.
**group_size** (*Optional**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The quantization group size (see
[mlx.core.quantize()](mlx.core.quantize.html#mlx.core.quantize)). Default: `None`.
**bits** (*Optional**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The number of bits per parameter (see
[mlx.core.quantize()](mlx.core.quantize.html#mlx.core.quantize)). Default: `None`.
**mode** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The quantization method to use (see
[mlx.core.quantize()](mlx.core.quantize.html#mlx.core.quantize)). Default: `"affine"`.
**quantize_input** ([bool](https://docs.python.org/3/library/functions.html#bool)) – Whether to quantize activations. Default: `False`.
**class_predicate** (*Optional**[**Callable**]*) – A callable which receives the
[Module](../nn/module.html#mlx.nn.Module) path and [Module](../nn/module.html#mlx.nn.Module) itself and returns `True` or a
dict of params for `to_quantized` if it should be quantized and
`False` otherwise. If `None`, then all layers that define a
`to_quantized()` method are quantized. Default: `None`.

Example
Weight only quantization for all layers that define a `to_quantized()` method:
>>> import mlx.nn as nn
>>> nn.quantize(model, group_size=64, bits=4, mode="affine")

Weight and input quantization for all linear layers:
>>> predicate = lambda p, m: isinstance(m, nn.Linear)
>>> nn.quantize(model, mode="nvfp4", quantize_input=True, class_predicate=predicate)

** Contents
