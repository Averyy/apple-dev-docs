---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/ops.html
---

# Operations

| [abs](_autosummary/mlx.core.abs.md#mlx.core.abs)(a, /, *[, stream]) | Element-wise absolute value. |
| --- | --- |
| [add](_autosummary/mlx.core.add.md#mlx.core.add)(a, b[, stream]) | Element-wise addition. |
| [addmm](_autosummary/mlx.core.addmm.md#mlx.core.addmm)(c, a, b, /[, alpha, beta, stream]) | Matrix multiplication with addition and optional scaling. |
| [all](_autosummary/mlx.core.all.md#mlx.core.all)(a, /[, axis, keepdims, stream]) | An and reduction over the given axes. |
| [allclose](_autosummary/mlx.core.allclose.md#mlx.core.allclose)(a, b, /[, rtol, atol, equal_nan, ...]) | Approximate comparison of two arrays. |
| [any](_autosummary/mlx.core.any.md#mlx.core.any)(a, /[, axis, keepdims, stream]) | An or reduction over the given axes. |
| [arange](_autosummary/mlx.core.arange.md#mlx.core.arange)(-> array) | Overloaded function. |
| [arccos](_autosummary/mlx.core.arccos.md#mlx.core.arccos)(a, /, *[, stream]) | Element-wise inverse cosine. |
| [arccosh](_autosummary/mlx.core.arccosh.md#mlx.core.arccosh)(a, /, *[, stream]) | Element-wise inverse hyperbolic cosine. |
| [arcsin](_autosummary/mlx.core.arcsin.md#mlx.core.arcsin)(a, /, *[, stream]) | Element-wise inverse sine. |
| [arcsinh](_autosummary/mlx.core.arcsinh.md#mlx.core.arcsinh)(a, /, *[, stream]) | Element-wise inverse hyperbolic sine. |
| [arctan](_autosummary/mlx.core.arctan.md#mlx.core.arctan)(a, /, *[, stream]) | Element-wise inverse tangent. |
| [arctan2](_autosummary/mlx.core.arctan2.md#mlx.core.arctan2)(a, b, /, *[, stream]) | Element-wise inverse tangent of the ratio of two arrays. |
| [arctanh](_autosummary/mlx.core.arctanh.md#mlx.core.arctanh)(a, /, *[, stream]) | Element-wise inverse hyperbolic tangent. |
| [argmax](_autosummary/mlx.core.argmax.md#mlx.core.argmax)(a, /[, axis, keepdims, stream]) | Indices of the maximum values along the axis. |
| [argmin](_autosummary/mlx.core.argmin.md#mlx.core.argmin)(a, /[, axis, keepdims, stream]) | Indices of the minimum values along the axis. |
| [argpartition](_autosummary/mlx.core.argpartition.md#mlx.core.argpartition)(a, /, kth[, axis, stream]) | Returns the indices that partition the array. |
| [argsort](_autosummary/mlx.core.argsort.md#mlx.core.argsort)(a, /[, axis, stream]) | Returns the indices that sort the array. |
| [array_equal](_autosummary/mlx.core.array_equal.md#mlx.core.array_equal)(a, b[, equal_nan, stream]) | Array equality check. |
| [asarray](_autosummary/mlx.core.asarray.md#mlx.core.asarray)(a[, dtype, copy]) | Convert the input to an array. |
| [as_strided](_autosummary/mlx.core.as_strided.md#mlx.core.as_strided)(a, /[, shape, strides, offset, ...]) | Create a view into the array with the given shape and strides. |
| [astype](_autosummary/mlx.core.astype.md#mlx.core.astype)(a, dtype, /, *[, stream]) | Cast the array to a specified type. |
| [atleast_1d](_autosummary/mlx.core.atleast_1d.md#mlx.core.atleast_1d)(*arys[, stream]) | Convert all arrays to have at least one dimension. |
| [atleast_2d](_autosummary/mlx.core.atleast_2d.md#mlx.core.atleast_2d)(*arys[, stream]) | Convert all arrays to have at least two dimensions. |
| [atleast_3d](_autosummary/mlx.core.atleast_3d.md#mlx.core.atleast_3d)(*arys[, stream]) | Convert all arrays to have at least three dimensions. |
| [bartlett](_autosummary/mlx.core.bartlett.md#mlx.core.bartlett)(M, *[, stream]) | Return the Bartlett window. |
| [bitwise_and](_autosummary/mlx.core.bitwise_and.md#mlx.core.bitwise_and)(a, b[, stream]) | Element-wise bitwise and. |
| [bitwise_invert](_autosummary/mlx.core.bitwise_invert.md#mlx.core.bitwise_invert)(a[, stream]) | Element-wise bitwise inverse. |
| [bitwise_or](_autosummary/mlx.core.bitwise_or.md#mlx.core.bitwise_or)(a, b[, stream]) | Element-wise bitwise or. |
| [bitwise_xor](_autosummary/mlx.core.bitwise_xor.md#mlx.core.bitwise_xor)(a, b[, stream]) | Element-wise bitwise xor. |
| [blackman](_autosummary/mlx.core.blackman.md#mlx.core.blackman)(M, *[, stream]) | Return the Blackman window. |
| [block_masked_mm](_autosummary/mlx.core.block_masked_mm.md#mlx.core.block_masked_mm)(a, b, /[, block_size, ...]) | Matrix multiplication with block masking. |
| [broadcast_arrays](_autosummary/mlx.core.broadcast_arrays.md#mlx.core.broadcast_arrays)(*arrays[, stream]) | Broadcast arrays against one another. |
| [broadcast_shapes](_autosummary/mlx.core.broadcast_shapes.md#mlx.core.broadcast_shapes)(*shapes) | Broadcast shapes. |
| [broadcast_to](_autosummary/mlx.core.broadcast_to.md#mlx.core.broadcast_to)(a, /, shape, *[, stream]) | Broadcast an array to the given shape. |
| [can_cast](_autosummary/mlx.core.can_cast.md#mlx.core.can_cast)(from_, to) | Determine if one data type can be cast to another according to type promotion rules. |
| [ceil](_autosummary/mlx.core.ceil.md#mlx.core.ceil)(a, /, *[, stream]) | Element-wise ceil. |
| [clip](_autosummary/mlx.core.clip.md#mlx.core.clip)(a, /, a_min, a_max, *[, stream]) | Clip the values of the array between the given minimum and maximum. |
| [concat](_autosummary/mlx.core.concat.md#mlx.core.concat)(arrays[, axis, stream]) | See [concatenate()](_autosummary/mlx.core.concatenate.md#mlx.core.concatenate). |
| [concatenate](_autosummary/mlx.core.concatenate.md#mlx.core.concatenate)(arrays[, axis, stream]) | Concatenate the arrays along the given axis. |
| [contiguous](_autosummary/mlx.core.contiguous.md#mlx.core.contiguous)(a, /[, allow_col_major, stream]) | Force an array to be row contiguous. |
| [conj](_autosummary/mlx.core.conj.md#mlx.core.conj)(a, *[, stream]) | Return the elementwise complex conjugate of the input. |
| [conjugate](_autosummary/mlx.core.conjugate.md#mlx.core.conjugate)(a, *[, stream]) | Return the elementwise complex conjugate of the input. |
| [convolve](_autosummary/mlx.core.convolve.md#mlx.core.convolve)(a, v, /[, mode, stream]) | The discrete convolution of 1D arrays. |
| [conv1d](_autosummary/mlx.core.conv1d.md#mlx.core.conv1d)(input, weight, /[, stride, padding, ...]) | 1D convolution over an input with several channels |
| [conv2d](_autosummary/mlx.core.conv2d.md#mlx.core.conv2d)(input, weight, /[, stride, padding, ...]) | 2D convolution over an input with several channels |
| [conv3d](_autosummary/mlx.core.conv3d.md#mlx.core.conv3d)(input, weight, /[, stride, padding, ...]) | 3D convolution over an input with several channels |
| [conv_transpose1d](_autosummary/mlx.core.conv_transpose1d.md#mlx.core.conv_transpose1d)(input, weight, /[, stride, ...]) | 1D transposed convolution over an input with several channels |
| [conv_transpose2d](_autosummary/mlx.core.conv_transpose2d.md#mlx.core.conv_transpose2d)(input, weight, /[, stride, ...]) | 2D transposed convolution over an input with several channels |
| [conv_transpose3d](_autosummary/mlx.core.conv_transpose3d.md#mlx.core.conv_transpose3d)(input, weight, /[, stride, ...]) | 3D transposed convolution over an input with several channels |
| [conv_general](_autosummary/mlx.core.conv_general.md#mlx.core.conv_general)(input, weight, /[, stride, ...]) | General convolution over an input with several channels |
| [cos](_autosummary/mlx.core.cos.md#mlx.core.cos)(a, /, *[, stream]) | Element-wise cosine. |
| [cosh](_autosummary/mlx.core.cosh.md#mlx.core.cosh)(a, /, *[, stream]) | Element-wise hyperbolic cosine. |
| [cummax](_autosummary/mlx.core.cummax.md#mlx.core.cummax)(a, /[, axis, reverse, inclusive, stream]) | Return the cumulative maximum of the elements along the given axis. |
| [cummin](_autosummary/mlx.core.cummin.md#mlx.core.cummin)(a, /[, axis, reverse, inclusive, stream]) | Return the cumulative minimum of the elements along the given axis. |
| [cumprod](_autosummary/mlx.core.cumprod.md#mlx.core.cumprod)(a, /[, axis, reverse, inclusive, ...]) | Return the cumulative product of the elements along the given axis. |
| [cumsum](_autosummary/mlx.core.cumsum.md#mlx.core.cumsum)(a, /[, axis, reverse, inclusive, ...]) | Return the cumulative sum of the elements along the given axis. |
| [count_nonzero](_autosummary/mlx.core.count_nonzero.md#mlx.core.count_nonzero)(a, /, *[, axis, keepdims, stream]) | Count the number of non-zero elements along the given axis. |
| [degrees](_autosummary/mlx.core.degrees.md#mlx.core.degrees)(a, /, *[, stream]) | Convert angles from radians to degrees. |
| [depends](_autosummary/mlx.core.depends.md#mlx.core.depends)(inputs, dependencies) | Insert dependencies between arrays in the graph. |
| [dequantize](_autosummary/mlx.core.dequantize.md#mlx.core.dequantize)(w, /, scales[, biases, ...]) | Dequantize the matrix `w` using quantization parameters. |
| [diag](_autosummary/mlx.core.diag.md#mlx.core.diag)(a, /[, k, stream]) | Extract a diagonal or construct a diagonal matrix. |
| [diagonal](_autosummary/mlx.core.diagonal.md#mlx.core.diagonal)(a[, offset, axis1, axis2, stream]) | Return specified diagonals. |
| [diff](_autosummary/mlx.core.diff.md#mlx.core.diff)(a, /[, n, axis, stream]) | The n-th discrete difference along the given axis. |
| [divide](_autosummary/mlx.core.divide.md#mlx.core.divide)(a, b[, stream]) | Element-wise division. |
| [divmod](_autosummary/mlx.core.divmod.md#mlx.core.divmod)(a, b[, stream]) | Element-wise quotient and remainder. |
| [einsum](_autosummary/mlx.core.einsum.md#mlx.core.einsum)(subscripts, *operands[, stream]) | Perform the Einstein summation convention on the operands. |
| [einsum_path](_autosummary/mlx.core.einsum_path.md#mlx.core.einsum_path)(subscripts, *operands) | Compute the contraction order for the given Einstein summation. |
| [equal](_autosummary/mlx.core.equal.md#mlx.core.equal)(a, b[, stream]) | Element-wise equality. |
| [erf](_autosummary/mlx.core.erf.md#mlx.core.erf)(a, /, *[, stream]) | Element-wise error function. |
| [erfinv](_autosummary/mlx.core.erfinv.md#mlx.core.erfinv)(a, /, *[, stream]) | Element-wise inverse of [erf()](_autosummary/mlx.core.erf.md#mlx.core.erf). |
| [exp](_autosummary/mlx.core.exp.md#mlx.core.exp)(a, /, *[, stream]) | Element-wise exponential. |
| [expm1](_autosummary/mlx.core.expm1.md#mlx.core.expm1)(a, /, *[, stream]) | Element-wise exponential minus 1. |
| [expand_dims](_autosummary/mlx.core.expand_dims.md#mlx.core.expand_dims)(a, /, axis, *[, stream]) | Add a size one dimension at the given axis. |
| [eye](_autosummary/mlx.core.eye.md#mlx.core.eye)(n[, m, k, dtype, stream]) | Create an identity matrix or a general diagonal matrix. |
| [flatten](_autosummary/mlx.core.flatten.md#mlx.core.flatten)(a, /[, start_axis, end_axis, stream]) | Flatten an array. |
| [flip](_autosummary/mlx.core.flip.md#mlx.core.flip)(a, /[, axis, stream]) | Reverse the order of elements along the given axis. |
| [floor](_autosummary/mlx.core.floor.md#mlx.core.floor)(a, /, *[, stream]) | Element-wise floor. |
| [floor_divide](_autosummary/mlx.core.floor_divide.md#mlx.core.floor_divide)(a, b[, stream]) | Element-wise integer division. |
| [full](_autosummary/mlx.core.full.md#mlx.core.full)(shape, vals[, dtype, stream]) | Construct an array with the given value. |
| [from_dlpack](_autosummary/mlx.core.from_dlpack.md#mlx.core.from_dlpack)(x, /, *[, copy]) | Create an array from an object that supports DLPack. |
| [full_like](_autosummary/mlx.core.full_like.md#mlx.core.full_like)(a, vals[, dtype, stream]) | An array filled with `vals` with the same shape as the input. |
| [from_fp8](_autosummary/mlx.core.from_fp8.md#mlx.core.from_fp8)(x[, dtype, stream]) | Convert the array from fp8 (e4m3) to another floating-point type. |
| [gather_mm](_autosummary/mlx.core.gather_mm.md#mlx.core.gather_mm)(a, b, /[, lhs_indices, ...]) | Matrix multiplication with matrix-level gather. |
| [gather_qmm](_autosummary/mlx.core.gather_qmm.md#mlx.core.gather_qmm)(x, w, /, scales[, biases, ...]) | Perform quantized matrix multiplication with matrix-level gather. |
| [greater](_autosummary/mlx.core.greater.md#mlx.core.greater)(a, b[, stream]) | Element-wise greater than. |
| [greater_equal](_autosummary/mlx.core.greater_equal.md#mlx.core.greater_equal)(a, b[, stream]) | Element-wise greater or equal. |
| [hadamard_transform](_autosummary/mlx.core.hadamard_transform.md#mlx.core.hadamard_transform)(a[, scale, stream]) | Perform the Walsh-Hadamard transform along the final axis. |
| [hamming](_autosummary/mlx.core.hamming.md#mlx.core.hamming)(M, *[, stream]) | Return the Hamming window. |
| [hanning](_autosummary/mlx.core.hanning.md#mlx.core.hanning)(M, *[, stream]) | Return the Hanning window. |
| [identity](_autosummary/mlx.core.identity.md#mlx.core.identity)(n[, dtype, stream]) | Create a square identity matrix. |
| [imag](_autosummary/mlx.core.imag.md#mlx.core.imag)(a, /, *[, stream]) | Returns the imaginary part of a complex array. |
| [inner](_autosummary/mlx.core.inner.md#mlx.core.inner)(a, b, /, *[, stream]) | Ordinary inner product of vectors for 1-D arrays, in higher dimensions a sum product over the last axes. |
| [isdtype](_autosummary/mlx.core.isdtype.md#mlx.core.isdtype)(dtype, kind) | Test whether a dtype belongs to one or more data type kinds. |
| [isfinite](_autosummary/mlx.core.isfinite.md#mlx.core.isfinite)(a[, stream]) | Return a boolean array indicating which elements are finite. |
| [isclose](_autosummary/mlx.core.isclose.md#mlx.core.isclose)(a, b, /[, rtol, atol, equal_nan, stream]) | Returns a boolean array where two arrays are element-wise equal within a tolerance. |
| [isinf](_autosummary/mlx.core.isinf.md#mlx.core.isinf)(a[, stream]) | Return a boolean array indicating which elements are +/- inifnity. |
| [isnan](_autosummary/mlx.core.isnan.md#mlx.core.isnan)(a[, stream]) | Return a boolean array indicating which elements are NaN. |
| [isneginf](_autosummary/mlx.core.isneginf.md#mlx.core.isneginf)(a[, stream]) | Return a boolean array indicating which elements are negative infinity. |
| [isposinf](_autosummary/mlx.core.isposinf.md#mlx.core.isposinf)(a[, stream]) | Return a boolean array indicating which elements are positive infinity. |
| [issubdtype](_autosummary/mlx.core.issubdtype.md#mlx.core.issubdtype)(arg1, arg2) | Check if a [Dtype](_autosummary/mlx.core.Dtype.md#mlx.core.Dtype) or [DtypeCategory](_autosummary/mlx.core.DtypeCategory.md#mlx.core.DtypeCategory) is a subtype of another. |
| [kron](_autosummary/mlx.core.kron.md#mlx.core.kron)(a, b, *[, stream]) | Compute the Kronecker product of two arrays `a` and `b`. |
| [left_shift](_autosummary/mlx.core.left_shift.md#mlx.core.left_shift)(a, b[, stream]) | Element-wise left shift. |
| [less](_autosummary/mlx.core.less.md#mlx.core.less)(a, b[, stream]) | Element-wise less than. |
| [less_equal](_autosummary/mlx.core.less_equal.md#mlx.core.less_equal)(a, b[, stream]) | Element-wise less than or equal. |
| [linspace](_autosummary/mlx.core.linspace.md#mlx.core.linspace)(start, stop[, num, endpoint, ...]) | Generate `num` evenly spaced numbers over interval `[start, stop]`. |
| [load](_autosummary/mlx.core.load.md#mlx.core.load)(file, /[, format, return_metadata, stream]) | Load array(s) from a binary file. |
| [log](_autosummary/mlx.core.log.md#mlx.core.log)(a, /, *[, stream]) | Element-wise natural logarithm. |
| [log2](_autosummary/mlx.core.log2.md#mlx.core.log2)(a, /, *[, stream]) | Element-wise base-2 logarithm. |
| [log10](_autosummary/mlx.core.log10.md#mlx.core.log10)(a, /, *[, stream]) | Element-wise base-10 logarithm. |
| [log1p](_autosummary/mlx.core.log1p.md#mlx.core.log1p)(a, /, *[, stream]) | Element-wise natural log of one plus the array. |
| [logaddexp](_autosummary/mlx.core.logaddexp.md#mlx.core.logaddexp)(a, b, /, *[, stream]) | Element-wise log-add-exp. |
| [logcumsumexp](_autosummary/mlx.core.logcumsumexp.md#mlx.core.logcumsumexp)(a, /[, axis, reverse, ...]) | Return the cumulative logsumexp of the elements along the given axis. |
| [logical_not](_autosummary/mlx.core.logical_not.md#mlx.core.logical_not)(a, /, *[, stream]) | Element-wise logical not. |
| [logical_and](_autosummary/mlx.core.logical_and.md#mlx.core.logical_and)(a, b, /, *[, stream]) | Element-wise logical and. |
| [logical_or](_autosummary/mlx.core.logical_or.md#mlx.core.logical_or)(a, b, /, *[, stream]) | Element-wise logical or. |
| [logical_xor](_autosummary/mlx.core.logical_xor.md#mlx.core.logical_xor)(a, b, /, *[, stream]) | Element-wise logical exclusive or. |
| [logsumexp](_autosummary/mlx.core.logsumexp.md#mlx.core.logsumexp)(a, /[, axis, keepdims, stream]) | A log-sum-exp reduction over the given axes. |
| [matmul](_autosummary/mlx.core.matmul.md#mlx.core.matmul)(a, b, /, *[, stream]) | Matrix multiplication. |
| [max](_autosummary/mlx.core.max.md#mlx.core.max)(a, /[, axis, keepdims, stream]) | A max reduction over the given axes. |
| [maximum](_autosummary/mlx.core.maximum.md#mlx.core.maximum)(a, b, /, *[, stream]) | Element-wise maximum. |
| [mean](_autosummary/mlx.core.mean.md#mlx.core.mean)(a, /[, axis, keepdims, stream]) | Compute the mean(s) over the given axes. |
| [median](_autosummary/mlx.core.median.md#mlx.core.median)(a, /[, axis, keepdims, stream]) | Compute the median(s) over the given axes. |
| [meshgrid](_autosummary/mlx.core.meshgrid.md#mlx.core.meshgrid)(*arrays[, sparse, indexing, stream]) | Generate multidimensional coordinate grids from 1-D coordinate arrays |
| [min](_autosummary/mlx.core.min.md#mlx.core.min)(a, /[, axis, keepdims, stream]) | A min reduction over the given axes. |
| [minimum](_autosummary/mlx.core.minimum.md#mlx.core.minimum)(a, b, /, *[, stream]) | Element-wise minimum. |
| [minmax](_autosummary/mlx.core.minmax.md#mlx.core.minmax)(a, /[, axis, keepdims, stream]) | Return the minimum and maximum over the given axes. |
| [moveaxis](_autosummary/mlx.core.moveaxis.md#mlx.core.moveaxis)(a, /, source, destination, *[, stream]) | Move an axis to a new position. |
| [multiply](_autosummary/mlx.core.multiply.md#mlx.core.multiply)(a, b[, stream]) | Element-wise multiplication. |
| [nan_to_num](_autosummary/mlx.core.nan_to_num.md#mlx.core.nan_to_num)(a[, nan, posinf, neginf, stream]) | Replace NaN and Inf values with finite numbers. |
| [negative](_autosummary/mlx.core.negative.md#mlx.core.negative)(a, /, *[, stream]) | Element-wise negation. |
| [not_equal](_autosummary/mlx.core.not_equal.md#mlx.core.not_equal)(a, b[, stream]) | Element-wise not equal. |
| [ones](_autosummary/mlx.core.ones.md#mlx.core.ones)(shape[, dtype, stream]) | Construct an array of ones. |
| [ones_like](_autosummary/mlx.core.ones_like.md#mlx.core.ones_like)(a, /[, dtype, stream]) | An array of ones like the input. |
| [outer](_autosummary/mlx.core.outer.md#mlx.core.outer)(a, b, /, *[, stream]) | Compute the outer product of two 1-D arrays, if the array's passed are not 1-D a flatten op will be run beforehand. |
| [partition](_autosummary/mlx.core.partition.md#mlx.core.partition)(a, /, kth[, axis, stream]) | Returns a partitioned copy of the array such that the smaller `kth` elements are first. |
| [pad](_autosummary/mlx.core.pad.md#mlx.core.pad)(a, pad_width[, mode, constant_values, ...]) | Pad an array with a constant value |
| [permute_dims](_autosummary/mlx.core.permute_dims.md#mlx.core.permute_dims)(a, /[, axes, stream]) | See [transpose()](_autosummary/mlx.core.transpose.md#mlx.core.transpose). |
| [positive](_autosummary/mlx.core.positive.md#mlx.core.positive)(a, /, *[, stream]) | Element-wise unary plus. |
| [power](_autosummary/mlx.core.power.md#mlx.core.power)(a, b, /, *[, stream]) | Element-wise power operation. |
| [prod](_autosummary/mlx.core.prod.md#mlx.core.prod)(a, /[, axis, keepdims, stream]) | An product reduction over the given axes. |
| [put_along_axis](_autosummary/mlx.core.put_along_axis.md#mlx.core.put_along_axis)(a, /, indices, values[, ...]) | Put values along an axis at the specified indices. |
| [quantize](_autosummary/mlx.core.quantize.md#mlx.core.quantize)(w, /[, group_size, bits, mode, ...]) | Quantize the array `w`. |
| [quantized_matmul](_autosummary/mlx.core.quantized_matmul.md#mlx.core.quantized_matmul)(x, w, /, scales[, biases, ...]) | Perform the matrix multiplication with the quantized matrix `w`. |
| [qqmm](_autosummary/mlx.core.qqmm.md#mlx.core.qqmm)(x, w[, scales, group_size, bits, mode, ...]) | Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. |
| [radians](_autosummary/mlx.core.radians.md#mlx.core.radians)(a, /, *[, stream]) | Convert angles from degrees to radians. |
| [real](_autosummary/mlx.core.real.md#mlx.core.real)(a, /, *[, stream]) | Returns the real part of a complex array. |
| [reciprocal](_autosummary/mlx.core.reciprocal.md#mlx.core.reciprocal)(a, /, *[, stream]) | Element-wise reciprocal. |
| [remainder](_autosummary/mlx.core.remainder.md#mlx.core.remainder)(a, b[, stream]) | Element-wise remainder of division. |
| [repeat](_autosummary/mlx.core.repeat.md#mlx.core.repeat)(array, repeats[, axis, stream]) | Repeat an array along a specified axis. |
| [reshape](_autosummary/mlx.core.reshape.md#mlx.core.reshape)(a, /, shape, *[, stream]) | Reshape an array while preserving the size. |
| [result_type](_autosummary/mlx.core.result_type.md#mlx.core.result_type)(*arrays_and_dtypes) | The type that results from applying type promotion to the inputs. |
| [right_shift](_autosummary/mlx.core.right_shift.md#mlx.core.right_shift)(a, b[, stream]) | Element-wise right shift. |
| [roll](_autosummary/mlx.core.roll.md#mlx.core.roll)(a, shift[, axis, stream]) | Roll array elements along a given axis. |
| [round](_autosummary/mlx.core.round.md#mlx.core.round)(a, /[, decimals, stream]) | Round to the given number of decimals. |
| [rsqrt](_autosummary/mlx.core.rsqrt.md#mlx.core.rsqrt)(a, /, *[, stream]) | Element-wise reciprocal and square root. |
| [save](_autosummary/mlx.core.save.md#mlx.core.save)(file, arr) | Save the array to a binary file in `.npy` format. |
| [savez](_autosummary/mlx.core.savez.md#mlx.core.savez)(file, *args, **kwargs) | Save several arrays to a binary file in uncompressed `.npz` format. |
| [savez_compressed](_autosummary/mlx.core.savez_compressed.md#mlx.core.savez_compressed)(file, *args, **kwargs) | Save several arrays to a binary file in compressed `.npz` format. |
| [save_gguf](_autosummary/mlx.core.save_gguf.md#mlx.core.save_gguf)(file, arrays, metadata) | Save array(s) to a binary file in `.gguf` format. |
| [save_safetensors](_autosummary/mlx.core.save_safetensors.md#mlx.core.save_safetensors)(file, arrays[, metadata]) | Save array(s) to a binary file in `.safetensors` format. |
| [searchsorted](_autosummary/mlx.core.searchsorted.md#mlx.core.searchsorted)(sorted_sequence, values, /[, ...]) | Find the indices that keep `sorted_sequence` sorted when inserting `values`. |
| [sigmoid](_autosummary/mlx.core.sigmoid.md#mlx.core.sigmoid)(a, /, *[, stream]) | Element-wise logistic sigmoid. |
| [sign](_autosummary/mlx.core.sign.md#mlx.core.sign)(a, /, *[, stream]) | Element-wise sign. |
| [sin](_autosummary/mlx.core.sin.md#mlx.core.sin)(a, /, *[, stream]) | Element-wise sine. |
| [sinh](_autosummary/mlx.core.sinh.md#mlx.core.sinh)(a, /, *[, stream]) | Element-wise hyperbolic sine. |
| [slice](_autosummary/mlx.core.slice.md#mlx.core.slice)(a, start_indices, axes, slice_size, *) | Extract a sub-array from the input array. |
| [slice_update](_autosummary/mlx.core.slice_update.md#mlx.core.slice_update)(a, update, start_indices, axes, *) | Update a sub-array of the input array. |
| [segmented_mm](_autosummary/mlx.core.segmented_mm.md#mlx.core.segmented_mm)(a, b, /, segments, *[, stream]) | Perform a matrix multiplication but segment the inner dimension and save the result for each segment separately. |
| [softmax](_autosummary/mlx.core.softmax.md#mlx.core.softmax)(a, /[, axis, precise, stream]) | Perform the softmax along the given axis. |
| [sort](_autosummary/mlx.core.sort.md#mlx.core.sort)(a, /[, axis, stream]) | Returns a sorted copy of the array. |
| [split](_autosummary/mlx.core.split.md#mlx.core.split)(a, /, indices_or_sections[, axis, stream]) | Split an array along a given axis. |
| [sqrt](_autosummary/mlx.core.sqrt.md#mlx.core.sqrt)(a, /, *[, stream]) | Element-wise square root. |
| [square](_autosummary/mlx.core.square.md#mlx.core.square)(a, /, *[, stream]) | Element-wise square. |
| [squeeze](_autosummary/mlx.core.squeeze.md#mlx.core.squeeze)(a, /[, axis, stream]) | Remove length one axes from an array. |
| [stack](_autosummary/mlx.core.stack.md#mlx.core.stack)(arrays[, axis, stream]) | Stacks the arrays along a new axis. |
| [std](_autosummary/mlx.core.std.md#mlx.core.std)(a, /[, axis, keepdims, ddof, stream]) | Compute the standard deviation(s) over the given axes. |
| [stop_gradient](_autosummary/mlx.core.stop_gradient.md#mlx.core.stop_gradient)(a, /, *[, stream]) | Stop gradients from being computed. |
| [subtract](_autosummary/mlx.core.subtract.md#mlx.core.subtract)(a, b[, stream]) | Element-wise subtraction. |
| [sum](_autosummary/mlx.core.sum.md#mlx.core.sum)(a, /[, axis, keepdims, stream]) | Sum reduce the array over the given axes. |
| [swapaxes](_autosummary/mlx.core.swapaxes.md#mlx.core.swapaxes)(a, /, axis1, axis2, *[, stream]) | Swap two axes of an array. |
| [take](_autosummary/mlx.core.take.md#mlx.core.take)(a, /, indices[, axis, stream]) | Take elements along an axis. |
| [take_along_axis](_autosummary/mlx.core.take_along_axis.md#mlx.core.take_along_axis)(a, /, indices[, axis, stream]) | Take values along an axis at the specified indices. |
| [tan](_autosummary/mlx.core.tan.md#mlx.core.tan)(a, /, *[, stream]) | Element-wise tangent. |
| [tanh](_autosummary/mlx.core.tanh.md#mlx.core.tanh)(a, /, *[, stream]) | Element-wise hyperbolic tangent. |
| [tensordot](_autosummary/mlx.core.tensordot.md#mlx.core.tensordot)(a, b, /[, axes, stream]) | Compute the tensor dot product along the specified axes. |
| [tile](_autosummary/mlx.core.tile.md#mlx.core.tile)(a, reps, /, *[, stream]) | Construct an array by repeating `a` the number of times given by `reps`. |
| [topk](_autosummary/mlx.core.topk.md#mlx.core.topk)(a, /, k[, axis, stream]) | Returns the `k` largest elements from the input along a given axis. |
| [to_fp8](_autosummary/mlx.core.to_fp8.md#mlx.core.to_fp8)(x, *[, stream]) | Convert the array to fp8 (e4m3) from another floating-point type. |
| [trace](_autosummary/mlx.core.trace.md#mlx.core.trace)(a, /[, offset, axis1, axis2, dtype, ...]) | Return the sum along a specified diagonal in the given array. |
| [transpose](_autosummary/mlx.core.transpose.md#mlx.core.transpose)(a, /[, axes, stream]) | Transpose the dimensions of the array. |
| [tri](_autosummary/mlx.core.tri.md#mlx.core.tri)(n[, m, k, dtype, stream]) | An array with ones at and below the given diagonal and zeros elsewhere. |
| [tril](_autosummary/mlx.core.tril.md#mlx.core.tril)(x[, k, stream]) | Zeros the array above the given diagonal. |
| [triu](_autosummary/mlx.core.triu.md#mlx.core.triu)(x[, k, stream]) | Zeros the array below the given diagonal. |
| [trunc](_autosummary/mlx.core.trunc.md#mlx.core.trunc)(a, /, *[, stream]) | Element-wise truncation towards zero. |
| [unflatten](_autosummary/mlx.core.unflatten.md#mlx.core.unflatten)(a, /, axis, shape, *[, stream]) | Unflatten an axis of an array to a shape. |
| [unique](_autosummary/mlx.core.unique.md#mlx.core.unique)(a, /, size[, return_index, ...]) | Returns the sorted unique elements of the flattened array. |
| [unstack](_autosummary/mlx.core.unstack.md#mlx.core.unstack)(x, /, *[, axis, stream]) | Split an array into a sequence of arrays along the given axis. |
| [vecdot](_autosummary/mlx.core.vecdot.md#mlx.core.vecdot)(a, b, /, *[, axis, stream]) | Compute the vector dot product of two arrays along an axis. |
| [var](_autosummary/mlx.core.var.md#mlx.core.var)(a, /[, axis, keepdims, ddof, stream]) | Compute the variance(s) over the given axes. |
| [view](_autosummary/mlx.core.view.md#mlx.core.view)(a, dtype[, stream]) | View the array as a different type. |
| [where](_autosummary/mlx.core.where.md#mlx.core.where)(condition, x, y, /, *[, stream]) | Select from `x` or `y` according to `condition`. |
| [zeros](_autosummary/mlx.core.zeros.md#mlx.core.zeros)(shape[, dtype, stream]) | Construct an array of zeros. |
| [zeros_like](_autosummary/mlx.core.zeros_like.md#mlx.core.zeros_like)(a, /[, dtype, stream]) | An array of zeros like the input. |
