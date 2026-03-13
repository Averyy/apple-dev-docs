---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.QuantizedEmbedding.html
---

# mlx.nn.QuantizedEmbedding

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.QuantizedEmbedding.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.QuantizedEmbedding

 Table of contents 

## Contents

# mlx.nn.QuantizedEmbedding

**class QuantizedEmbedding(*num_embeddings: int*, *dims: int*, *group_size: int = None*, *bits: int = None*, *mode: str = 'affine'*)**
: The same as [Embedding](mlx.nn.Embedding.html#mlx.nn.Embedding) but with a  quantized weight matrix.
[QuantizedEmbedding](#mlx.nn.QuantizedEmbedding) also provides a `from_embedding()`
classmethod to convert embedding layers to [QuantizedEmbedding](#mlx.nn.QuantizedEmbedding)
layers.

Parameters:

**num_embeddings** ([int](https://docs.python.org/3/library/functions.html#int)) – How many possible discrete tokens can we embed.
Usually called the vocabulary size.
**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the embeddings.
**group_size** (*Optional**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The group size to use for the quantized
weight. See [quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize). Default: `None`.
**bits** (*Optional**[*[int](https://docs.python.org/3/library/functions.html#int)*]*) – The bit width to use for the quantized weight.
See [quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize). Default: `None`.
**mode** ([str](https://docs.python.org/3/library/stdtypes.html#str)) – The quantization method to use (see
[mlx.core.quantize()](../../_autosummary/mlx.core.quantize.html#mlx.core.quantize)). Default: `"affine"`.

Methods

`as_linear`(x)
Call the quantized embedding layer as a quantized linear layer.

`from_embedding`(embedding_layer[, ...])
Create a [QuantizedEmbedding](#mlx.nn.QuantizedEmbedding) layer from an [Embedding](mlx.nn.Embedding.html#mlx.nn.Embedding) layer.

** Contents
