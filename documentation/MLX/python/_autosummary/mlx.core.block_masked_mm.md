---
source: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.block_masked_mm.html
---

# mlx.core.block_masked_mm

**

- [.rst](../../_sources/python/_autosummary/mlx.core.block_masked_mm.rst)
- **

.pdf

**

# mlx.core.block_masked_mm

 Table of contents 

## Contents

# mlx.core.block_masked_mm

**block_masked_mm(*a: array*, *b: array*, */*, *block_size: int = 64*, *mask_out: array | None = None*, *mask_lhs: array | None = None*, *mask_rhs: array | None = None*, ***, *stream: None | Stream | Device = None*) → [array](mlx.core.array.html#mlx.core.array)**
: Matrix multiplication with block masking.
Perform the (possibly batched) matrix multiplication of two arrays and with blocks
of size `block_size x block_size` optionally masked out.
Assuming `a` with shape (…, M, K) and b with shape (…, K, N)

`lhs_mask` must have shape (…, \(\lceil\) M / `block_size` \(\rceil\), \(\lceil\) K / `block_size` \(\rceil\))
`rhs_mask` must have shape (…, \(\lceil\) K / `block_size` \(\rceil\), \(\lceil\) N / `block_size` \(\rceil\))
`out_mask` must have shape (…, \(\lceil\) M / `block_size` \(\rceil\), \(\lceil\) N / `block_size` \(\rceil\))

Note: Only `block_size=64` and `block_size=32` are currently supported

Parameters:

**a** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**b** ([array](mlx.core.array.html#mlx.core.array)) – Input array or scalar.
**block_size** ([int](https://docs.python.org/3/library/functions.html#int)) – Size of blocks to be masked. Must be `32` or `64`. Default: `64`.
**mask_out** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – Mask for output. Default: `None`.
**mask_lhs** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – Mask for `a`. Default: `None`.
**mask_rhs** ([array](mlx.core.array.html#mlx.core.array)*, **optional*) – Mask for `b`. Default: `None`.

Returns:
The output array.

Return type:
[array](mlx.core.array.html#mlx.core.array)

** Contents
