---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Embedding.html
---

# mlx.nn.Embedding

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Embedding.rst)
- **

.pdf

**

# mlx.nn.Embedding

 Table of contents 

## Contents

# mlx.nn.Embedding

**class Embedding(*num_embeddings: int*, *dims: int*)**
: Implements a simple lookup table that maps each input integer to a
high-dimensional vector.
Typically used to embed discrete tokens for processing by neural networks.

Parameters:

**num_embeddings** ([int](https://docs.python.org/3/library/functions.html#int)) – How many possible discrete tokens can we embed.
Usually called the vocabulary size.
**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the embeddings.

Methods

`as_linear`(x)
Call the embedding layer as a linear layer.

`to_quantized`([group_size, bits, mode, ...])
Return a [QuantizedEmbedding](mlx.nn.QuantizedEmbedding.html#mlx.nn.QuantizedEmbedding) layer that approximates this embedding layer.

** Contents
