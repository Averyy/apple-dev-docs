---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.SinusoidalPositionalEncoding.html
---

# mlx.nn.SinusoidalPositionalEncoding

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.SinusoidalPositionalEncoding.rst)
- **

.pdf

**

**
**
**

**

# mlx.nn.SinusoidalPositionalEncoding

 Table of contents 

## Contents

# mlx.nn.SinusoidalPositionalEncoding

**class SinusoidalPositionalEncoding(*dims: int*, *min_freq: float = 0.0001*, *max_freq: float = 1*, *scale: float | None = None*, *cos_first: bool = False*, *full_turns: bool = False*)**
: Implements sinusoidal positional encoding.
For more details see the paper [Attention Is All You Need](https://arxiv.org/abs/1706.03762).

Parameters:

**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The dimensionality of the resulting positional embeddings.
**min_freq** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The minimum frequency expected. Default:
`0.0001`.
**max_freq** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – The maximum frequency expected. Default:
`1`.
**scale** ([float](https://docs.python.org/3/library/functions.html#float)*, **optional*) – A multiplicative scale for the embeddings.
Default: `sqrt(2/dims)`.
**cos_first** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True` embed using `[cos(x); sin(x)]`
instead of the reverse. Default: `False`.
**full_turns** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – If `True` multiply the frequencies with
\(2\pi\). Default: `False`.

Methods

** Contents
