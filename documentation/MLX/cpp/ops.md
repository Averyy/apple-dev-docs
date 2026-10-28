---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/cpp/ops.html
---

# Operations

```cpp
array arange(double start, double stop, double step, Dtype dtype, StreamOrDevice s = {})
```

A 1D array of numbers starting at `start` (optional), stopping at stop, stepping by `step` (optional).

```cpp
array arange(double start, double stop, double step, StreamOrDevice s = {})
```

```cpp
array arange(double start, double stop, Dtype dtype, StreamOrDevice s = {})
```

```cpp
array arange(double start, double stop, StreamOrDevice s = {})
```

```cpp
array arange(double stop, Dtype dtype, StreamOrDevice s = {})
```

```cpp
array arange(double stop, StreamOrDevice s = {})
```

```cpp
array arange(int start, int stop, int step, StreamOrDevice s = {})
```

```cpp
array arange(int start, int stop, StreamOrDevice s = {})
```

```cpp
array arange(int stop, StreamOrDevice s = {})
```

```cpp
array linspace(double start, double stop, int num, bool endpoint, Dtype dtype = float32, StreamOrDevice s = {})
```

A 1D array of `num` evenly spaced numbers in the range `[start, stop]`, or in the half-open range `[start, stop)` when `endpoint` is false.

```cpp
inline array linspace(double start, double stop, int num = 50, Dtype dtype = float32, StreamOrDevice s = {})
```

```cpp
array astype(array a, Dtype dtype, StreamOrDevice s = {})
```

Convert an array to the given data type.

```cpp
array as_strided(array a, Shape shape, Strides strides, size_t offset, StreamOrDevice s = {})
```

Create a view of an array with the given shape and strides.

```cpp
array copy(array a, StreamOrDevice s = {})
```

Copy another array.

```cpp
array full(Shape shape, array vals, Dtype dtype, StreamOrDevice s = {})
```

Fill an array of the given shape with the given value(s).

```cpp
array full(Shape shape, array vals, StreamOrDevice s = {})
```

```cpp
template<typename T>
array full(Shape shape, T val, Dtype dtype, StreamOrDevice s = {})
```

```cpp
template<typename T>
array full(Shape shape, T val, StreamOrDevice s = {})
```

```cpp
array full_like(const array &a, array vals, Dtype dtype, StreamOrDevice s = {})
```

```cpp
array full_like(const array &a, array vals, StreamOrDevice s = {})
```

```cpp
template<typename T>
array full_like(const array &a, T val, Dtype dtype, StreamOrDevice s = {})
```

```cpp
template<typename T>
array full_like(const array &a, T val, StreamOrDevice s = {})
```

```cpp
array zeros(const Shape &shape, Dtype dtype, StreamOrDevice s = {})
```

Fill an array of the given shape with zeros.

```cpp
inline array zeros(const Shape &shape, StreamOrDevice s = {})
```

```cpp
array zeros_like(const array &a, StreamOrDevice s = {})
```

Create an array of zeros with the shape of `a`.

```cpp
array zeros_like(const array &a, Dtype dtype, StreamOrDevice s = {})
```

```cpp
array ones(const Shape &shape, Dtype dtype, StreamOrDevice s = {})
```

Fill an array of the given shape with ones.

```cpp
inline array ones(const Shape &shape, StreamOrDevice s = {})
```

```cpp
array ones_like(const array &a, StreamOrDevice s = {})
```

Create an array of ones with the shape of `a`.

```cpp
array ones_like(const array &a, Dtype dtype, StreamOrDevice s = {})
```

```cpp
array eye(int n, int m, int k, Dtype dtype, StreamOrDevice s = {})
```

Fill an array of the given shape (n,m) with ones in the specified diagonal k, and zeros everywhere else.

```cpp
inline array eye(int n, Dtype dtype, StreamOrDevice s = {})
```

```cpp
inline array eye(int n, int m, StreamOrDevice s = {})
```

```cpp
inline array eye(int n, int m, int k, StreamOrDevice s = {})
```

```cpp
inline array eye(int n, StreamOrDevice s = {})
```

```cpp
array identity(int n, Dtype dtype, StreamOrDevice s = {})
```

Create a square matrix of shape (n,n) of zeros, and ones in the major diagonal.

```cpp
inline array identity(int n, StreamOrDevice s = {})
```

```cpp
array tri(int n, int m, int k, Dtype type, StreamOrDevice s = {})
```

```cpp
inline array tri(int n, Dtype type, StreamOrDevice s = {})
```

```cpp
array tril(array x, int k = 0, StreamOrDevice s = {})
```

```cpp
array triu(array x, int k = 0, StreamOrDevice s = {})
```

```cpp
array reshape(const array &a, Shape shape, StreamOrDevice s = {})
```

Reshape an array to the given shape.

```cpp
array unflatten(const array &a, int axis, Shape shape, StreamOrDevice s = {})
```

Unflatten the axis to the given shape.

```cpp
array flatten(const array &a, int start_axis, int end_axis = -1, StreamOrDevice s = {})
```

Flatten the dimensions in the range `[start_axis, end_axis]` .

```cpp
array flatten(const array &a, StreamOrDevice s = {})
```

Flatten the array to 1D.

```cpp
array hadamard_transform(const array &a, std::optional<float> scale = std::nullopt, StreamOrDevice s = {})
```

Multiply the array by the Hadamard matrix of corresponding size.

```cpp
array squeeze(const array &a, const std::vector<int> &axes, StreamOrDevice s = {})
```

Remove singleton dimensions at the given axes.

```cpp
array squeeze(const array &a, int axis, StreamOrDevice s = {})
```

Remove singleton dimensions at the given axis.

```cpp
array squeeze(const array &a, StreamOrDevice s = {})
```

Remove all singleton dimensions.

```cpp
array expand_dims(const array &a, const std::vector<int> &axes, StreamOrDevice s = {})
```

Add a singleton dimension at the given axes.

```cpp
array expand_dims(const array &a, int axis, StreamOrDevice s = {})
```

