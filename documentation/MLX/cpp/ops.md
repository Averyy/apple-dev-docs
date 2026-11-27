---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/cpp/ops.html
---

# Operations

```cpp
array mlx::core::arange(double start, double stop, double step, Dtype dtype, StreamOrDevice s)
```

A 1D array of numbers starting at start (optional), stopping at stop,
stepping by step (optional).

```cpp
array mlx::core::linspace(double start, double stop, int num, bool endpoint, Dtype dtype, StreamOrDevice s)
```

A 1D array of num evenly spaced numbers in the range [start, stop], or
in the half-open range [start, stop) when endpoint is false.

```cpp
array mlx::core::astype(array a, Dtype dtype, StreamOrDevice s)
```

Convert an array to the given data type.

```cpp
array mlx::core::as_strided(array a, Shape shape, Strides strides, size_t offset, StreamOrDevice s)
```

Create a view of an array with the given shape and strides.

```cpp
array mlx::core::copy(array a, StreamOrDevice s)
```

Copy another array.

```cpp
array mlx::core::full(Shape shape, array vals, Dtype dtype, StreamOrDevice s)
```

Fill an array of the given shape with the given value(s).

```cpp
array mlx::core::zeros(const Shape &shape, Dtype dtype, StreamOrDevice s)
```

Fill an array of the given shape with zeros.

```cpp
array mlx::core::zeros_like(const array &a, StreamOrDevice s)
```

Create an array of zeros with the shape of a.

```cpp
array mlx::core::ones(const Shape &shape, Dtype dtype, StreamOrDevice s)
```

Fill an array of the given shape with ones.

```cpp
array mlx::core::ones_like(const array &a, StreamOrDevice s)
```

Create an array of ones with the shape of a.

```cpp
array mlx::core::eye(int n, int m, int k, Dtype dtype, StreamOrDevice s)
```

**Fill an array of the given shape (n,m) with ones in the specified diagonal**

- k, and zeros everywhere else.

```cpp
array mlx::core::identity(int n, Dtype dtype, StreamOrDevice s)
```

**Create a square matrix of shape (n,n) of zeros, and ones in the major**

- diagonal.

```cpp
array mlx::core::reshape(const array &a, Shape shape, StreamOrDevice s)
```

Reshape an array to the given shape.

```cpp
array mlx::core::unflatten(const array &a, int axis, Shape shape, StreamOrDevice s)
```

Unflatten the axis to the given shape.

```cpp
array mlx::core::flatten(const array &a, int start_axis, int end_axis, StreamOrDevice s)
```

Flatten the dimensions in the range [start_axis, end_axis] .

```cpp
array mlx::core::flatten(const array &a, StreamOrDevice s)
```

Flatten the array to 1D.

```cpp
array mlx::core::hadamard_transform(const array &a, std::optional<float> scale, StreamOrDevice s)
```

Multiply the array by the Hadamard matrix of corresponding size.

```cpp
array mlx::core::squeeze(const array &a, const std::vector<int> &axes, StreamOrDevice s)
```

Remove singleton dimensions at the given axes.

```cpp
array mlx::core::squeeze(const array &a, int axis, StreamOrDevice s)
```

Remove singleton dimensions at the given axis.

```cpp
array mlx::core::squeeze(const array &a, StreamOrDevice s)
```

Remove all singleton dimensions.

```cpp
array mlx::core::expand_dims(const array &a, const std::vector<int> &axes, StreamOrDevice s)
```

Add a singleton dimension at the given axes.

```cpp
array mlx::core::expand_dims(const array &a, int axis, StreamOrDevice s)
```

Add a singleton dimension at the given axis.

```cpp
array mlx::core::flip(const array &a, const std::vector<int> &axes, StreamOrDevice s)
```

Reverse the order of the elements along the given axes.

```cpp
array mlx::core::flip(const array &a, int axis, StreamOrDevice s)
```

Reverse the order of the elements along the given axis.

```cpp
array mlx::core::flip(const array &a, StreamOrDevice s)
```

Reverse the order of the elements along all axes.

```cpp
array mlx::core::slice(const array &a, Shape start, Shape stop, Shape strides, StreamOrDevice s)
```

Slice an array.

```cpp
array mlx::core::slice(const array &a, Shape start, Shape stop, StreamOrDevice s)
```

Slice an array with a stride of 1 in each dimension.

```cpp
array mlx::core::slice(const array &a, const array &start, std::vector<int> axes, Shape slice_size, StreamOrDevice s)
```

Slice an array with dynamic starting indices.

```cpp
array mlx::core::slice_update(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s)
```

Update a slice from the source array.

```cpp
array mlx::core::slice_update(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s)
```

Update a slice from the source array with stride 1 in each dimension.

```cpp
array mlx::core::slice_update(const array &src, const array &update, const array &start, std::vector<int> axes, StreamOrDevice s)
```

