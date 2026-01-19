---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.Transformer.html
---

# mlx.nn.Transformer

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.Transformer.rst)
- **

.pdf

**

# mlx.nn.Transformer

 Table of contents 

## Contents

# mlx.nn.Transformer

**class Transformer(*dims: int = 512, num_heads: int = 8, num_encoder_layers: int = 6, num_decoder_layers: int = 6, mlp_dims: int | None = None, dropout: float = 0.0, activation: ~typing.Callable[[~typing.Any], ~typing.Any] = <mlx.gc_func object>, custom_encoder: ~typing.Any | None = None, custom_decoder: ~typing.Any | None = None, norm_first: bool = True, checkpoint: bool = False*)**
: Implements a standard Transformer model.
The implementation is based on [Attention Is All You Need](https://arxiv.org/abs/1706.03762).
The Transformer model contains an encoder and a decoder. The encoder
processes the input sequence and the decoder generates the output sequence.
The interaction between encoder and decoder happens through the attention
mechanism.

Parameters:

**dims** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of expected features in the
encoder/decoder inputs. Default: `512`.
**num_heads** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of attention heads. Default:
`8`.
**num_encoder_layers** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of encoder layers in the
Transformer encoder. Default: `6`.
**num_decoder_layers** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The number of decoder layers in the
Transformer decoder. Default: `6`.
**mlp_dims** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The hidden dimension of the MLP block in each
Transformer layer. Defaults to `4*dims` if not provided. Default:
`None`.
**dropout** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The dropout value for the Transformer
encoder and decoder. Dropout is used after each attention layer and
the activation in the MLP layer. Default: `0.0`.
**activation** (*function**, **optional*) – the activation function for the MLP
hidden layer. Default: [mlx.nn.relu()](../_autosummary_functions/mlx.nn.relu.html#mlx.nn.relu).
**custom_encoder** ([Module](../module.html#mlx.nn.Module)*, **optional*) – A custom encoder to replace the
standard Transformer encoder. Default: `None`.
**custom_decoder** ([Module](../module.html#mlx.nn.Module)*, **optional*) – A custom decoder to replace the
standard Transformer decoder. Default: `None`.
**norm_first** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – if `True`, encoder and decoder layers
will perform layer normalization before attention and MLP
operations, otherwise after. Default: `True`.
**checkpoint** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – if `True` perform gradient checkpointing
to reduce the memory usage at the expense of more computation.
Default: `False`.

Methods

** Contents
