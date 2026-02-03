---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.fast.scaled_dot_product_attention.html
---

# mlx.core.fast.scaled_dot_product_attention

**

- [.rst](../../_sources/python/_autosummary/mlx.core.fast.scaled_dot_product_attention.rst)
- **

.pdf

**

# mlx.core.fast.scaled_dot_product_attention

 Table of contents 

## Contents

# mlx.core.fast.scaled_dot_product_attention

**scaled_dot_product_attention(*q: array*, *k: array*, *v: array*, ***, *scale: float*, *mask: None | str | array = None*, *sinks: array | None = None*, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: A fast implementation of multi-head attention: `O = softmax(Q @ K.T, dim=-1) @ V`.
Supports:

[Multi-Head Attention](https://arxiv.org/abs/1706.03762)
[Grouped Query Attention](https://arxiv.org/abs/2305.13245)
[Multi-Query Attention](https://arxiv.org/abs/1911.02150)

Note

The softmax operation is performed in `float32` regardless of
the input precision.
For Grouped Query Attention and Multi-Query Attention, the `k`
and `v` inputs should not be pre-tiled to match `q`.

In the following the dimensions are given by:

`B`: The batch size.
`N_q`: The number of query heads.
`N_kv`: The number of key and value heads.
`T_q`: The number of queries per example.
`T_kv`: The number of keys and values per example.
`D`: The per-head dimension.

Parameters:

**q** ([array](mlx.core.array.html#mlx.core.array)) – Queries with shape `[B, N_q, T_q, D]`.
**k** ([array](mlx.core.array.html#mlx.core.array)) – Keys with shape `[B, N_kv, T_kv, D]`.
**v** ([array](mlx.core.array.html#mlx.core.array)) – Values with shape `[B, N_kv, T_kv, D]`.
**scale** ([float](https://docs.python.org/3/library/functions.html#float)) – Scale for queries (typically `1.0 / sqrt(q.shape(-1)`).
**mask** ([str](https://docs.python.org/3/library/stdtypes.html#str)* or *[array](mlx.core.array.html#mlx.core.array)*, **optional*) – The mask to apply to the
query-key scores. The mask can be an array or a string indicating
the mask type. The only supported string type is `"causal"`. If
the mask is an array it can be a boolean or additive mask. The mask
can have at most 4 dimensions and must be broadcast-compatible with
the shape `[B, N, T_q, T_kv]`. If an additive mask is given its
type must promote to the promoted type of `q`, `k`, and `v`.
The `"causal"` mask uses lower-right alignment where the
last query aligns with the last key.
**sinks** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – An optional array of attention sinks.
Default: `None`.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

Example
B = 2
N_q = N_kv = 32
T_q = T_kv = 1000
D = 128

q = mx.random.normal(shape=(B, N_q, T_q, D))
k = mx.random.normal(shape=(B, N_kv, T_kv, D))
v = mx.random.normal(shape=(B, N_kv, T_kv, D))
scale = D ** -0.5
out = mx.fast.scaled_dot_product_attention(q, k, v, scale=scale, mask="causal")

** Contents