Update a slice from the source array with dynamic starting indices.

```cpp
array mlx::core::slice_update_add(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s)
```

Slice update and add updates to given slice.

```cpp
array mlx::core::slice_update_add(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s)
```

Slice update and add updates to given slice with stride 1 in each dimension.

```cpp
array mlx::core::slice_update_prod(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s)
```

Slice update and prod updates to given slice.

```cpp
array mlx::core::slice_update_prod(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s)
```

**Slice update and prod updates to given slice with stride 1 in each**

- dimension.

```cpp
array mlx::core::slice_update_max(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s)
```

Slice update and max updates to given slice.

```cpp
array mlx::core::slice_update_max(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s)
```

Slice update and max updates to given slice with stride 1 in each dimension.

```cpp
array mlx::core::slice_update_min(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s)
```

Slice update and min updates to given slice.

```cpp
array mlx::core::slice_update_min(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s)
```

Slice update and min updates to given slice with stride 1 in each dimension.

```cpp
std::vector<array> mlx::core::split(const array &a, int num_splits, int axis, StreamOrDevice s)
```

Split an array into sub-arrays along a given axis.

```cpp
std::vector<array> mlx::core::unstack(const array &a, int axis, StreamOrDevice s)
```

Split an array into a sequence of arrays along an axis, removing it.

```cpp
std::vector<array> mlx::core::meshgrid(const std::vector<array> &arrays, bool sparse, const std::string &indexing, StreamOrDevice s)
```

A vector of coordinate arrays from coordinate vectors.

```cpp
array mlx::core::clip(const array &a, const std::optional<array> &a_min, const std::optional<array> &a_max, StreamOrDevice s)
```

Clip (limit) the values in an array.

```cpp
array mlx::core::concatenate(std::vector<array> arrays, int axis, StreamOrDevice s)
```

Concatenate arrays along a given axis.

```cpp
array mlx::core::stack(const std::vector<array> &arrays, int axis, StreamOrDevice s)
```

Stack arrays along a new axis.

```cpp
array mlx::core::repeat(const array &arr, int repeats, int axis, StreamOrDevice s)
```

Repeat an array along an axis.

```cpp
array mlx::core::transpose(const array &a, std::vector<int> axes, StreamOrDevice s)
```

Permutes the dimensions according to the given axes.

```cpp
array mlx::core::matrix_transpose(const array &a, StreamOrDevice s)
```

Permutes last two dimensions of an array.

```cpp
array mlx::core::swapaxes(const array &a, int axis1, int axis2, StreamOrDevice s)
```

Swap two axes of an array.

```cpp
array mlx::core::moveaxis(const array &a, int source, int destination, StreamOrDevice s)
```

Move an axis of an array.

```cpp
array mlx::core::pad(const array &a, const std::vector<int> &axes, const Shape &low_pad_size, const Shape &high_pad_size, const array &pad_value, const std::string &mode, StreamOrDevice s)
```

Pad an array with a constant value

```cpp
array mlx::core::pad(const array &a, const std::vector<std::pair<int, int>> &pad_width, const array &pad_value, const std::string &mode, StreamOrDevice s)
```

Pad an array with a constant value along all axes

```cpp
array mlx::core::transpose(const array &a, StreamOrDevice s)
```

Permutes the dimensions in reverse order.

```cpp
array mlx::core::broadcast_to(const array &a, const Shape &shape, StreamOrDevice s)
```

Broadcast an array to a given shape.

```cpp
std::vector<array> mlx::core::broadcast_arrays(const std::vector<array> &inputs, StreamOrDevice s)
```

Broadcast a vector of arrays against one another.

```cpp
array mlx::core::equal(const array &a, const array &b, StreamOrDevice s)
```

Returns the bool array with (a == b) element-wise.

```cpp
array mlx::core::not_equal(const array &a, const array &b, StreamOrDevice s)
```

Returns the bool array with (a != b) element-wise.

```cpp
array mlx::core::greater(const array &a, const array &b, StreamOrDevice s)
```

Returns bool array with (a > b) element-wise.

```cpp
array mlx::core::greater_equal(const array &a, const array &b, StreamOrDevice s)
```

Returns bool array with (a >= b) element-wise.

```cpp
array mlx::core::less(const array &a, const array &b, StreamOrDevice s)
```

Returns bool array with (a < b) element-wise.

```cpp
array mlx::core::less_equal(const array &a, const array &b, StreamOrDevice s)
```

Returns bool array with (a <= b) element-wise.

```cpp
array mlx::core::array_equal(const array &a, const array &b, bool equal_nan, StreamOrDevice s)
```

True if two arrays have the same shape and elements.

```cpp
array mlx::core::where(const array &condition, const array &x, const array &y, StreamOrDevice s)
```

Select from x or y depending on condition.

```cpp
array mlx::core::nan_to_num(const array &a, float nan, const std::optional<float> posinf, const std::optional<float> neginf, StreamOrDevice s)
```

