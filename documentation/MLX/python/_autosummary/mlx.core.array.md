---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/_autosummary/mlx.core.array.html
---

# mlx.core.array

```python
class array(*args, **kwargs)
```

An N-dimensional array object.

```python
__init__(self: array, val: scalar | list | tuple | DLPackCompatible | array, dtype: Dtype | None = None)
```

Methods

| [__init__](#mlx.core.array.__init__)(self, val[, dtype]) |  |
| --- | --- |
| [abs](mlx.core.array.abs.md#mlx.core.array.abs)(self, *[, stream]) | See [abs()](mlx.core.abs.md#mlx.core.abs). |
| [all](mlx.core.array.all.md#mlx.core.array.all)(self[, axis, keepdims, stream]) | See [all()](mlx.core.all.md#mlx.core.all). |
| [any](mlx.core.array.any.md#mlx.core.array.any)(self[, axis, keepdims, stream]) | See [any()](mlx.core.any.md#mlx.core.any). |
| [argmax](mlx.core.array.argmax.md#mlx.core.array.argmax)(self[, axis, keepdims, stream]) | See [argmax()](mlx.core.argmax.md#mlx.core.argmax). |
| [argmin](mlx.core.array.argmin.md#mlx.core.array.argmin)(self[, axis, keepdims, stream]) | See [argmin()](mlx.core.argmin.md#mlx.core.argmin). |
| [astype](mlx.core.array.astype.md#mlx.core.array.astype)(self, dtype[, stream]) | Cast the array to a specified type. |
| [conj](mlx.core.array.conj.md#mlx.core.array.conj)(self, *[, stream]) | See [conj()](mlx.core.conj.md#mlx.core.conj). |
| [cos](mlx.core.array.cos.md#mlx.core.array.cos)(self, *[, stream]) | See [cos()](mlx.core.cos.md#mlx.core.cos). |
| [cummax](mlx.core.array.cummax.md#mlx.core.array.cummax)(self[, axis, reverse, inclusive, stream]) | See [cummax()](mlx.core.cummax.md#mlx.core.cummax). |
| [cummin](mlx.core.array.cummin.md#mlx.core.array.cummin)(self[, axis, reverse, inclusive, stream]) | See [cummin()](mlx.core.cummin.md#mlx.core.cummin). |
| [cumprod](mlx.core.array.cumprod.md#mlx.core.array.cumprod)(self[, axis, reverse, inclusive, stream]) | See [cumprod()](mlx.core.cumprod.md#mlx.core.cumprod). |
| [cumsum](mlx.core.array.cumsum.md#mlx.core.array.cumsum)(self[, axis, reverse, inclusive, stream]) | See [cumsum()](mlx.core.cumsum.md#mlx.core.cumsum). |
| [diag](mlx.core.array.diag.md#mlx.core.array.diag)(self[, k, stream]) | Extract a diagonal or construct a diagonal matrix. |
| [diagonal](mlx.core.array.diagonal.md#mlx.core.array.diagonal)(self[, offset, axis1, axis2, stream]) | See [diagonal()](mlx.core.diagonal.md#mlx.core.diagonal). |
| [exp](mlx.core.array.exp.md#mlx.core.array.exp)(self, *[, stream]) | See [exp()](mlx.core.exp.md#mlx.core.exp). |
| [flatten](mlx.core.array.flatten.md#mlx.core.array.flatten)(self[, start_axis, end_axis, stream]) | See [flatten()](mlx.core.flatten.md#mlx.core.flatten). |
| [item](mlx.core.array.item.md#mlx.core.array.item)(self) | Access the value of a scalar array. |
| [log](mlx.core.array.log.md#mlx.core.array.log)(self, *[, stream]) | See [log()](mlx.core.log.md#mlx.core.log). |
| [log10](mlx.core.array.log10.md#mlx.core.array.log10)(self, *[, stream]) | See [log10()](mlx.core.log10.md#mlx.core.log10). |
| [log1p](mlx.core.array.log1p.md#mlx.core.array.log1p)(self, *[, stream]) | See [log1p()](mlx.core.log1p.md#mlx.core.log1p). |
| [log2](mlx.core.array.log2.md#mlx.core.array.log2)(self, *[, stream]) | See [log2()](mlx.core.log2.md#mlx.core.log2). |
| [logcumsumexp](mlx.core.array.logcumsumexp.md#mlx.core.array.logcumsumexp)(self[, axis, reverse, ...]) | See [logcumsumexp()](mlx.core.logcumsumexp.md#mlx.core.logcumsumexp). |
| [logsumexp](mlx.core.array.logsumexp.md#mlx.core.array.logsumexp)(self[, axis, keepdims, stream]) | See [logsumexp()](mlx.core.logsumexp.md#mlx.core.logsumexp). |
| [max](mlx.core.array.max.md#mlx.core.array.max)(self[, axis, keepdims, stream]) | See [max()](mlx.core.max.md#mlx.core.max). |
| [mean](mlx.core.array.mean.md#mlx.core.array.mean)(self[, axis, keepdims, stream]) | See [mean()](mlx.core.mean.md#mlx.core.mean). |
| [min](mlx.core.array.min.md#mlx.core.array.min)(self[, axis, keepdims, stream]) | See [min()](mlx.core.min.md#mlx.core.min). |
| [moveaxis](mlx.core.array.moveaxis.md#mlx.core.array.moveaxis)(self, source, destination, *[, stream]) | See [moveaxis()](mlx.core.moveaxis.md#mlx.core.moveaxis). |
| [prod](mlx.core.array.prod.md#mlx.core.array.prod)(self[, axis, keepdims, stream]) | See [prod()](mlx.core.prod.md#mlx.core.prod). |
| [reciprocal](mlx.core.array.reciprocal.md#mlx.core.array.reciprocal)(self, *[, stream]) | See [reciprocal()](mlx.core.reciprocal.md#mlx.core.reciprocal). |
| [reshape](mlx.core.array.reshape.md#mlx.core.array.reshape)(self, *shape[, stream]) | Equivalent to [reshape()](mlx.core.reshape.md#mlx.core.reshape) but the shape can be passed either as a [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple) or as separate arguments. |
| [round](mlx.core.array.round.md#mlx.core.array.round)(self[, decimals, stream]) | See [round()](mlx.core.round.md#mlx.core.round). |
| [rsqrt](mlx.core.array.rsqrt.md#mlx.core.array.rsqrt)(self, *[, stream]) | See [rsqrt()](mlx.core.rsqrt.md#mlx.core.rsqrt). |
| [sin](mlx.core.array.sin.md#mlx.core.array.sin)(self, *[, stream]) | See [sin()](mlx.core.sin.md#mlx.core.sin). |
| [split](mlx.core.array.split.md#mlx.core.array.split)(self, indices_or_sections[, axis, stream]) | See [split()](mlx.core.split.md#mlx.core.split). |
| [sqrt](mlx.core.array.sqrt.md#mlx.core.array.sqrt)(self, *[, stream]) | See [sqrt()](mlx.core.sqrt.md#mlx.core.sqrt). |
| [square](mlx.core.array.square.md#mlx.core.array.square)(self, *[, stream]) | See [square()](mlx.core.square.md#mlx.core.square). |
| [squeeze](mlx.core.array.squeeze.md#mlx.core.array.squeeze)(self[, axis, stream]) | See [squeeze()](mlx.core.squeeze.md#mlx.core.squeeze). |
| [std](mlx.core.array.std.md#mlx.core.array.std)(self[, axis, keepdims, ddof, ...]) | See [std()](mlx.core.std.md#mlx.core.std). |
| [sum](mlx.core.array.sum.md#mlx.core.array.sum)(self[, axis, keepdims, stream]) | See [sum()](mlx.core.sum.md#mlx.core.sum). |
| [swapaxes](mlx.core.array.swapaxes.md#mlx.core.array.swapaxes)(self, axis1, axis2, *[, stream]) | See [swapaxes()](mlx.core.swapaxes.md#mlx.core.swapaxes). |
| [tolist](mlx.core.array.tolist.md#mlx.core.array.tolist)(self) | Convert the array to a Python [list](https://docs.python.org/3/builtins/stdtypes.html#list). |
| [transpose](mlx.core.array.transpose.md#mlx.core.array.transpose)(self, *axes[, stream]) | Equivalent to [transpose()](mlx.core.transpose.md#mlx.core.transpose) but the axes can be passed either as a tuple or as separate arguments. |
| [var](mlx.core.array.var.md#mlx.core.array.var)(self[, axis, keepdims, ddof, ...]) | See [var()](mlx.core.var.md#mlx.core.var). |
| [view](mlx.core.array.view.md#mlx.core.array.view)(self, dtype, *[, stream]) | See [view()](mlx.core.view.md#mlx.core.view). |

Attributes

| [T](mlx.core.array.T.md#mlx.core.array.T) | Equivalent to calling `self.transpose()` with no arguments. |
| --- | --- |
| [at](mlx.core.array.at.md#mlx.core.array.at) | Used to apply updates at the given indices. |
| [dtype](mlx.core.array.dtype.md#mlx.core.array.dtype) | The array's [Dtype](mlx.core.Dtype.md#mlx.core.Dtype). |
| [imag](mlx.core.array.imag.md#mlx.core.array.imag) | The imaginary part of a complex array. |
| [itemsize](mlx.core.array.itemsize.md#mlx.core.array.itemsize) | The size of the array's datatype in bytes. |
| `mT` | Equivalent to calling `self.transpose()` with the last two axes swapped. |
| [nbytes](mlx.core.array.nbytes.md#mlx.core.array.nbytes) | The number of bytes in the array. |
| [ndim](mlx.core.array.ndim.md#mlx.core.array.ndim) | The array's dimension. |
| [real](mlx.core.array.real.md#mlx.core.array.real) | The real part of a complex array. |
| [shape](mlx.core.array.shape.md#mlx.core.array.shape) | The shape of the array as a Python tuple. |
| [size](mlx.core.array.size.md#mlx.core.array.size) | Number of elements in the array. |
