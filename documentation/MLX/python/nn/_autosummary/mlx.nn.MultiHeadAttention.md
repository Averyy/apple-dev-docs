---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/nn/_autosummary/mlx.nn.MultiHeadAttention.html
---

# mlx.nn.MultiHeadAttention

**

- [.rst](../../../_sources/python/nn/_autosummary/mlx.nn.MultiHeadAttention.rst)
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

# mlx.nn.MultiHeadAttention

 Table of contents 

## Contents

# mlx.nn.MultiHeadAttention

**class MultiHeadAttention(*dims: int*, *num_heads: int*, *query_input_dims: int | None = None*, *key_input_dims: int | None = None*, *value_input_dims: int | None = None*, *value_dims: int | None = None*, *value_output_dims: int | None = None*, *bias: bool = False*)**
: Implements the scaled dot product attention with multiple heads.
Given inputs for queries, keys and values the `MultiHeadAttention`
produces new values by aggregating information from the input values
according to the similarities of the input queries and keys.
All inputs as well as the output are linearly projected without biases by
default.
`MultiHeadAttention` also takes an optional additive attention mask that
should be broadcastable with `(batch, num_heads, # queries, # keys)`. The
mask should have `-inf` or very large negative numbers at the positions
that should *not* be attended to.

Parameters:

**dims** ([int](https://docs.python.org/3/library/functions.html#int)) – The model dimensions. This is also the default
value for the queries, keys, values, and the output.
**num_heads** ([int](https://docs.python.org/3/library/functions.html#int)) – The number of attention heads to use.
**query_input_dims** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The input dimensions of the queries.
Default: `dims`.
**key_input_dims** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The input dimensions of the keys.
Default: `dims`.
**value_input_dims** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The input dimensions of the values.
Default: `key_input_dims`.
**value_dims** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The dimensions of the values after the
projection. Default: `dims`.
**value_output_dims** ([int](https://docs.python.org/3/library/functions.html#int)*, **optional*) – The dimensions the new values will
be projected to. Default: `dims`.
**bias** ([bool](https://docs.python.org/3/library/functions.html#bool)*, **optional*) – Whether or not to use a bias in the projections.
Default: `False`.

Methods

`create_additive_causal_mask`(N[, dtype])

** Contents