Add a singleton dimension at the given axis.

```cpp
array flip(const array &a, const std::vector<int> &axes, StreamOrDevice s = {})
```

Reverse the order of the elements along the given axes.

```cpp
array flip(const array &a, int axis, StreamOrDevice s = {})
```

Reverse the order of the elements along the given axis.

```cpp
array flip(const array &a, StreamOrDevice s = {})
```

Reverse the order of the elements along all axes.

```cpp
array slice(const array &a, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})
```

Slice an array.

```cpp
inline array slice(const array &a, std::initializer_list<int> start, Shape stop, Shape strides, StreamOrDevice s = {})
```

```cpp
array slice(const array &a, Shape start, Shape stop, StreamOrDevice s = {})
```

Slice an array with a stride of 1 in each dimension.

```cpp
array slice(const array &a, const array &start, std::vector<int> axes, Shape slice_size, StreamOrDevice s = {})
```

Slice an array with dynamic starting indices.

```cpp
array slice_update(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})
```

Update a slice from the source array.

```cpp
array slice_update(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})
```

Update a slice from the source array with stride 1 in each dimension.

```cpp
array slice_update(const array &src, const array &update, const array &start, std::vector<int> axes, StreamOrDevice s = {})
```

Update a slice from the source array with dynamic starting indices.

```cpp
array slice_update_add(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})
```

Slice update and add updates to given slice.

```cpp
array slice_update_add(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})
```

Slice update and add updates to given slice with stride 1 in each dimension.

```cpp
array slice_update_prod(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})
```

Slice update and prod updates to given slice.

```cpp
array slice_update_prod(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})
```

Slice update and prod updates to given slice with stride 1 in each dimension.

```cpp
array slice_update_max(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})
```

Slice update and max updates to given slice.

```cpp
array slice_update_max(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})
```

Slice update and max updates to given slice with stride 1 in each dimension.

```cpp
array slice_update_min(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})
```

Slice update and min updates to given slice.

```cpp
array slice_update_min(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})
```

Slice update and min updates to given slice with stride 1 in each dimension.

```cpp
std::vector<array> split(const array &a, int num_splits, int axis, StreamOrDevice s = {})
```

Split an array into sub-arrays along a given axis.

```cpp
std::vector<array> split(const array &a, int num_splits, StreamOrDevice s = {})
```

```cpp
std::vector<array> split(const array &a, const Shape &indices, int axis, StreamOrDevice s = {})
```

```cpp
std::vector<array> split(const array &a, const Shape &indices, StreamOrDevice s = {})
```

```cpp
std::vector<array> unstack(const array &a, int axis, StreamOrDevice s = {})
```

Split an array into a sequence of arrays along an axis, removing it.

```cpp
std::vector<array> unstack(const array &a, StreamOrDevice s = {})
```

```cpp
std::vector<array> meshgrid(const std::vector<array> &arrays, bool sparse = false, const std::string &indexing = "xy", StreamOrDevice s = {})
```

A vector of coordinate arrays from coordinate vectors.

```cpp
array clip(const array &a, const std::optional<array> &a_min = std::nullopt, const std::optional<array> &a_max = std::nullopt, StreamOrDevice s = {})
```

Clip (limit) the values in an array.

```cpp
array concatenate(std::vector<array> arrays, int axis, StreamOrDevice s = {})
```

Concatenate arrays along a given axis.

```cpp
array concatenate(std::vector<array> arrays, StreamOrDevice s = {})
```

```cpp
array stack(const std::vector<array> &arrays, int axis, StreamOrDevice s = {})
```

Stack arrays along a new axis.

```cpp
array stack(const std::vector<array> &arrays, StreamOrDevice s = {})
```

```cpp
array repeat(const array &arr, int repeats, int axis, StreamOrDevice s = {})
```

Repeat an array along an axis.

```cpp
array repeat(const array &arr, int repeats, StreamOrDevice s = {})
```

```cpp
array tile(const array &arr, std::vector<int> reps, StreamOrDevice s = {})
```

```cpp
array transpose(const array &a, std::vector<int> axes, StreamOrDevice s = {})
```

Permutes the dimensions according to the given axes.

```cpp
inline array transpose(const array &a, std::initializer_list<int> axes, StreamOrDevice s = {})
```

```cpp
array matrix_transpose(const array &a, StreamOrDevice s = {})
```

Permutes last two dimensions of an array.

```cpp
array swapaxes(const array &a, int axis1, int axis2, StreamOrDevice s = {})
```

Swap two axes of an array.

```cpp
array moveaxis(const array &a, int source, int destination, StreamOrDevice s = {})
```

Move an axis of an array.

```cpp
array pad(const array &a, const std::vector<int> &axes, const Shape &low_pad_size, const Shape &high_pad_size, const array &pad_value = array(0), const std::string &mode = "constant", StreamOrDevice s = {})
```

Pad an array with a constant value.

```cpp
array pad(const array &a, const std::vector<std::pair<int, int>> &pad_width, const array &pad_value = array(0), const std::string &mode = "constant", StreamOrDevice s = {})
```

Pad an array with a constant value along all axes.

```cpp
array pad(const array &a, const std::pair<int, int> &pad_width, const array &pad_value = array(0), const std::string &mode = "constant", StreamOrDevice s = {})
```

```cpp
array pad(const array &a, int pad_width, const array &pad_value = array(0), const std::string &mode = "constant", StreamOrDevice s = {})
```

```cpp
array transpose(const array &a, StreamOrDevice s = {})
```

Permutes the dimensions in reverse order.

```cpp
array broadcast_to(const array &a, const Shape &shape, StreamOrDevice s = {})
```

Broadcast an array to a given shape.

```cpp
std::vector<array> broadcast_arrays(const std::vector<array> &inputs, StreamOrDevice s = {})
```

Broadcast a vector of arrays against one another.

```cpp
array equal(const array &a, const array &b, StreamOrDevice s = {})
```

Returns the bool array with (a == b) element-wise.

```cpp
inline array operator==(const array &a, const array &b)
```

