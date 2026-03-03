---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/python/ops.html
---

# Operations

**

- [.rst](../_sources/python/ops.rst)
- **

.pdf

**

# Operations

 Table of contents 

# Operations

| abs(a, /, *[, stream]) | Element-wise absolute value. |
| --- | --- |
| add(a, b[, stream]) | Element-wise addition. |
| addmm(c, a, b, /[, alpha, beta, stream]) | Matrix multiplication with addition and optional scaling. |
| all(a, /[, axis, keepdims, stream]) | Anandreduction over the given axes. |
| allclose(a, b, /[, rtol, atol, equal_nan, ...]) | Approximate comparison of two arrays. |
| any(a, /[, axis, keepdims, stream]) | Anorreduction over the given axes. |
| arange(-> array) | Overloaded function. |
| arccos(a, /, *[, stream]) | Element-wise inverse cosine. |
| arccosh(a, /, *[, stream]) | Element-wise inverse hyperbolic cosine. |
| arcsin(a, /, *[, stream]) | Element-wise inverse sine. |
| arcsinh(a, /, *[, stream]) | Element-wise inverse hyperbolic sine. |
| arctan(a, /, *[, stream]) | Element-wise inverse tangent. |
| arctan2(a, b, /, *[, stream]) | Element-wise inverse tangent of the ratio of two arrays. |
| arctanh(a, /, *[, stream]) | Element-wise inverse hyperbolic tangent. |
| argmax(a, /[, axis, keepdims, stream]) | Indices of the maximum values along the axis. |
| argmin(a, /[, axis, keepdims, stream]) | Indices of the minimum values along the axis. |
| argpartition(a, /, kth[, axis, stream]) | Returns the indices that partition the array. |
| argsort(a, /[, axis, stream]) | Returns the indices that sort the array. |
| array_equal(a, b[, equal_nan, stream]) | Array equality check. |
| as_strided(a, /[, shape, strides, offset, ...]) | Create a view into the array with the given shape and strides. |
| atleast_1d(*arys[, stream]) | Convert all arrays to have at least one dimension. |
| atleast_2d(*arys[, stream]) | Convert all arrays to have at least two dimensions. |
| atleast_3d(*arys[, stream]) | Convert all arrays to have at least three dimensions. |
| bitwise_and(a, b[, stream]) | Element-wise bitwise and. |
| bitwise_invert(a[, stream]) | Element-wise bitwise inverse. |
| bitwise_or(a, b[, stream]) | Element-wise bitwise or. |
| bitwise_xor(a, b[, stream]) | Element-wise bitwise xor. |
| block_masked_mm(a, b, /[, block_size, ...]) | Matrix multiplication with block masking. |
| broadcast_arrays(*arrays[, stream]) | Broadcast arrays against one another. |
| broadcast_to(a, /, shape, *[, stream]) | Broadcast an array to the given shape. |
| ceil(a, /, *[, stream]) | Element-wise ceil. |
| clip(a, /, a_min, a_max, *[, stream]) | Clip the values of the array between the given minimum and maximum. |
| concatenate(arrays[, axis, stream]) | Concatenate the arrays along the given axis. |
| contiguous(a, /[, allow_col_major, stream]) | Force an array to be row contiguous. |
| conj(a, *[, stream]) | Return the elementwise complex conjugate of the input. |
| conjugate(a, *[, stream]) | Return the elementwise complex conjugate of the input. |
| convolve(a, v, /[, mode, stream]) | The discrete convolution of 1D arrays. |
| conv1d(input, weight, /[, stride, padding, ...]) | 1D convolution over an input with several channels |
| conv2d(input, weight, /[, stride, padding, ...]) | 2D convolution over an input with several channels |
| conv3d(input, weight, /[, stride, padding, ...]) | 3D convolution over an input with several channels |
| conv_transpose1d(input, weight, /[, stride, ...]) | 1D transposed convolution over an input with several channels |
| conv_transpose2d(input, weight, /[, stride, ...]) | 2D transposed convolution over an input with several channels |
| conv_transpose3d(input, weight, /[, stride, ...]) | 3D transposed convolution over an input with several channels |
| conv_general(input, weight, /[, stride, ...]) | General convolution over an input with several channels |
| cos(a, /, *[, stream]) | Element-wise cosine. |
| cosh(a, /, *[, stream]) | Element-wise hyperbolic cosine. |
| cummax(a, /[, axis, reverse, inclusive, stream]) | Return the cumulative maximum of the elements along the given axis. |
| cummin(a, /[, axis, reverse, inclusive, stream]) | Return the cumulative minimum of the elements along the given axis. |
| cumprod(a, /[, axis, reverse, inclusive, stream]) | Return the cumulative product of the elements along the given axis. |
| cumsum(a, /[, axis, reverse, inclusive, stream]) | Return the cumulative sum of the elements along the given axis. |
| degrees(a, /, *[, stream]) | Convert angles from radians to degrees. |
| dequantize(w, /, scales[, biases, ...]) | Dequantize the matrixwusing quantization parameters. |
| diag(a, /[, k, stream]) | Extract a diagonal or construct a diagonal matrix. |
| diagonal(a[, offset, axis1, axis2, stream]) | Return specified diagonals. |
| divide(a, b[, stream]) | Element-wise division. |
| divmod(a, b[, stream]) | Element-wise quotient and remainder. |
| einsum(subscripts, *operands[, stream]) | Perform the Einstein summation convention on the operands. |
| einsum_path(subscripts, *operands) | Compute the contraction order for the given Einstein summation. |
| equal(a, b[, stream]) | Element-wise equality. |
| erf(a, /, *[, stream]) | Element-wise error function. |
| erfinv(a, /, *[, stream]) | Element-wise inverse oferf(). |
| exp(a, /, *[, stream]) | Element-wise exponential. |
| expm1(a, /, *[, stream]) | Element-wise exponential minus 1. |
| expand_dims(a, /, axis, *[, stream]) | Add a size one dimension at the given axis. |
| eye(n[, m, k, dtype, stream]) | Create an identity matrix or a general diagonal matrix. |
| flatten(a, /[, start_axis, end_axis, stream]) | Flatten an array. |
| floor(a, /, *[, stream]) | Element-wise floor. |
| floor_divide(a, b[, stream]) | Element-wise integer division. |
| full(shape, vals[, dtype, stream]) | Construct an array with the given value. |
| gather_mm(a, b, /, lhs_indices, rhs_indices, *) | Matrix multiplication with matrix-level gather. |
| gather_qmm(x, w, /, scales[, biases, ...]) | Perform quantized matrix multiplication with matrix-level gather. |
| greater(a, b[, stream]) | Element-wise greater than. |
| greater_equal(a, b[, stream]) | Element-wise greater or equal. |
| hadamard_transform(a[, scale, stream]) | Perform the Walsh-Hadamard transform along the final axis. |
| identity(n[, dtype, stream]) | Create a square identity matrix. |
| imag(a, /, *[, stream]) | Returns the imaginary part of a complex array. |
| inner(a, b, /, *[, stream]) | Ordinary inner product of vectors for 1-D arrays, in higher dimensions a sum product over the last axes. |
| isfinite(a[, stream]) | Return a boolean array indicating which elements are finite. |
| isclose(a, b, /[, rtol, atol, equal_nan, stream]) | Returns a boolean array where two arrays are element-wise equal within a tolerance. |
| isinf(a[, stream]) | Return a boolean array indicating which elements are +/- inifnity. |
| isnan(a[, stream]) | Return a boolean array indicating which elements are NaN. |
| isneginf(a[, stream]) | Return a boolean array indicating which elements are negative infinity. |
| isposinf(a[, stream]) | Return a boolean array indicating which elements are positive infinity. |
| issubdtype(arg1, arg2) | Check if aDtypeorDtypeCategoryis a subtype of another. |
| kron(a, b, *[, stream]) | Compute the Kronecker product of two arraysaandb. |
| left_shift(a, b[, stream]) | Element-wise left shift. |
| less(a, b[, stream]) | Element-wise less than. |
| less_equal(a, b[, stream]) | Element-wise less than or equal. |
| linspace(start, stop[, num, dtype, stream]) | Generatenumevenly spaced numbers over interval[start,stop]. |
| load(file, /[, format, return_metadata, stream]) | Load array(s) from a binary file. |
| log(a, /, *[, stream]) | Element-wise natural logarithm. |
| log2(a, /, *[, stream]) | Element-wise base-2 logarithm. |
| log10(a, /, *[, stream]) | Element-wise base-10 logarithm. |
| log1p(a, /, *[, stream]) | Element-wise natural log of one plus the array. |
| logaddexp(a, b, /, *[, stream]) | Element-wise log-add-exp. |
| logcumsumexp(a, /[, axis, reverse, ...]) | Return the cumulative logsumexp of the elements along the given axis. |
| logical_not(a, /, *[, stream]) | Element-wise logical not. |
| logical_and(a, b, /, *[, stream]) | Element-wise logical and. |
| logical_or(a, b, /, *[, stream]) | Element-wise logical or. |
| logsumexp(a, /[, axis, keepdims, stream]) | Alog-sum-expreduction over the given axes. |
| matmul(a, b, /, *[, stream]) | Matrix multiplication. |
| max(a, /[, axis, keepdims, stream]) | Amaxreduction over the given axes. |
| maximum(a, b, /, *[, stream]) | Element-wise maximum. |
| mean(a, /[, axis, keepdims, stream]) | Compute the mean(s) over the given axes. |
| median(a, /[, axis, keepdims, stream]) | Compute the median(s) over the given axes. |
| meshgrid(*arrays[, sparse, indexing, stream]) | Generate multidimensional coordinate grids from 1-D coordinate arrays |
| min(a, /[, axis, keepdims, stream]) | Aminreduction over the given axes. |
| minimum(a, b, /, *[, stream]) | Element-wise minimum. |
| moveaxis(a, /, source, destination, *[, stream]) | Move an axis to a new position. |
| multiply(a, b[, stream]) | Element-wise multiplication. |
| nan_to_num(a[, nan, posinf, neginf, stream]) | Replace NaN and Inf values with finite numbers. |
| negative(a, /, *[, stream]) | Element-wise negation. |
| not_equal(a, b[, stream]) | Element-wise not equal. |
| ones(shape[, dtype, stream]) | Construct an array of ones. |
| ones_like(a, /, *[, stream]) | An array of ones like the input. |
| outer(a, b, /, *[, stream]) | Compute the outer product of two 1-D arrays, if the array's passed are not 1-D a flatten op will be run beforehand. |
| partition(a, /, kth[, axis, stream]) | Returns a partitioned copy of the array such that the smallerkthelements are first. |
| pad(a, pad_width[, mode, constant_values, ...]) | Pad an array with a constant value |
| power(a, b, /, *[, stream]) | Element-wise power operation. |
| prod(a, /[, axis, keepdims, stream]) | An product reduction over the given axes. |
| put_along_axis(a, /, indices, values[, ...]) | Put values along an axis at the specified indices. |
| quantize(w, /[, group_size, bits, mode, ...]) | Quantize the arrayw. |
| quantized_matmul(x, w, /, scales[, biases, ...]) | Perform the matrix multiplication with the quantized matrixw. |
| radians(a, /, *[, stream]) | Convert angles from degrees to radians. |
| real(a, /, *[, stream]) | Returns the real part of a complex array. |
| reciprocal(a, /, *[, stream]) | Element-wise reciprocal. |
| remainder(a, b[, stream]) | Element-wise remainder of division. |
| repeat(array, repeats[, axis, stream]) | Repeat an array along a specified axis. |
| reshape(a, /, shape, *[, stream]) | Reshape an array while preserving the size. |
| right_shift(a, b[, stream]) | Element-wise right shift. |
| roll(a, shift[, axis, stream]) | Roll array elements along a given axis. |
| round(a, /[, decimals, stream]) | Round to the given number of decimals. |
| rsqrt(a, /, *[, stream]) | Element-wise reciprocal and square root. |
| save(file, arr) | Save the array to a binary file in.npyformat. |
| savez(file, *args, **kwargs) | Save several arrays to a binary file in uncompressed.npzformat. |
| savez_compressed(file, *args, **kwargs) | Save several arrays to a binary file in compressed.npzformat. |
| save_gguf(file, arrays, metadata) | Save array(s) to a binary file in.ggufformat. |
| save_safetensors(file, arrays[, metadata]) | Save array(s) to a binary file in.safetensorsformat. |
| sigmoid(a, /, *[, stream]) | Element-wise logistic sigmoid. |
| sign(a, /, *[, stream]) | Element-wise sign. |
| sin(a, /, *[, stream]) | Element-wise sine. |
| sinh(a, /, *[, stream]) | Element-wise hyperbolic sine. |
| slice(a, start_indices, axes, slice_size, *) | Extract a sub-array from the input array. |
| slice_update(a, update, start_indices, axes, *) | Update a sub-array of the input array. |
| softmax(a, /[, axis, stream]) | Perform the softmax along the given axis. |
| sort(a, /[, axis, stream]) | Returns a sorted copy of the array. |
| split(a, /, indices_or_sections[, axis, stream]) | Split an array along a given axis. |
| sqrt(a, /, *[, stream]) | Element-wise square root. |
| square(a, /, *[, stream]) | Element-wise square. |
| squeeze(a, /[, axis, stream]) | Remove length one axes from an array. |
| stack(arrays[, axis, stream]) | Stacks the arrays along a new axis. |
| std(a, /[, axis, keepdims, ddof, stream]) | Compute the standard deviation(s) over the given axes. |
| stop_gradient(a, /, *[, stream]) | Stop gradients from being computed. |
| subtract(a, b[, stream]) | Element-wise subtraction. |
| sum(a, /[, axis, keepdims, stream]) | Sum reduce the array over the given axes. |
| swapaxes(a, /, axis1, axis2, *[, stream]) | Swap two axes of an array. |
| take(a, /, indices[, axis, stream]) | Take elements along an axis. |
| take_along_axis(a, /, indices[, axis, stream]) | Take values along an axis at the specified indices. |
| tan(a, /, *[, stream]) | Element-wise tangent. |
| tanh(a, /, *[, stream]) | Element-wise hyperbolic tangent. |
| tensordot(a, b, /[, axes, stream]) | Compute the tensor dot product along the specified axes. |
| tile(a, reps, /, *[, stream]) | Construct an array by repeatingathe number of times given byreps. |
| topk(a, /, k[, axis, stream]) | Returns theklargest elements from the input along a given axis. |
| trace(a, /[, offset, axis1, axis2, dtype, ...]) | Return the sum along a specified diagonal in the given array. |
| transpose(a, /[, axes, stream]) | Transpose the dimensions of the array. |
| tri(n, m, k[, dtype, stream]) | An array with ones at and below the given diagonal and zeros elsewhere. |
| tril(x, k, *[, stream]) | Zeros the array above the given diagonal. |
| triu(x, k, *[, stream]) | Zeros the array below the given diagonal. |
| unflatten(a, /, axis, shape, *[, stream]) | Unflatten an axis of an array to a shape. |
| var(a, /[, axis, keepdims, ddof, stream]) | Compute the variance(s) over the given axes. |
| view(a, dtype[, stream]) | View the array as a different type. |
| where(condition, x, y, /, *[, stream]) | Select fromxoryaccording tocondition. |
| zeros(shape[, dtype, stream]) | Construct an array of zeros. |
| zeros_like(a, /, *[, stream]) | An array of zeros like the input. |
