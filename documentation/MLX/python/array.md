---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/array.html
---

# Array

**

- [.rst](../_sources/python/array.rst)
- **

.pdf

**

**
**
**

**

# Array

 Table of contents 

# Array

| array(*args, **kwargs) | An N-dimensional array object. |
| --- | --- |
| array.astype(self, dtype[, stream]) | Cast the array to a specified type. |
| array.at | Used to apply updates at the given indices. |
| array.item(self) | Access the value of a scalar array. |
| array.tolist(self) | Convert the array to a Pythonlist. |
| array.dtype | The array'sDtype. |
| array.itemsize | The size of the array's datatype in bytes. |
| array.nbytes | The number of bytes in the array. |
| array.ndim | The array's dimension. |
| array.shape | The shape of the array as a Python tuple. |
| array.size | Number of elements in the array. |
| array.real | The real part of a complex array. |
| array.imag | The imaginary part of a complex array. |
| array.abs(self, *[, stream]) | Seeabs(). |
| array.all(self[, axis, keepdims, stream]) | Seeall(). |
| array.any(self[, axis, keepdims, stream]) | Seeany(). |
| array.argmax(self[, axis, keepdims, stream]) | Seeargmax(). |
| array.argmin(self[, axis, keepdims, stream]) | Seeargmin(). |
| array.conj(self, *[, stream]) | Seeconj(). |
| array.cos(self, *[, stream]) | Seecos(). |
| array.cummax(self[, axis, reverse, ...]) | Seecummax(). |
| array.cummin(self[, axis, reverse, ...]) | Seecummin(). |
| array.cumprod(self[, axis, reverse, ...]) | Seecumprod(). |
| array.cumsum(self[, axis, reverse, ...]) | Seecumsum(). |
| array.diag(self[, k, stream]) | Extract a diagonal or construct a diagonal matrix. |
| array.diagonal(self[, offset, axis1, axis2, ...]) | Seediagonal(). |
| array.exp(self, *[, stream]) | Seeexp(). |
| array.flatten(self[, start_axis, end_axis, ...]) | Seeflatten(). |
| array.log(self, *[, stream]) | Seelog(). |
| array.log10(self, *[, stream]) | Seelog10(). |
| array.log1p(self, *[, stream]) | Seelog1p(). |
| array.log2(self, *[, stream]) | Seelog2(). |
| array.logcumsumexp(self[, axis, reverse, ...]) | Seelogcumsumexp(). |
| array.logsumexp(self[, axis, keepdims, stream]) | Seelogsumexp(). |
| array.max(self[, axis, keepdims, stream]) | Seemax(). |
| array.mean(self[, axis, keepdims, stream]) | Seemean(). |
| array.min(self[, axis, keepdims, stream]) | Seemin(). |
| array.moveaxis(self, source, destination, *) | Seemoveaxis(). |
| array.prod(self[, axis, keepdims, stream]) | Seeprod(). |
| array.reciprocal(self, *[, stream]) | Seereciprocal(). |
| array.reshape(self, *shape[, stream]) | Equivalent toreshape()but the shape can be passed either as atupleor as separate arguments. |
| array.round(self[, decimals, stream]) | Seeround(). |
| array.rsqrt(self, *[, stream]) | Seersqrt(). |
| array.sin(self, *[, stream]) | Seesin(). |
| array.split(self, indices_or_sections[, ...]) | Seesplit(). |
| array.sqrt(self, *[, stream]) | Seesqrt(). |
| array.square(self, *[, stream]) | Seesquare(). |
| array.squeeze(self[, axis, stream]) | Seesqueeze(). |
| array.std(self[, axis, keepdims, ddof, stream]) | Seestd(). |
| array.sum(self[, axis, keepdims, stream]) | Seesum(). |
| array.swapaxes(self, axis1, axis2, *[, stream]) | Seeswapaxes(). |
| array.transpose(self, *axes[, stream]) | Equivalent totranspose()but the axes can be passed either as a tuple or as separate arguments. |
| array.T | Equivalent to callingself.transpose()with no arguments. |
| array.var(self[, axis, keepdims, ddof, stream]) | Seevar(). |
| array.view(self, dtype, *[, stream]) | Seeview(). |