```cpp
template<typename T>
array operator==(T a, const array &b)
```

```cpp
template<typename T>
array operator==(const array &a, T b)
```

```cpp
array not_equal(const array &a, const array &b, StreamOrDevice s = {})
```

Returns the bool array with (a != b) element-wise.

```cpp
inline array operator!=(const array &a, const array &b)
```

```cpp
template<typename T>
array operator!=(T a, const array &b)
```

```cpp
template<typename T>
array operator!=(const array &a, T b)
```

```cpp
array greater(const array &a, const array &b, StreamOrDevice s = {})
```

Returns bool array with (a > b) element-wise.

```cpp
inline array operator>(const array &a, const array &b)
```

```cpp
template<typename T>
array operator>(T a, const array &b)
```

```cpp
template<typename T>
array operator>(const array &a, T b)
```

```cpp
array greater_equal(const array &a, const array &b, StreamOrDevice s = {})
```

Returns bool array with (a >= b) element-wise.

```cpp
inline array operator>=(const array &a, const array &b)
```

```cpp
template<typename T>
array operator>=(T a, const array &b)
```

```cpp
template<typename T>
array operator>=(const array &a, T b)
```

```cpp
array less(const array &a, const array &b, StreamOrDevice s = {})
```

Returns bool array with (a < b) element-wise.

```cpp
inline array operator<(const array &a, const array &b)
```

```cpp
template<typename T>
array operator<(T a, const array &b)
```

```cpp
template<typename T>
array operator<(const array &a, T b)
```

```cpp
array less_equal(const array &a, const array &b, StreamOrDevice s = {})
```

Returns bool array with (a <= b) element-wise.

```cpp
inline array operator<=(const array &a, const array &b)
```

```cpp
template<typename T>
array operator<=(T a, const array &b)
```

```cpp
template<typename T>
array operator<=(const array &a, T b)
```

```cpp
array array_equal(const array &a, const array &b, bool equal_nan, StreamOrDevice s = {})
```

True if two arrays have the same shape and elements.

```cpp
inline array array_equal(const array &a, const array &b, StreamOrDevice s = {})
```

```cpp
array isnan(const array &a, StreamOrDevice s = {})
```

```cpp
array isinf(const array &a, StreamOrDevice s = {})
```

```cpp
array isfinite(const array &a, StreamOrDevice s = {})
```

```cpp
array isposinf(const array &a, StreamOrDevice s = {})
```

```cpp
array isneginf(const array &a, StreamOrDevice s = {})
```

```cpp
array where(const array &condition, const array &x, const array &y, StreamOrDevice s = {})
```

Select from x or y depending on condition.

```cpp
array nan_to_num(const array &a, float nan = 0.0f, const std::optional<float> posinf = std::nullopt, const std::optional<float> neginf = std::nullopt, StreamOrDevice s = {})
```

Replace NaN and infinities with finite numbers.

```cpp
array all(const array &a, bool keepdims, StreamOrDevice s = {})
```

True if all elements in the array are true (or non-zero).

```cpp
inline array all(const array &a, StreamOrDevice s = {})
```

```cpp
array allclose(const array &a, const array &b, double rtol = 1e-5, double atol = 1e-8, bool equal_nan = false, StreamOrDevice s = {})
```

True if the two arrays are equal within the specified tolerance.

```cpp
array isclose(const array &a, const array &b, double rtol = 1e-5, double atol = 1e-8, bool equal_nan = false, StreamOrDevice s = {})
```

Returns a boolean array where two arrays are element-wise equal within the specified tolerance.