Replace NaN and infinities with finite numbers.

```cpp
array mlx::core::all(const array &a, bool keepdims, StreamOrDevice s)
```

True if all elements in the array are true (or non-zero). *

```cpp
array mlx::core::allclose(const array &a, const array &b, double rtol, double atol, bool equal_nan, StreamOrDevice s)
```

True if the two arrays are equal within the specified tolerance.

```cpp
array mlx::core::isclose(const array &a, const array &b, double rtol, double atol, bool equal_nan, StreamOrDevice s)
```

Returns a boolean array where two arrays are element-wise equal within the
specified tolerance.

```cpp
array mlx::core::all(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

Reduces the input along the given axes. An output value is true
if all the corresponding inputs are true.

```cpp
array mlx::core::all(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

Reduces the input along the given axis. An output value is true
if all the corresponding inputs are true.

```cpp
array mlx::core::any(const array &a, bool keepdims, StreamOrDevice s)
```

True if any elements in the array are true (or non-zero). *

```cpp
array mlx::core::any(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

Reduces the input along the given axes. An output value is true
if any of the corresponding inputs are true.

```cpp
array mlx::core::any(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

Reduces the input along the given axis. An output value is true
if any of the corresponding inputs are true.

```cpp
array mlx::core::sum(const array &a, bool keepdims, StreamOrDevice s)
```

Sums the elements of an array.

```cpp
array mlx::core::sum(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

Sums the elements of an array along the given axes.

```cpp
array mlx::core::sum(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

Sums the elements of an array along the given axis.

```cpp
array mlx::core::count_nonzero(const array &a, bool keepdims, StreamOrDevice s)
```

Count the number of non-zero elements in an array.

```cpp
array mlx::core::mean(const array &a, bool keepdims, StreamOrDevice s)
```

Computes the mean of the elements of an array.

```cpp
array mlx::core::mean(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

Computes the mean of the elements of an array along the given axes

```cpp
array mlx::core::mean(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

Computes the mean of the elements of an array along the given axis

```cpp
array mlx::core::median(const array &a, bool keepdims, StreamOrDevice s)
```

Computes the median of the elements of an array.

```cpp
array mlx::core::median(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

Computes the median of the elements of an array along the given axes

```cpp
array mlx::core::median(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

Computes the median of the elements of an array along the given axis

```cpp
array mlx::core::var(const array &a, bool keepdims, int ddof, StreamOrDevice s)
```

Computes the variance of the elements of an array.

```cpp
array mlx::core::var(const array &a, const std::vector<int> &axes, bool keepdims, int ddof, StreamOrDevice s)
```

Computes the variance of the elements of an array along the given axes.

```cpp
array mlx::core::var(const array &a, int axis, bool keepdims, int ddof, StreamOrDevice s)
```

Computes the variance of the elements of an array along the given axis.

```cpp
array mlx::core::std(const array &a, bool keepdims, int ddof, StreamOrDevice s)
```

Computes the standard deviation of the elements of an array.

```cpp
array mlx::core::std(const array &a, const std::vector<int> &axes, bool keepdims, int ddof, StreamOrDevice s)
```

Computes the standard deviation of the elements of an array along the given
axes.

```cpp
array mlx::core::std(const array &a, int axis, bool keepdims, int ddof, StreamOrDevice s)
```

Computes the standard deviation of the elements of an array along the given
axes.

```cpp
array mlx::core::prod(const array &a, bool keepdims, StreamOrDevice s)
```

The product of all elements of the array.

```cpp
array mlx::core::prod(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

The product of the elements of an array along the given axes.

```cpp
array mlx::core::prod(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

The product of the elements of an array along the given axis.

```cpp
array mlx::core::max(const array &a, bool keepdims, StreamOrDevice s)
```

The maximum of all elements of the array.

```cpp
array mlx::core::max(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

The maximum of the elements of an array along the given axes.

```cpp
array mlx::core::max(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

The maximum of the elements of an array along the given axis.

```cpp
array mlx::core::min(const array &a, bool keepdims, StreamOrDevice s)
```

The minimum of all elements of the array.

```cpp
array mlx::core::min(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

The minimum of the elements of an array along the given axes.

```cpp
array mlx::core::min(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

The minimum of the elements of an array along the given axis.

```cpp
std::tuple<array, array> mlx::core::minmax(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

The minimum and maximum of the elements of an array along the given axes.

```cpp
std::tuple<array, array> mlx::core::minmax(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

The minimum and maximum of the elements of an array along the given axis.

```cpp
array mlx::core::hanning(int M, StreamOrDevice s)
```

Returns the Hanning window of size M.

```cpp
array mlx::core::hamming(int M, StreamOrDevice s)
```

Returns the Hamming window of size M.

```cpp
array mlx::core::bartlett(int M, StreamOrDevice s)
```

Returns the bartlett window of size M.

```cpp
array mlx::core::blackman(int M, StreamOrDevice s)
```

Returns the Blackmann window of size M.

```cpp
array mlx::core::argmin(const array &a, bool keepdims, StreamOrDevice s)
```

Returns the index of the minimum value in the array.

```cpp
array mlx::core::argmin(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

Returns the indices of the minimum values along a given axis.

```cpp
array mlx::core::argmax(const array &a, bool keepdims, StreamOrDevice s)
```

Returns the index of the maximum value in the array.

```cpp
array mlx::core::argmax(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

Returns the indices of the maximum values along a given axis.

```cpp
array mlx::core::sort(const array &a, StreamOrDevice s)
```

Returns a sorted copy of the flattened array.
The sort is stable and NaN values are placed at the end.

```cpp
array mlx::core::sort(const array &a, int axis, StreamOrDevice s)
```

Returns a sorted copy of the array along a given axis.
The sort is stable and NaN values are placed at the end.

```cpp
array mlx::core::argsort(const array &a, StreamOrDevice s)
```

Returns indices that sort the flattened array.
The sort is stable and NaN values are placed at the end.

```cpp
array mlx::core::argsort(const array &a, int axis, StreamOrDevice s)
```

Returns indices that sort the array along a given axis.
The sort is stable and NaN values are placed at the end.

```cpp
array mlx::core::partition(const array &a, int kth, StreamOrDevice s)
```

Returns a partitioned copy of the flattened array
such that the smaller kth elements are first.

```cpp
array mlx::core::partition(const array &a, int kth, int axis, StreamOrDevice s)
```

Returns a partitioned copy of the array along a given axis
such that the smaller kth elements are first.

```cpp
array mlx::core::argpartition(const array &a, int kth, StreamOrDevice s)
```

Returns indices that partition the flattened array
such that the smaller kth elements are first.

```cpp
array mlx::core::argpartition(const array &a, int kth, int axis, StreamOrDevice s)
```

Returns indices that partition the array along a given axis
such that the smaller kth elements are first.

```cpp
array mlx::core::searchsorted(const array &sorted_sequence, const array &values, const std::string &side, StreamOrDevice s)
```

Find the indices of values in sorted_sequence.

```cpp
array mlx::core::topk(const array &a, int k, StreamOrDevice s)
```

Returns topk elements of the flattened array.

```cpp
array mlx::core::topk(const array &a, int k, int axis, StreamOrDevice s)
```

Returns topk elements of the array along a given axis.

```cpp
std::vector<array> mlx::core::unique(const array &a, int size, bool return_index, bool return_inverse, bool return_counts, const std::optional<array> &fill_value, StreamOrDevice s)
```

Returns the sorted unique elements of the flattened array, and optionally
the index of the first occurrence of each, the inverse indices and the
counts. The output has the given size, and
is truncated if `size` is smaller than the number of unique values.
If `size` is larger, the result is padded with `fill_value`, or the
first of the sorted unique values if no fill value is provided. An empty
input has none, so it throws unless `size` is zero or a fill value is
given.
A truncated output loses the counts of the values it drops, and its inverse
indices are clamped to the last entry.

```cpp
array mlx::core::logcumsumexp(const array &a, bool reverse, bool inclusive, StreamOrDevice s)
```

Cumulative logsumexp of an array.

```cpp
array mlx::core::logcumsumexp(const array &a, int axis, bool reverse, bool inclusive, StreamOrDevice s)
```

Cumulative logsumexp of an array along the given axis.

```cpp
array mlx::core::logsumexp(const array &a, bool keepdims, StreamOrDevice s)
```

The logsumexp of all elements of the array.

```cpp
array mlx::core::logsumexp(const array &a, const std::vector<int> &axes, bool keepdims, StreamOrDevice s)
```

The logsumexp of the elements of an array along the given axes.

```cpp
array mlx::core::logsumexp(const array &a, int axis, bool keepdims, StreamOrDevice s)
```

The logsumexp of the elements of an array along the given axis.

```cpp
array mlx::core::abs(const array &a, StreamOrDevice s)
```

Absolute value of elements in an array.

```cpp
array mlx::core::positive(const array &a, StreamOrDevice s)
```

Unary plus — return a copy of the array unchanged.

```cpp
array mlx::core::negative(const array &a, StreamOrDevice s)
```

Negate an array.

```cpp
array mlx::core::sign(const array &a, StreamOrDevice s)
```

The sign of the elements in an array.

```cpp
array mlx::core::logical_not(const array &a, StreamOrDevice s)
```

Logical not of an array

```cpp
array mlx::core::logical_and(const array &a, const array &b, StreamOrDevice s)
```

Logical and of two arrays

```cpp
array mlx::core::logical_or(const array &a, const array &b, StreamOrDevice s)
```

Logical or of two arrays

```cpp
array mlx::core::logical_xor(const array &a, const array &b, StreamOrDevice s)
```

Logical exclusive or of two arrays

```cpp
array mlx::core::reciprocal(const array &a, StreamOrDevice s)
```

The reciprocal (1/x) of the elements in an array.

```cpp
array mlx::core::add(const array &a, const array &b, StreamOrDevice s)
```

Add two arrays.

```cpp
array mlx::core::subtract(const array &a, const array &b, StreamOrDevice s)
```

Subtract two arrays.

```cpp
array mlx::core::multiply(const array &a, const array &b, StreamOrDevice s)
```

Multiply two arrays.

```cpp
array mlx::core::divide(const array &a, const array &b, StreamOrDevice s)
```

Divide two arrays.

```cpp
std::vector<array> mlx::core::divmod(const array &a, const array &b, StreamOrDevice s)
```

Compute the element-wise quotient and remainder.

```cpp
array mlx::core::floor_divide(const array &a, const array &b, StreamOrDevice s)
```

Compute integer division. Equivalent to doing floor(a / x).

```cpp
array mlx::core::remainder(const array &a, const array &b, StreamOrDevice s)
```

Compute the element-wise remainder of division

```cpp
array mlx::core::maximum(const array &a, const array &b, StreamOrDevice s)
```

Element-wise maximum between two arrays.

```cpp
array mlx::core::minimum(const array &a, const array &b, StreamOrDevice s)
```

Element-wise minimum between two arrays.

```cpp
array mlx::core::floor(const array &a, StreamOrDevice s)
```

Floor the element of an array. *

```cpp
array mlx::core::ceil(const array &a, StreamOrDevice s)
```

Ceil the element of an array. *

```cpp
array mlx::core::trunc(const array &a, StreamOrDevice s)
```

Truncate the elements of an array towards zero. *

```cpp
array mlx::core::square(const array &a, StreamOrDevice s)
```

Square the elements of an array.

```cpp
array mlx::core::exp(const array &a, StreamOrDevice s)
```

Exponential of the elements of an array.

```cpp
array mlx::core::sin(const array &a, StreamOrDevice s)
```

Sine of the elements of an array

```cpp
array mlx::core::cos(const array &a, StreamOrDevice s)
```

Cosine of the elements of an array

```cpp
array mlx::core::tan(const array &a, StreamOrDevice s)
```

Tangent of the elements of an array

```cpp
array mlx::core::arcsin(const array &a, StreamOrDevice s)
```

Arc Sine of the elements of an array

```cpp
array mlx::core::arccos(const array &a, StreamOrDevice s)
```

Arc Cosine of the elements of an array

```cpp
array mlx::core::arctan(const array &a, StreamOrDevice s)
```

Arc Tangent of the elements of an array

```cpp
array mlx::core::arctan2(const array &a, const array &b, StreamOrDevice s)
```

Inverse tangent of the ratio of two arrays

```cpp
array mlx::core::sinh(const array &a, StreamOrDevice s)
```

Hyperbolic Sine of the elements of an array

```cpp
array mlx::core::cosh(const array &a, StreamOrDevice s)
```

Hyperbolic Cosine of the elements of an array

```cpp
array mlx::core::tanh(const array &a, StreamOrDevice s)
```

Hyperbolic Tangent of the elements of an array

```cpp
array mlx::core::arcsinh(const array &a, StreamOrDevice s)
```

Inverse Hyperbolic Sine of the elements of an array

```cpp
array mlx::core::arccosh(const array &a, StreamOrDevice s)
```

Inverse Hyperbolic Cosine of the elements of an array

```cpp
array mlx::core::arctanh(const array &a, StreamOrDevice s)
```

Inverse Hyperbolic Tangent of the elements of an array

```cpp
array mlx::core::degrees(const array &a, StreamOrDevice s)
```

Convert the elements of an array from Radians to Degrees *

```cpp
array mlx::core::radians(const array &a, StreamOrDevice s)
```

Convert the elements of an array from Degrees to Radians *

```cpp
array mlx::core::log(const array &a, StreamOrDevice s)
```

Natural logarithm of the elements of an array.

```cpp
array mlx::core::log2(const array &a, StreamOrDevice s)
```

Log base 2 of the elements of an array.

```cpp
array mlx::core::log10(const array &a, StreamOrDevice s)
```

Log base 10 of the elements of an array.

```cpp
array mlx::core::log1p(const array &a, StreamOrDevice s)
```

Natural logarithm of one plus elements in the array: log(1 + a).

```cpp
array mlx::core::logaddexp(const array &a, const array &b, StreamOrDevice s)
```

Log-add-exp of one elements in the array: log(exp(a) + exp(b)).

```cpp
array mlx::core::sigmoid(const array &a, StreamOrDevice s)
```

Element-wise logistic sigmoid of the array: 1 / (1 + exp(-x).

```cpp
array mlx::core::erf(const array &a, StreamOrDevice s)
```

Computes the error function of the elements of an array.

```cpp
array mlx::core::erfinv(const array &a, StreamOrDevice s)
```

Computes the inverse error function of the elements of an array.

```cpp
array mlx::core::expm1(const array &a, StreamOrDevice s)
```

Computes the expm1 function of the elements of an array.

```cpp
array mlx::core::stop_gradient(const array &a, StreamOrDevice s)
```

Stop the flow of gradients.

```cpp
array mlx::core::round(const array &a, int decimals, StreamOrDevice s)
```

Round a floating point number

```cpp
array mlx::core::matmul(const array &a, const array &b, StreamOrDevice s)
```

Matrix-matrix multiplication.

```cpp
array mlx::core::gather(const array &a, const std::vector<array> &indices, const std::vector<int> &axes, const Shape &slice_sizes, StreamOrDevice s)
```

Gather array entries given indices and slices

```cpp
array mlx::core::kron(const array &a, const array &b, StreamOrDevice s)
```

Compute the Kronecker product of two arrays.

```cpp
array mlx::core::take(const array &a, const array &indices, int axis, StreamOrDevice s)
```

Take array slices at the given indices of the specified axis.

```cpp
array mlx::core::take(const array &a, const array &indices, StreamOrDevice s)
```

Take array entries at the given indices treating the array as flattened.

```cpp
array mlx::core::take_along_axis(const array &a, const array &indices, int axis, StreamOrDevice s)
```

Take array entries given indices along the axis

```cpp
array mlx::core::put_along_axis(const array &a, const array &indices, const array &values, int axis, StreamOrDevice s)
```

Put the values into the array at the given indices along the axis

```cpp
array mlx::core::scatter_add_axis(const array &a, const array &indices, const array &values, int axis, StreamOrDevice s)
```

Add the values into the array at the given indices along the axis

```cpp
array mlx::core::scatter(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s)
```

Scatter updates to the given indices.

The parameters `indices` and `axes` determine the locations of `a`
that are updated with the values in `updates`. Assuming 1-d `indices`
for simplicity, `indices[i]` are the indices on axis `axes[i]` to which
the values in `updates` will be applied. Note each array in
`indices` is assigned to a corresponding axis and hence `indices.size() ==
axes.size()`. If an index/axis pair is not provided then indices along that
axis are assumed to be zero.

Note the rank of `updates` must be equal to the sum of the rank of the
broadcasted `indices` and the rank of `a`. In other words, assuming the
arrays in `indices` have the same shape, `updates.ndim() ==
indices[0].ndim() + a.ndim()`. The leading dimensions of `updates`
correspond to the indices, and the remaining `a.ndim()` dimensions are the
values that will be applied to the given location in `a`.

For example:

```
auto in = zeros({4, 4}, float32);
auto indices = array({2});
auto updates = reshape(arange(1, 3, float32), {1, 1, 2});
std::vector<int> axes{0};

auto out = scatter(in, {indices}, updates, axes);
```

will produce:

```
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [1, 2, 0, 0],
       [0, 0, 0, 0]], dtype=float32)
```

This scatters the two-element row vector `[1, 2]` starting at the `(2,
0)` position of `a`.

Adding another element to `indices` will scatter into another location of
`a`. We also have to add an another update for the new index:

```
auto in = zeros({4, 4}, float32);
auto indices = array({2, 0});
auto updates = reshape(arange(1, 5, float32), {2, 1, 2});
std::vector<int> axes{0};

auto out = scatter(in, {indices}, updates, axes):
```

will produce:

```
array([[3, 4, 0, 0],
       [0, 0, 0, 0],
       [1, 2, 0, 0],
       [0, 0, 0, 0]], dtype=float32)
```

To control the scatter location on an additional axis, add another index
array to `indices` and another axis to `axes`:

```
auto in = zeros({4, 4}, float32);
auto indices = std::vector{array({2, 0}), array({1, 2})};
auto updates = reshape(arange(1, 5, float32), {2, 1, 2});
std::vector<int> axes{0, 1};

auto out = scatter(in, indices, updates, axes);
```

will produce:

```
array([[0, 0, 3, 4],
      [0, 0, 0, 0],
      [0, 1, 2, 0],
      [0, 0, 0, 0]], dtype=float32)
```

Items in indices are broadcasted together. This means:

```
auto indices = std::vector{array({2, 0}), array({1})};
```

is equivalent to:

```
auto indices = std::vector{array({2, 0}), array({1, 1})};
```

Note, `scatter` does not perform bounds checking on the indices and
updates.  Out-of-bounds accesses on `a` are undefined and typically result
in unintended or invalid memory writes.

```cpp
array mlx::core::scatter_add(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s)
```

Scatter and add updates to given indices

```cpp
array mlx::core::scatter_prod(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s)
```

Scatter and prod updates to given indices

```cpp
array mlx::core::scatter_max(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s)
```

Scatter and max updates to given linear indices

```cpp
array mlx::core::scatter_min(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s)
```

Scatter and min updates to given linear indices

```cpp
array mlx::core::sqrt(const array &a, StreamOrDevice s)
```

Square root the elements of an array.

```cpp
array mlx::core::rsqrt(const array &a, StreamOrDevice s)
```

Square root and reciprocal the elements of an array.

```cpp
array mlx::core::softmax(const array &a, const std::vector<int> &axes, bool precise, StreamOrDevice s)
```

Softmax of an array.

```cpp
array mlx::core::softmax(const array &a, bool precise, StreamOrDevice s)
```

Softmax of an array.

```cpp
inline array mlx::core::softmax(const array &a, int axis, bool precise, StreamOrDevice s)
```

Softmax of an array.

```cpp
array mlx::core::power(const array &a, const array &b, StreamOrDevice s)
```

Raise elements of a to the power of b element-wise

```cpp
array mlx::core::cumsum(const array &a, bool reverse, bool inclusive, std::optional<Dtype> dtype, StreamOrDevice s)
```

Cumulative sum of an array.

```cpp
array mlx::core::cumsum(const array &a, int axis, bool reverse, bool inclusive, std::optional<Dtype> dtype, StreamOrDevice s)
```

Cumulative sum of an array along the given axis.

```cpp
array mlx::core::cumprod(const array &a, bool reverse, bool inclusive, std::optional<Dtype> dtype, StreamOrDevice s)
```

Cumulative product of an array.

```cpp
array mlx::core::cumprod(const array &a, int axis, bool reverse, bool inclusive, std::optional<Dtype> dtype, StreamOrDevice s)
```

Cumulative product of an array along the given axis.

```cpp
array mlx::core::cummax(const array &a, bool reverse, bool inclusive, StreamOrDevice s)
```

Cumulative max of an array.

```cpp
array mlx::core::cummax(const array &a, int axis, bool reverse, bool inclusive, StreamOrDevice s)
```

Cumulative max of an array along the given axis.

```cpp
array mlx::core::cummin(const array &a, bool reverse, bool inclusive, StreamOrDevice s)
```

Cumulative min of an array.

```cpp
array mlx::core::cummin(const array &a, int axis, bool reverse, bool inclusive, StreamOrDevice s)
```

Cumulative min of an array along the given axis.

```cpp
array mlx::core::diff(const array &a, int n, int axis, StreamOrDevice s)
```

The n-th discrete difference along the given axis.

```cpp
array mlx::core::conv_general(array input, array weight, std::vector<int> stride, std::vector<int> padding_lo, std::vector<int> padding_hi, std::vector<int> kernel_dilation, std::vector<int> input_dilation, int groups, bool flip, StreamOrDevice s)
```

General convolution with a filter

```cpp
inline array mlx::core::conv_general(const array &input, const array &weight, std::vector<int> stride, std::vector<int> padding, std::vector<int> kernel_dilation, std::vector<int> input_dilation, int groups, bool flip, StreamOrDevice s)
```

General convolution with a filter

```cpp
array mlx::core::conv1d(const array &input, const array &weight, int stride, int padding, int dilation, int groups, StreamOrDevice s)
```

1D convolution with a filter

```cpp
array mlx::core::conv2d(const array &input, const array &weight, const std::pair<int, int> &stride, const std::pair<int, int> &padding, const std::pair<int, int> &dilation, int groups, StreamOrDevice s)
```

2D convolution with a filter

```cpp
array mlx::core::conv3d(const array &input, const array &weight, const std::tuple<int, int, int> &stride, const std::tuple<int, int, int> &padding, const std::tuple<int, int, int> &dilation, int groups, StreamOrDevice s)
```

3D convolution with a filter

```cpp
array mlx::core::conv_transpose1d(const array &input, const array &weight, int stride, int padding, int dilation, int output_padding, int groups, StreamOrDevice s)
```

1D transposed convolution with a filter

```cpp
array mlx::core::conv_transpose2d(const array &input, const array &weight, const std::pair<int, int> &stride, const std::pair<int, int> &padding, const std::pair<int, int> &dilation, const std::pair<int, int> &output_padding, int groups, StreamOrDevice s)
```

2D transposed convolution with a filter

```cpp
array mlx::core::conv_transpose3d(const array &input, const array &weight, const std::tuple<int, int, int> &stride, const std::tuple<int, int, int> &padding, const std::tuple<int, int, int> &dilation, const std::tuple<int, int, int> &output_padding, int groups, StreamOrDevice s)
```

3D transposed convolution with a filter

```cpp
array mlx::core::quantized_matmul(const array &x, const array &w, const array &scales, const std::optional<array> &biases, bool transpose, std::optional<int> group_size, std::optional<int> bits, const std::string &mode, StreamOrDevice s)
```

Quantized matmul multiplies x with a quantized matrix w

```cpp
std::vector<array> mlx::core::quantize(const array &w, std::optional<int> group_size, std::optional<int> bits, const std::string &mode, const std::optional<array> &global_scale, StreamOrDevice s)
```

Quantize a matrix along its last axis

```cpp
array mlx::core::dequantize(const array &w, const array &scales, const std::optional<array> &biases, std::optional<int> group_size, std::optional<int> bits, const std::string &mode, const std::optional<array> &global_scale, std::optional<Dtype> dtype, StreamOrDevice s)
```

Dequantize a matrix produced by quantize()

```cpp
array mlx::core::from_fp8(array x, Dtype dtype, StreamOrDevice s)
```

Convert an E4M3 float8 to the given floating point dtype.

```cpp
array mlx::core::to_fp8(array x, StreamOrDevice s)
```

Convert a floating point matrix to E4M3 float8.

```cpp
array mlx::core::gather_qmm(const array &x, const array &w, const array &scales, const std::optional<array> &biases, std::optional<array> lhs_indices, std::optional<array> rhs_indices, bool transpose, std::optional<int> group_size, std::optional<int> bits, const std::string &mode, const std::optional<array> &global_scale, bool sorted_indices, StreamOrDevice s)
```

Compute matrix products with matrix-level gather.

```cpp
array mlx::core::tensordot(const array &a, const array &b, const int axis, StreamOrDevice s)
```

Returns a contraction of a and b over multiple dimensions.

```cpp
array mlx::core::outer(const array &a, const array &b, StreamOrDevice s)
```

Compute the outer product of two vectors.

```cpp
array mlx::core::inner(const array &a, const array &b, StreamOrDevice s)
```

Compute the inner product of two vectors.

```cpp
array mlx::core::vecdot(const array &a, const array &b, int axis, StreamOrDevice s)
```

Compute a vector dot product along an axis.

```cpp
array mlx::core::addmm(array c, array a, array b, const float &alpha, const float &beta, StreamOrDevice s)
```

Compute D = beta * C + alpha * (A @ B)

```cpp
array mlx::core::block_masked_mm(array a, array b, int block_size, std::optional<array> mask_out, std::optional<array> mask_lhs, std::optional<array> mask_rhs, StreamOrDevice s)
```

Compute matrix product with block masking

```cpp
array mlx::core::gather_mm(array a, array b, std::optional<array> lhs_indices, std::optional<array> rhs_indices, bool sorted_indices, StreamOrDevice s)
```

Compute matrix product with matrix-level gather

```cpp
array mlx::core::segmented_mm(array a, array b, array segments, StreamOrDevice s)
```

Compute a matrix product but segment the inner dimension and write the
result separately for each segment.

```cpp
array mlx::core::diagonal(const array &a, int offset, int axis1, int axis2, StreamOrDevice s)
```

Extract a diagonal or construct a diagonal array

```cpp
array mlx::core::diag(const array &a, int k, StreamOrDevice s)
```

Extract diagonal from a 2d array or create a diagonal matrix.

```cpp
array mlx::core::trace(const array &a, int offset, int axis1, int axis2, Dtype dtype, StreamOrDevice s)
```

Return the sum along a specified diagonal in the given array.

```cpp
std::vector<array> mlx::core::depends(const std::vector<array> &inputs, const std::vector<array> &dependencies)
```

Implements the identity function but allows injecting dependencies to other
arrays. This ensures that these other arrays will have been computed
when the outputs of this function are computed.

```cpp
array mlx::core::atleast_1d(const array &a, StreamOrDevice s)
```

convert an array to an atleast ndim array

```cpp
array mlx::core::number_of_elements(const array &a, std::vector<int> axes, bool inverted, Dtype dtype, StreamOrDevice s)
```

Extract the number of elements along some axes as a scalar array. Used to
allow shape dependent shapeless compilation (pun intended).

```cpp
array mlx::core::bitwise_and(const array &a, const array &b, StreamOrDevice s)
```

Bitwise and.

```cpp
array mlx::core::bitwise_or(const array &a, const array &b, StreamOrDevice s)
```

Bitwise inclusive or.

```cpp
array mlx::core::bitwise_xor(const array &a, const array &b, StreamOrDevice s)
```

Bitwise exclusive or.

```cpp
array mlx::core::left_shift(const array &a, const array &b, StreamOrDevice s)
```

Shift bits to the left.

```cpp
array mlx::core::right_shift(const array &a, const array &b, StreamOrDevice s)
```

Shift bits to the right.

```cpp
array mlx::core::bitwise_invert(const array &a, StreamOrDevice s)
```

Invert the bits.

```cpp
array mlx::core::roll(const array &a, int shift, StreamOrDevice s)
```

Roll elements along an axis and introduce them on the other side