```cpp
array all(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

Reduces the input along the given axes.

An output value is true if all the corresponding inputs are true.

```cpp
array all(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

Reduces the input along the given axis.

An output value is true if all the corresponding inputs are true.

```cpp
array any(const array &a, bool keepdims, StreamOrDevice s = {})
```

True if any elements in the array are true (or non-zero).

```cpp
inline array any(const array &a, StreamOrDevice s = {})
```

```cpp
array any(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

Reduces the input along the given axes.

An output value is true if any of the corresponding inputs are true.

```cpp
array any(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

Reduces the input along the given axis.

An output value is true if any of the corresponding inputs are true.

```cpp
array sum(const array &a, bool keepdims, StreamOrDevice s = {})
```

Sums the elements of an array.

```cpp
inline array sum(const array &a, StreamOrDevice s = {})
```

```cpp
array sum(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

Sums the elements of an array along the given axes.

```cpp
array sum(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

Sums the elements of an array along the given axis.

```cpp
array count_nonzero(const array &a, bool keepdims = false, StreamOrDevice s = {})
```

Count the number of non-zero elements in an array.

```cpp
array count_nonzero(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

```cpp
array count_nonzero(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

```cpp
array mean(const array &a, bool keepdims, StreamOrDevice s = {})
```

Computes the mean of the elements of an array.

```cpp
inline array mean(const array &a, StreamOrDevice s = {})
```

```cpp
array mean(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

Computes the mean of the elements of an array along the given axes.

```cpp
array mean(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

Computes the mean of the elements of an array along the given axis.

```cpp
array median(const array &a, bool keepdims, StreamOrDevice s = {})
```

Computes the median of the elements of an array.

```cpp
inline array median(const array &a, StreamOrDevice s = {})
```

```cpp
array median(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

Computes the median of the elements of an array along the given axes.

```cpp
array median(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

Computes the median of the elements of an array along the given axis.

```cpp
array var(const array &a, bool keepdims, int ddof = 0, StreamOrDevice s = {})
```

Computes the variance of the elements of an array.

```cpp
inline array var(const array &a, StreamOrDevice s = {})
```

```cpp
array var(const array &a, const std::vector<int> &axes, bool keepdims = false, int ddof = 0, StreamOrDevice s = {})
```

Computes the variance of the elements of an array along the given axes.

```cpp
array var(const array &a, int axis, bool keepdims = false, int ddof = 0, StreamOrDevice s = {})
```

Computes the variance of the elements of an array along the given axis.

```cpp
array std(const array &a, bool keepdims, int ddof = 0, StreamOrDevice s = {})
```

Computes the standard deviation of the elements of an array.

```cpp
inline array std(const array &a, StreamOrDevice s = {})
```

```cpp
array std(const array &a, const std::vector<int> &axes, bool keepdims = false, int ddof = 0, StreamOrDevice s = {})
```

Computes the standard deviation of the elements of an array along the given axes.

```cpp
array std(const array &a, int axis, bool keepdims = false, int ddof = 0, StreamOrDevice s = {})
```

Computes the standard deviation of the elements of an array along the given axis.

```cpp
array prod(const array &a, bool keepdims, StreamOrDevice s = {})
```

The product of all elements of the array.

```cpp
inline array prod(const array &a, StreamOrDevice s = {})
```

```cpp
array prod(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

The product of the elements of an array along the given axes.

```cpp
array prod(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

The product of the elements of an array along the given axis.

```cpp
array max(const array &a, bool keepdims, StreamOrDevice s = {})
```

The maximum of all elements of the array.

```cpp
inline array max(const array &a, StreamOrDevice s = {})
```

```cpp
array max(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

The maximum of the elements of an array along the given axes.

```cpp
array max(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

The maximum of the elements of an array along the given axis.

```cpp
array min(const array &a, bool keepdims, StreamOrDevice s = {})
```

The minimum of all elements of the array.

```cpp
inline array min(const array &a, StreamOrDevice s = {})
```

```cpp
array min(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

The minimum of the elements of an array along the given axes.

```cpp
array min(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

The minimum of the elements of an array along the given axis.

```cpp
std::tuple<array, array> minmax(const array &a, bool keepdims, StreamOrDevice s = {})
```

```cpp
inline std::tuple<array, array> minmax(const array &a, StreamOrDevice s = {})
```

```cpp
std::tuple<array, array> minmax(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

The minimum and maximum of the elements of an array along the given axes.

```cpp
std::tuple<array, array> minmax(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

The minimum and maximum of the elements of an array along the given axis.

```cpp
array hanning(int M, StreamOrDevice s = {})
```

Returns the Hanning window of size M.

```cpp
array hamming(int M, StreamOrDevice s = {})
```

Returns the Hamming window of size M.

```cpp
array bartlett(int M, StreamOrDevice s = {})
```

Returns the bartlett window of size M.

```cpp
array blackman(int M, StreamOrDevice s = {})
```

Returns the Blackmann window of size M.

```cpp
array argmin(const array &a, bool keepdims, StreamOrDevice s = {})
```

Returns the index of the minimum value in the array.

```cpp
inline array argmin(const array &a, StreamOrDevice s = {})
```

```cpp
array argmin(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

Returns the indices of the minimum values along a given axis.

```cpp
array argmax(const array &a, bool keepdims, StreamOrDevice s = {})
```

Returns the index of the maximum value in the array.

```cpp
inline array argmax(const array &a, StreamOrDevice s = {})
```

```cpp
array argmax(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

Returns the indices of the maximum values along a given axis.

```cpp
array sort(const array &a, StreamOrDevice s = {})
```

Returns a sorted copy of the flattened array.

The sort is stable and NaN values are placed at the end.

```cpp
array sort(const array &a, int axis, StreamOrDevice s = {})
```

Returns a sorted copy of the array along a given axis.

The sort is stable and NaN values are placed at the end.

```cpp
array argsort(const array &a, StreamOrDevice s = {})
```

Returns indices that sort the flattened array.

The sort is stable and NaN values are placed at the end.

```cpp
array argsort(const array &a, int axis, StreamOrDevice s = {})
```

Returns indices that sort the array along a given axis.

The sort is stable and NaN values are placed at the end.

```cpp
array partition(const array &a, int kth, StreamOrDevice s = {})
```

Returns a partitioned copy of the flattened array such that the smaller kth elements are first.

```cpp
array partition(const array &a, int kth, int axis, StreamOrDevice s = {})
```

Returns a partitioned copy of the array along a given axis such that the smaller kth elements are first.

```cpp
array argpartition(const array &a, int kth, StreamOrDevice s = {})
```

Returns indices that partition the flattened array such that the smaller kth elements are first.

```cpp
array argpartition(const array &a, int kth, int axis, StreamOrDevice s = {})
```

Returns indices that partition the array along a given axis such that the smaller kth elements are first.

```cpp
array searchsorted(const array &sorted_sequence, const array &values, const std::string &side = "left", StreamOrDevice s = {})
```

Find the indices of `values` in `sorted_sequence`.

```cpp
array topk(const array &a, int k, StreamOrDevice s = {})
```

Returns topk elements of the flattened array.

```cpp
array topk(const array &a, int k, int axis, StreamOrDevice s = {})
```

Returns topk elements of the array along a given axis.

```cpp
std::vector<array> unique(const array &a, int size, bool return_index = false, bool return_inverse = false, bool return_counts = false, const std::optional<array> &fill_value = std::nullopt, StreamOrDevice s = {})
```

Returns the sorted unique elements of the flattened array, and optionally the index of the first occurrence of each, the inverse indices and the counts.

The output has the given size, and is truncated if `size` is smaller than the number of unique values. If `size` is larger, the result is padded with `fill_value`, or the first of the sorted unique values if no fill value is provided. An empty input has none, so it throws unless `size` is zero or a fill value is given. A truncated output loses the counts of the values it drops, and its inverse indices are clamped to the last entry.

```cpp
array logcumsumexp(const array &a, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})
```

Cumulative logsumexp of an array.

```cpp
array logcumsumexp(const array &a, int axis, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})
```

Cumulative logsumexp of an array along the given axis.

```cpp
array logsumexp(const array &a, bool keepdims, StreamOrDevice s = {})
```

The logsumexp of all elements of the array.

```cpp
inline array logsumexp(const array &a, StreamOrDevice s = {})
```

```cpp
array logsumexp(const array &a, const std::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})
```

The logsumexp of the elements of an array along the given axes.

```cpp
array logsumexp(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})
```

The logsumexp of the elements of an array along the given axis.

```cpp
array abs(const array &a, StreamOrDevice s = {})
```

Absolute value of elements in an array.

```cpp
array positive(const array &a, StreamOrDevice s = {})
```

Unary plus — return a copy of the array unchanged.

```cpp
array negative(const array &a, StreamOrDevice s = {})
```

Negate an array.

```cpp
array operator-(const array &a)
```

```cpp
array sign(const array &a, StreamOrDevice s = {})
```

The sign of the elements in an array.

```cpp
array logical_not(const array &a, StreamOrDevice s = {})
```

Logical not of an array.

```cpp
array logical_and(const array &a, const array &b, StreamOrDevice s = {})
```

Logical and of two arrays.

```cpp
array operator&&(const array &a, const array &b)
```

```cpp
array logical_or(const array &a, const array &b, StreamOrDevice s = {})
```

Logical or of two arrays.

```cpp
array operator||(const array &a, const array &b)
```

```cpp
array logical_xor(const array &a, const array &b, StreamOrDevice s = {})
```

Logical exclusive or of two arrays.

```cpp
array reciprocal(const array &a, StreamOrDevice s = {})
```

The reciprocal (1/x) of the elements in an array.

```cpp
array add(const array &a, const array &b, StreamOrDevice s = {})
```

Add two arrays.

```cpp
array operator+(const array &a, const array &b)
```

```cpp
template<typename T>
array operator+(T a, const array &b)
```

```cpp
template<typename T>
array operator+(const array &a, T b)
```

```cpp
array subtract(const array &a, const array &b, StreamOrDevice s = {})
```

Subtract two arrays.

```cpp
array operator-(const array &a, const array &b)
```

```cpp
template<typename T>
array operator-(T a, const array &b)
```

```cpp
template<typename T>
array operator-(const array &a, T b)
```

```cpp
array multiply(const array &a, const array &b, StreamOrDevice s = {})
```

Multiply two arrays.

```cpp
array operator*(const array &a, const array &b)
```

```cpp
template<typename T>
array operator*(T a, const array &b)
```

```cpp
template<typename T>
array operator*(const array &a, T b)
```

```cpp
array divide(const array &a, const array &b, StreamOrDevice s = {})
```

Divide two arrays.

```cpp
array operator/(const array &a, const array &b)
```

```cpp
array operator/(double a, const array &b)
```

```cpp
array operator/(const array &a, double b)
```

```cpp
std::vector<array> divmod(const array &a, const array &b, StreamOrDevice s = {})
```

Compute the element-wise quotient and remainder.

```cpp
array floor_divide(const array &a, const array &b, StreamOrDevice s = {})
```

Compute integer division.

Equivalent to doing floor(a / x).

```cpp
array remainder(const array &a, const array &b, StreamOrDevice s = {})
```

Compute the element-wise remainder of division.

```cpp
array operator%(const array &a, const array &b)
```

```cpp
template<typename T>
array operator%(T a, const array &b)
```

```cpp
template<typename T>
array operator%(const array &a, T b)
```

```cpp
array maximum(const array &a, const array &b, StreamOrDevice s = {})
```

Element-wise maximum between two arrays.

```cpp
array minimum(const array &a, const array &b, StreamOrDevice s = {})
```

Element-wise minimum between two arrays.

```cpp
array floor(const array &a, StreamOrDevice s = {})
```

Floor the element of an array.

```cpp
array ceil(const array &a, StreamOrDevice s = {})
```

Ceil the element of an array.

```cpp
array trunc(const array &a, StreamOrDevice s = {})
```

Truncate the elements of an array towards zero.

```cpp
array square(const array &a, StreamOrDevice s = {})
```

Square the elements of an array.

```cpp
array exp(const array &a, StreamOrDevice s = {})
```

Exponential of the elements of an array.

```cpp
array sin(const array &a, StreamOrDevice s = {})
```

Sine of the elements of an array.

```cpp
array cos(const array &a, StreamOrDevice s = {})
```

Cosine of the elements of an array.

```cpp
array tan(const array &a, StreamOrDevice s = {})
```

Tangent of the elements of an array.

```cpp
array arcsin(const array &a, StreamOrDevice s = {})
```

Arc Sine of the elements of an array.

```cpp
array arccos(const array &a, StreamOrDevice s = {})
```

Arc Cosine of the elements of an array.

```cpp
array arctan(const array &a, StreamOrDevice s = {})
```

Arc Tangent of the elements of an array.

```cpp
array arctan2(const array &a, const array &b, StreamOrDevice s = {})
```

Inverse tangent of the ratio of two arrays.

```cpp
array sinh(const array &a, StreamOrDevice s = {})
```

Hyperbolic Sine of the elements of an array.

```cpp
array cosh(const array &a, StreamOrDevice s = {})
```

Hyperbolic Cosine of the elements of an array.

```cpp
array tanh(const array &a, StreamOrDevice s = {})
```

Hyperbolic Tangent of the elements of an array.

```cpp
array arcsinh(const array &a, StreamOrDevice s = {})
```

Inverse Hyperbolic Sine of the elements of an array.

```cpp
array arccosh(const array &a, StreamOrDevice s = {})
```

Inverse Hyperbolic Cosine of the elements of an array.

```cpp
array arctanh(const array &a, StreamOrDevice s = {})
```

Inverse Hyperbolic Tangent of the elements of an array.

```cpp
array degrees(const array &a, StreamOrDevice s = {})
```

Convert the elements of an array from Radians to Degrees.

```cpp
array radians(const array &a, StreamOrDevice s = {})
```

Convert the elements of an array from Degrees to Radians.

```cpp
array log(const array &a, StreamOrDevice s = {})
```

Natural logarithm of the elements of an array.

```cpp
array log2(const array &a, StreamOrDevice s = {})
```

Log base 2 of the elements of an array.

```cpp
array log10(const array &a, StreamOrDevice s = {})
```

Log base 10 of the elements of an array.

```cpp
array log1p(const array &a, StreamOrDevice s = {})
```

Natural logarithm of one plus elements in the array: `log(1 + a)`.

```cpp
array logaddexp(const array &a, const array &b, StreamOrDevice s = {})
```

Log-add-exp of one elements in the array: `log(exp(a) + exp(b))`.

```cpp
array sigmoid(const array &a, StreamOrDevice s = {})
```

Element-wise logistic sigmoid of the array: `1 / (1 + exp(-x)`.

```cpp
array erf(const array &a, StreamOrDevice s = {})
```

Computes the error function of the elements of an array.

```cpp
array erfinv(const array &a, StreamOrDevice s = {})
```

Computes the inverse error function of the elements of an array.

```cpp
array expm1(const array &a, StreamOrDevice s = {})
```

Computes the expm1 function of the elements of an array.

```cpp
array stop_gradient(const array &a, StreamOrDevice s = {})
```

Stop the flow of gradients.

```cpp
array round(const array &a, int decimals, StreamOrDevice s = {})
```

Round a floating point number.

```cpp
inline array round(const array &a, StreamOrDevice s = {})
```

```cpp
array matmul(const array &a, const array &b, StreamOrDevice s = {})
```

Matrix-matrix multiplication.

```cpp
array gather(const array &a, const std::vector<array> &indices, const std::vector<int> &axes, const Shape &slice_sizes, StreamOrDevice s = {})
```

Gather array entries given indices and slices.

```cpp
inline array gather(const array &a, const array &indices, int axis, const Shape &slice_sizes, StreamOrDevice s = {})
```

```cpp
array kron(const array &a, const array &b, StreamOrDevice s = {})
```

Compute the Kronecker product of two arrays.

```cpp
array take(const array &a, const array &indices, int axis, StreamOrDevice s = {})
```

Take array slices at the given indices of the specified axis.

```cpp
array take(const array &a, int index, int axis, StreamOrDevice s = {})
```

```cpp
array take(const array &a, const array &indices, StreamOrDevice s = {})
```

Take array entries at the given indices treating the array as flattened.

```cpp
array take(const array &a, int index, StreamOrDevice s = {})
```

```cpp
array take_along_axis(const array &a, const array &indices, int axis, StreamOrDevice s = {})
```

Take array entries given indices along the axis.

```cpp
array put_along_axis(const array &a, const array &indices, const array &values, int axis, StreamOrDevice s = {})
```

Put the values into the array at the given indices along the axis.

```cpp
array scatter_add_axis(const array &a, const array &indices, const array &values, int axis, StreamOrDevice s = {})
```

Add the values into the array at the given indices along the axis.

```cpp
array scatter(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s = {})
```

Scatter updates to the given indices.

The parameters `indices` and `axes` determine the locations of `a` that are updated with the values in `updates`. Assuming 1-d `indices` for simplicity, `indices[i]` are the indices on axis `axes[i]` to which the values in `updates` will be applied. Note each array in `indices` is assigned to a corresponding axis and hence `indices.size() == axes.size()`. If an index/axis pair is not provided then indices along that axis are assumed to be zero.

Note the rank of `updates` must be equal to the sum of the rank of the broadcasted `indices` and the rank of `a`. In other words, assuming the arrays in `indices` have the same shape, `updates.ndim() == indices[0].ndim() + a.ndim()`. The leading dimensions of `updates` correspond to the indices, and the remaining `a.ndim()` dimensions are the values that will be applied to the given location in `a`.

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

This scatters the two-element row vector `[1, 2]` starting at the `(2, 0)` position of `a`.

Adding another element to `indices` will scatter into another location of `a`. We also have to add an another update for the new index:

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

To control the scatter location on an additional axis, add another index array to `indices` and another axis to `axes`:

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

Note, `scatter` does not perform bounds checking on the indices and updates. Out-of-bounds accesses on `a` are undefined and typically result in unintended or invalid memory writes.

```cpp
inline array scatter(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})
```

```cpp
array scatter_add(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s = {})
```

Scatter and add updates to given indices.

```cpp
inline array scatter_add(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})
```

```cpp
array scatter_prod(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s = {})
```

Scatter and prod updates to given indices.

```cpp
inline array scatter_prod(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})
```

```cpp
array scatter_max(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s = {})
```

Scatter and max updates to given linear indices.

```cpp
inline array scatter_max(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})
```

```cpp
array scatter_min(const array &a, const std::vector<array> &indices, const array &updates, const std::vector<int> &axes, StreamOrDevice s = {})
```

Scatter and min updates to given linear indices.

```cpp
inline array scatter_min(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})
```

```cpp
array masked_scatter(const array &a, const array &mask, const array &src, StreamOrDevice s = {})
```

```cpp
array sqrt(const array &a, StreamOrDevice s = {})
```

Square root the elements of an array.

```cpp
array rsqrt(const array &a, StreamOrDevice s = {})
```

Square root and reciprocal the elements of an array.

```cpp
array softmax(const array &a, const std::vector<int> &axes, bool precise = false, StreamOrDevice s = {})
```

Softmax of an array.

```cpp
array softmax(const array &a, bool precise = false, StreamOrDevice s = {})
```

Softmax of an array.

```cpp
inline array softmax(const array &a, int axis, bool precise = false, StreamOrDevice s = {})
```

Softmax of an array.

```cpp
array power(const array &a, const array &b, StreamOrDevice s = {})
```

Raise elements of a to the power of b element-wise.

```cpp
array cumsum(const array &a, bool reverse = false, bool inclusive = true, std::optional<Dtype> dtype = std::nullopt, StreamOrDevice s = {})
```

Cumulative sum of an array.

```cpp
inline array cumsum(const array &a, bool reverse, bool inclusive, StreamOrDevice s)
```

```cpp
array cumsum(const array &a, int axis, bool reverse = false, bool inclusive = true, std::optional<Dtype> dtype = std::nullopt, StreamOrDevice s = {})
```

Cumulative sum of an array along the given axis.

```cpp
inline array cumsum(const array &a, int axis, bool reverse, bool inclusive, StreamOrDevice s)
```

```cpp
array cumprod(const array &a, bool reverse = false, bool inclusive = true, std::optional<Dtype> dtype = std::nullopt, StreamOrDevice s = {})
```

Cumulative product of an array.

```cpp
inline array cumprod(const array &a, bool reverse, bool inclusive, StreamOrDevice s)
```

```cpp
array cumprod(const array &a, int axis, bool reverse = false, bool inclusive = true, std::optional<Dtype> dtype = std::nullopt, StreamOrDevice s = {})
```

Cumulative product of an array along the given axis.

```cpp
inline array cumprod(const array &a, int axis, bool reverse, bool inclusive, StreamOrDevice s)
```

```cpp
array cummax(const array &a, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})
```

Cumulative max of an array.

```cpp
array cummax(const array &a, int axis, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})
```

Cumulative max of an array along the given axis.

```cpp
array cummin(const array &a, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})
```

Cumulative min of an array.

```cpp
array cummin(const array &a, int axis, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})
```

Cumulative min of an array along the given axis.

```cpp
array diff(const array &a, int n = 1, int axis = -1, StreamOrDevice s = {})
```

The n-th discrete difference along the given axis.

```cpp
array conv_general(array input, array weight, std::vector<int> stride = {}, std::vector<int> padding_lo = {}, std::vector<int> padding_hi = {}, std::vector<int> kernel_dilation = {}, std::vector<int> input_dilation = {}, int groups = 1, bool flip = false, StreamOrDevice s = {})
```

General convolution with a filter.

```cpp
inline array conv_general(const array &input, const array &weight, std::vector<int> stride = {}, std::vector<int> padding = {}, std::vector<int> kernel_dilation = {}, std::vector<int> input_dilation = {}, int groups = 1, bool flip = false, StreamOrDevice s = {})
```

General convolution with a filter.

```cpp
array conv1d(const array &input, const array &weight, int stride = 1, int padding = 0, int dilation = 1, int groups = 1, StreamOrDevice s = {})
```

1D convolution with a filter

```cpp
array conv2d(const array &input, const array &weight, const std::pair<int, int> &stride = {1, 1}, const std::pair<int, int> &padding = {0, 0}, const std::pair<int, int> &dilation = {1, 1}, int groups = 1, StreamOrDevice s = {})
```

2D convolution with a filter

```cpp
array conv3d(const array &input, const array &weight, const std::tuple<int, int, int> &stride = {1, 1, 1}, const std::tuple<int, int, int> &padding = {0, 0, 0}, const std::tuple<int, int, int> &dilation = {1, 1, 1}, int groups = 1, StreamOrDevice s = {})
```

3D convolution with a filter

```cpp
array conv_transpose1d(const array &input, const array &weight, int stride = 1, int padding = 0, int dilation = 1, int output_padding = 0, int groups = 1, StreamOrDevice s = {})
```

1D transposed convolution with a filter

```cpp
array conv_transpose2d(const array &input, const array &weight, const std::pair<int, int> &stride = {1, 1}, const std::pair<int, int> &padding = {0, 0}, const std::pair<int, int> &dilation = {1, 1}, const std::pair<int, int> &output_padding = {0, 0}, int groups = 1, StreamOrDevice s = {})
```

2D transposed convolution with a filter

```cpp
array conv_transpose3d(const array &input, const array &weight, const std::tuple<int, int, int> &stride = {1, 1, 1}, const std::tuple<int, int, int> &padding = {0, 0, 0}, const std::tuple<int, int, int> &dilation = {1, 1, 1}, const std::tuple<int, int, int> &output_padding = {0, 0, 0}, int groups = 1, StreamOrDevice s = {})
```

3D transposed convolution with a filter

```cpp
array quantized_matmul(const array &x, const array &w, const array &scales, const std::optional<array> &biases = std::nullopt, bool transpose = true, std::optional<int> group_size = std::nullopt, std::optional<int> bits = std::nullopt, const std::string &mode = "affine", StreamOrDevice s = {})
```

Quantized matmul multiplies x with a quantized matrix w.

```cpp
std::vector<array> quantize(const array &w, std::optional<int> group_size = std::nullopt, std::optional<int> bits = std::nullopt, const std::string &mode = "affine", const std::optional<array> &global_scale = std::nullopt, StreamOrDevice s = {})
```

Quantize a matrix along its last axis.

```cpp
array dequantize(const array &w, const array &scales, const std::optional<array> &biases = std::nullopt, std::optional<int> group_size = std::nullopt, std::optional<int> bits = std::nullopt, const std::string &mode = "affine", const std::optional<array> &global_scale = std::nullopt, std::optional<Dtype> dtype = std::nullopt, StreamOrDevice s = {})
```

Dequantize a matrix produced by [quantize()](#group__ops_1gaf70cd9a027e81e11e7f4fc91271e580c)

```cpp
array qqmm(const array &x, const array &w, const std::optional<array> &w_scales = std::nullopt, std::optional<int> group_size = std::nullopt, std::optional<int> bits = std::nullopt, const std::string &mode = "nvfp4", const std::optional<array> &global_scale_x = std::nullopt, const std::optional<array> &global_scale_w = std::nullopt, StreamOrDevice s = {})
```

```cpp
array from_fp8(array x, Dtype dtype, StreamOrDevice s = {})
```

Convert an E4M3 float8 to the given floating point dtype.

```cpp
array to_fp8(array x, StreamOrDevice s = {})
```

Convert a floating point matrix to E4M3 float8.

```cpp
array gather_qmm(const array &x, const array &w, const array &scales, const std::optional<array> &biases = std::nullopt, std::optional<array> lhs_indices = std::nullopt, std::optional<array> rhs_indices = std::nullopt, bool transpose = true, std::optional<int> group_size = std::nullopt, std::optional<int> bits = std::nullopt, const std::string &mode = "affine", const std::optional<array> &global_scale = std::nullopt, bool sorted_indices = false, StreamOrDevice s = {})
```

Compute matrix products with matrix-level gather.

```cpp
array gather_qqmm(const array &x, const array &w, const std::optional<array> &scales_w = std::nullopt, const std::optional<array> &lhs_indices = std::nullopt, const std::optional<array> &rhs_indices = std::nullopt, std::optional<int> group_size = std::nullopt, std::optional<int> bits = std::nullopt, const std::string &mode = "nvfp4", const std::optional<array> &global_scale_x = std::nullopt, const std::optional<array> &global_scale_w = std::nullopt, bool sorted_indices = false, StreamOrDevice s = {})
```

```cpp
array tensordot(const array &a, const array &b, const int axis = 2, StreamOrDevice s = {})
```

Returns a contraction of a and b over multiple dimensions.

```cpp
array tensordot(const array &a, const array &b, const std::vector<int> &axes_a, const std::vector<int> &axes_b, StreamOrDevice s = {})
```

```cpp
array outer(const array &a, const array &b, StreamOrDevice s = {})
```

Compute the outer product of two vectors.

```cpp
array inner(const array &a, const array &b, StreamOrDevice s = {})
```

Compute the inner product of two vectors.

```cpp
array vecdot(const array &a, const array &b, int axis = -1, StreamOrDevice s = {})
```

Compute a vector dot product along an axis.

```cpp
array addmm(array c, array a, array b, const float &alpha = 1.f, const float &beta = 1.f, StreamOrDevice s = {})
```

Compute D = beta * C + alpha * (A @ B)

```cpp
array block_masked_mm(array a, array b, int block_size, std::optional<array> mask_out = std::nullopt, std::optional<array> mask_lhs = std::nullopt, std::optional<array> mask_rhs = std::nullopt, StreamOrDevice s = {})
```

Compute matrix product with block masking.

```cpp
array gather_mm(array a, array b, std::optional<array> lhs_indices = std::nullopt, std::optional<array> rhs_indices = std::nullopt, bool sorted_indices = false, StreamOrDevice s = {})
```

Compute matrix product with matrix-level gather.

```cpp
array segmented_mm(array a, array b, array segments, StreamOrDevice s = {})
```

Compute a matrix product but segment the inner dimension and write the result separately for each segment.

```cpp
array diagonal(const array &a, int offset = 0, int axis1 = 0, int axis2 = 1, StreamOrDevice s = {})
```

Extract a diagonal or construct a diagonal array.

```cpp
array diag(const array &a, int k = 0, StreamOrDevice s = {})
```

Extract diagonal from a 2d array or create a diagonal matrix.

```cpp
array trace(const array &a, int offset, int axis1, int axis2, Dtype dtype, StreamOrDevice s = {})
```

Return the sum along a specified diagonal in the given array.

```cpp
array trace(const array &a, int offset, int axis1, int axis2, StreamOrDevice s = {})
```

```cpp
array trace(const array &a, StreamOrDevice s = {})
```

```cpp
std::vector<array> depends(const std::vector<array> &inputs, const std::vector<array> &dependencies)
```

Implements the identity function but allows injecting dependencies to other arrays.

This ensures that these other arrays will have been computed when the outputs of this function are computed.

```cpp
array atleast_1d(const array &a, StreamOrDevice s = {})
```

convert an array to an atleast ndim array

```cpp
std::vector<array> atleast_1d(const std::vector<array> &a, StreamOrDevice s = {})
```

```cpp
array atleast_2d(const array &a, StreamOrDevice s = {})
```

```cpp
std::vector<array> atleast_2d(const std::vector<array> &a, StreamOrDevice s = {})
```

```cpp
array atleast_3d(const array &a, StreamOrDevice s = {})
```

```cpp
std::vector<array> atleast_3d(const std::vector<array> &a, StreamOrDevice s = {})
```

```cpp
array number_of_elements(const array &a, std::vector<int> axes, bool inverted, Dtype dtype = int32, StreamOrDevice s = {})
```

Extract the number of elements along some axes as a scalar array.

Used to allow shape dependent shapeless compilation (pun intended).

```cpp
array conjugate(const array &a, StreamOrDevice s = {})
```

```cpp
array bitwise_and(const array &a, const array &b, StreamOrDevice s = {})
```

Bitwise and.

```cpp
array operator&(const array &a, const array &b)
```

```cpp
array bitwise_or(const array &a, const array &b, StreamOrDevice s = {})
```

Bitwise inclusive or.

```cpp
array operator|(const array &a, const array &b)
```

```cpp
array bitwise_xor(const array &a, const array &b, StreamOrDevice s = {})
```

Bitwise exclusive or.

```cpp
array operator^(const array &a, const array &b)
```

```cpp
array left_shift(const array &a, const array &b, StreamOrDevice s = {})
```

Shift bits to the left.

```cpp
array operator<<(const array &a, const array &b)
```

```cpp
array right_shift(const array &a, const array &b, StreamOrDevice s = {})
```

Shift bits to the right.

```cpp
array operator>>(const array &a, const array &b)
```

```cpp
array bitwise_invert(const array &a, StreamOrDevice s = {})
```

Invert the bits.

```cpp
array operator~(const array &a)
```

```cpp
array view(const array &a, const Dtype &dtype, StreamOrDevice s = {})
```

```cpp
array roll(const array &a, int shift, StreamOrDevice s = {})
```

Roll elements along an axis and introduce them on the other side.

```cpp
array roll(const array &a, const Shape &shift, StreamOrDevice s = {})
```

```cpp
array roll(const array &a, int shift, int axis, StreamOrDevice s = {})
```

```cpp
array roll(const array &a, int shift, const std::vector<int> &axes, StreamOrDevice s = {})
```

```cpp
array roll(const array &a, const Shape &shift, int axis, StreamOrDevice s = {})
```

```cpp
array roll(const array &a, const Shape &shift, const std::vector<int> &axes, StreamOrDevice s = {})
```

```cpp
array real(const array &a, StreamOrDevice s = {})
```

```cpp
array imag(const array &a, StreamOrDevice s = {})
```

```cpp
array contiguous(const array &a, bool allow_col_major = false, StreamOrDevice s = {})
```
