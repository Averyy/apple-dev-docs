---
source: MLX
framework: MLX
url: https://ml-explore.github.io/mlx/build/html/cpp/ops.html
---

# Operations

**

- [.rst](../_sources/cpp/ops.rst)
- **

.pdf

**

**
**
**

**

# Operations

 Table of contents 

## Contents

# Operations

**array arange(double start, double stop, double step, Dtype dtype, StreamOrDevice s = {})**
: A 1D array of numbers starting at `start` (optional), stopping at stop, stepping by `step` (optional).

**array arange(double start, double stop, double step, StreamOrDevice s = {})**
: 

**array arange(double start, double stop, Dtype dtype, StreamOrDevice s = {})**
: 

**array arange(double start, double stop, StreamOrDevice s = {})**
: 

**array arange(double stop, Dtype dtype, StreamOrDevice s = {})**
: 

**array arange(double stop, StreamOrDevice s = {})**
: 

**array arange(int start, int stop, int step, StreamOrDevice s = {})**
: 

**array arange(int start, int stop, StreamOrDevice s = {})**
: 

**array arange(int stop, StreamOrDevice s = {})**
: 

**array linspace(double start, double stop, int num = 50, Dtype dtype = float32, StreamOrDevice s = {})**
: A 1D array of `num` evenly spaced numbers in the range `[start, stop]`

**array astype(array a, Dtype dtype, StreamOrDevice s = {})**
: Convert an array to the given data type.

**array as_strided(array a, Shape shape, Strides strides, size_t offset, StreamOrDevice s = {})**
: Create a view of an array with the given shape and strides.

**array copy(array a, StreamOrDevice s = {})**
: Copy another array.

**array full(Shape shape, array vals, Dtype dtype, StreamOrDevice s = {})**
: Fill an array of the given shape with the given value(s).

**array full(Shape shape, array vals, StreamOrDevice s = {})**
: 

**template<typename T>
array full(Shape shape, [T](#_CPPv4I0E4full5array5Shape1T5Dtype14StreamOrDevice) val, Dtype dtype, StreamOrDevice s = {})**
: 

**template<typename T>
array full(Shape shape, [T](#_CPPv4I0E4full5array5Shape1T14StreamOrDevice) val, StreamOrDevice s = {})**
: 

**array full_like(const array &a, array vals, Dtype dtype, StreamOrDevice s = {})**
: 

**array full_like(const array &a, array vals, StreamOrDevice s = {})**
: 

**template<typename T>
array full_like(const array &a, [T](#_CPPv4I0E9full_like5arrayRK5array1T5Dtype14StreamOrDevice) val, Dtype dtype, StreamOrDevice s = {})**
: 

**template<typename T>
array full_like(const array &a, [T](#_CPPv4I0E9full_like5arrayRK5array1T14StreamOrDevice) val, StreamOrDevice s = {})**
: 

**array zeros(const Shape &shape, Dtype dtype, StreamOrDevice s = {})**
: Fill an array of the given shape with zeros.

**inline array zeros(const Shape &shape, StreamOrDevice s = {})**
: 

**array zeros_like(const array &a, StreamOrDevice s = {})**
: 

**array ones(const Shape &shape, Dtype dtype, StreamOrDevice s = {})**
: Fill an array of the given shape with ones.

**inline array ones(const Shape &shape, StreamOrDevice s = {})**
: 

**array ones_like(const array &a, StreamOrDevice s = {})**
: 

**array eye(int n, int m, int k, Dtype dtype, StreamOrDevice s = {})**
: Fill an array of the given shape (n,m) with ones in the specified diagonal k, and zeros everywhere else.

**inline array eye(int n, Dtype dtype, StreamOrDevice s = {})**
: 

**inline array eye(int n, int m, StreamOrDevice s = {})**
: 

**inline array eye(int n, int m, int k, StreamOrDevice s = {})**
: 

**inline array eye(int n, StreamOrDevice s = {})**
: 

**array identity(int n, Dtype dtype, StreamOrDevice s = {})**
: Create a square matrix of shape (n,n) of zeros, and ones in the major diagonal.

**inline array identity(int n, StreamOrDevice s = {})**
: 

**array tri(int n, int m, int k, Dtype type, StreamOrDevice s = {})**
: 

**inline array tri(int n, Dtype type, StreamOrDevice s = {})**
: 

**array tril(array x, int k = 0, StreamOrDevice s = {})**
: 

**array triu(array x, int k = 0, StreamOrDevice s = {})**
: 

**array reshape(const array &a, Shape shape, StreamOrDevice s = {})**
: Reshape an array to the given shape.

**array unflatten(const array &a, int axis, Shape shape, StreamOrDevice s = {})**
: Unflatten the axis to the given shape.

**array flatten(const array &a, int start_axis, int end_axis = -1, StreamOrDevice s = {})**
: Flatten the dimensions in the range `[start_axis, end_axis]` .

**array flatten(const array &a, StreamOrDevice s = {})**
: Flatten the array to 1D.

**array hadamard_transform(const array &a, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<float> scale = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, StreamOrDevice s = {})**
: Multiply the array by the Hadamard matrix of corresponding size.

**array squeeze(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: Remove singleton dimensions at the given axes.

**array squeeze(const array &a, int axis, StreamOrDevice s = {})**
: Remove singleton dimensions at the given axis.

**array squeeze(const array &a, StreamOrDevice s = {})**
: Remove all singleton dimensions.

**array expand_dims(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: Add a singleton dimension at the given axes.

**array expand_dims(const array &a, int axis, StreamOrDevice s = {})**
: Add a singleton dimension at the given axis.

**array slice(const array &a, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})**
: Slice an array.

**inline array slice(const array &a, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::initializer_list<int> start, Shape stop, Shape strides, StreamOrDevice s = {})**
: 

**array slice(const array &a, Shape start, Shape stop, StreamOrDevice s = {})**
: Slice an array with a stride of 1 in each dimension.

**array slice(const array &a, const array &start, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> axes, Shape slice_size, StreamOrDevice s = {})**
: Slice an array with dynamic starting indices.

**array slice_update(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})**
: Update a slice from the source array.

**array slice_update(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})**
: Update a slice from the source array with stride 1 in each dimension.

**array slice_update(const array &src, const array &update, const array &start, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> axes, StreamOrDevice s = {})**
: Update a slice from the source array with dynamic starting indices.

**array slice_update_add(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})**
: Slice update and add updates to given slice.

**array slice_update_add(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})**
: Slice update and add updates to given slice with stride 1 in each dimension.

**array slice_update_prod(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})**
: Slice update and prod updates to given slice.

**array slice_update_prod(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})**
: Slice update and prod updates to given slice with stride 1 in each dimension.

**array slice_update_max(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})**
: Slice update and max updates to given slice.

**array slice_update_max(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})**
: Slice update and max updates to given slice with stride 1 in each dimension.

**array slice_update_min(const array &src, const array &update, Shape start, Shape stop, Shape strides, StreamOrDevice s = {})**
: Slice update and min updates to given slice.

**array slice_update_min(const array &src, const array &update, Shape start, Shape stop, StreamOrDevice s = {})**
: Slice update and min updates to given slice with stride 1 in each dimension.

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> split(const array &a, int num_splits, int axis, StreamOrDevice s = {})**
: Split an array into sub-arrays along a given axis.

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> split(const array &a, int num_splits, StreamOrDevice s = {})**
: 

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> split(const array &a, const Shape &indices, int axis, StreamOrDevice s = {})**
: 

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> split(const array &a, const Shape &indices, StreamOrDevice s = {})**
: 

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> meshgrid(const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &arrays, bool sparse = false, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &indexing = "xy", StreamOrDevice s = {})**
: A vector of coordinate arrays from coordinate vectors.

**array clip(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> &a_min = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> &a_max = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, StreamOrDevice s = {})**
: Clip (limit) the values in an array.

**array concatenate([std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> arrays, int axis, StreamOrDevice s = {})**
: Concatenate arrays along a given axis.

**array concatenate([std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> arrays, StreamOrDevice s = {})**
: 

**array stack(const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &arrays, int axis, StreamOrDevice s = {})**
: Stack arrays along a new axis.

**array stack(const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &arrays, StreamOrDevice s = {})**
: 

**array repeat(const array &arr, int repeats, int axis, StreamOrDevice s = {})**
: Repeat an array along an axis.

**array repeat(const array &arr, int repeats, StreamOrDevice s = {})**
: 

**array tile(const array &arr, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> reps, StreamOrDevice s = {})**
: 

**array transpose(const array &a, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> axes, StreamOrDevice s = {})**
: Permutes the dimensions according to the given axes.

**inline array transpose(const array &a, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::initializer_list<int> axes, StreamOrDevice s = {})**
: 

**array swapaxes(const array &a, int axis1, int axis2, StreamOrDevice s = {})**
: Swap two axes of an array.

**array moveaxis(const array &a, int source, int destination, StreamOrDevice s = {})**
: Move an axis of an array.

**array pad(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, const Shape &low_pad_size, const Shape &high_pad_size, const array &pad_value = array(0), const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "constant", StreamOrDevice s = {})**
: Pad an array with a constant value.

**array pad(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<[std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int>> &pad_width, const array &pad_value = array(0), const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "constant", StreamOrDevice s = {})**
: Pad an array with a constant value along all axes.

**array pad(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int> &pad_width, const array &pad_value = array(0), const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "constant", StreamOrDevice s = {})**
: 

**array pad(const array &a, int pad_width, const array &pad_value = array(0), const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "constant", StreamOrDevice s = {})**
: 

**array transpose(const array &a, StreamOrDevice s = {})**
: Permutes the dimensions in reverse order.

**array broadcast_to(const array &a, const Shape &shape, StreamOrDevice s = {})**
: Broadcast an array to a given shape.

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> broadcast_arrays(const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &inputs, StreamOrDevice s = {})**
: Broadcast a vector of arrays against one another.

**array equal(const array &a, const array &b, StreamOrDevice s = {})**
: Returns the bool array with (a == b) element-wise.

**inline array operator==(const array &a, const array &b)**
: 

**template<typename T>
array operator==([T](#_CPPv4I0Eeq5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator==(const array &a, [T](#_CPPv4I0Eeq5arrayRK5array1T) b)**
: 

**array not_equal(const array &a, const array &b, StreamOrDevice s = {})**
: Returns the bool array with (a != b) element-wise.

**inline array operator!=(const array &a, const array &b)**
: 

**template<typename T>
array operator!=([T](#_CPPv4I0Ene5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator!=(const array &a, [T](#_CPPv4I0Ene5arrayRK5array1T) b)**
: 

**array greater(const array &a, const array &b, StreamOrDevice s = {})**
: Returns bool array with (a > b) element-wise.

**inline array operator>(const array &a, const array &b)**
: 

**template<typename T>
array operator>([T](#_CPPv4I0Egt5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator>(const array &a, [T](#_CPPv4I0Egt5arrayRK5array1T) b)**
: 

**array greater_equal(const array &a, const array &b, StreamOrDevice s = {})**
: Returns bool array with (a >= b) element-wise.

**inline array operator>=(const array &a, const array &b)**
: 

**template<typename T>
array operator>=([T](#_CPPv4I0Ege5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator>=(const array &a, [T](#_CPPv4I0Ege5arrayRK5array1T) b)**
: 

**array less(const array &a, const array &b, StreamOrDevice s = {})**
: Returns bool array with (a < b) element-wise.

**inline array operator<(const array &a, const array &b)**
: 

**template<typename T>
array operator<([T](#_CPPv4I0Elt5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator<(const array &a, [T](#_CPPv4I0Elt5arrayRK5array1T) b)**
: 

**array less_equal(const array &a, const array &b, StreamOrDevice s = {})**
: Returns bool array with (a <= b) element-wise.

**inline array operator<=(const array &a, const array &b)**
: 

**template<typename T>
array operator<=([T](#_CPPv4I0Ele5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator<=(const array &a, [T](#_CPPv4I0Ele5arrayRK5array1T) b)**
: 

**array array_equal(const array &a, const array &b, bool equal_nan, StreamOrDevice s = {})**
: True if two arrays have the same shape and elements.

**inline array array_equal(const array &a, const array &b, StreamOrDevice s = {})**
: 

**array isnan(const array &a, StreamOrDevice s = {})**
: 

**array isinf(const array &a, StreamOrDevice s = {})**
: 

**array isfinite(const array &a, StreamOrDevice s = {})**
: 

**array isposinf(const array &a, StreamOrDevice s = {})**
: 

**array isneginf(const array &a, StreamOrDevice s = {})**
: 

**array where(const array &condition, const array &x, const array &y, StreamOrDevice s = {})**
: Select from x or y depending on condition.

**array nan_to_num(const array &a, float nan = 0.0f, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<float> posinf = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<float> neginf = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, StreamOrDevice s = {})**
: Replace NaN and infinities with finite numbers.

**array all(const array &a, bool keepdims, StreamOrDevice s = {})**
: True if all elements in the array are true (or non-zero).

**inline array all(const array &a, StreamOrDevice s = {})**
: 

**array allclose(const array &a, const array &b, double rtol = 1e-5, double atol = 1e-8, bool equal_nan = false, StreamOrDevice s = {})**
: True if the two arrays are equal within the specified tolerance.

**array isclose(const array &a, const array &b, double rtol = 1e-5, double atol = 1e-8, bool equal_nan = false, StreamOrDevice s = {})**
: Returns a boolean array where two arrays are element-wise equal within the specified tolerance.

**array all(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: Reduces the input along the given axes. 
An output value is true if all the corresponding inputs are true.

**array all(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: Reduces the input along the given axis. 
An output value is true if all the corresponding inputs are true.

**array any(const array &a, bool keepdims, StreamOrDevice s = {})**
: True if any elements in the array are true (or non-zero).

**inline array any(const array &a, StreamOrDevice s = {})**
: 

**array any(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: Reduces the input along the given axes. 
An output value is true if any of the corresponding inputs are true.

**array any(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: Reduces the input along the given axis. 
An output value is true if any of the corresponding inputs are true.

**array sum(const array &a, bool keepdims, StreamOrDevice s = {})**
: Sums the elements of an array.

**inline array sum(const array &a, StreamOrDevice s = {})**
: 

**array sum(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: Sums the elements of an array along the given axes.

**array sum(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: Sums the elements of an array along the given axis.

**array mean(const array &a, bool keepdims, StreamOrDevice s = {})**
: Computes the mean of the elements of an array.

**inline array mean(const array &a, StreamOrDevice s = {})**
: 

**array mean(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: Computes the mean of the elements of an array along the given axes.

**array mean(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: Computes the mean of the elements of an array along the given axis.

**array median(const array &a, bool keepdims, StreamOrDevice s = {})**
: Computes the median of the elements of an array.

**inline array median(const array &a, StreamOrDevice s = {})**
: 

**array median(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: Computes the median of the elements of an array along the given axes.

**array median(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: Computes the median of the elements of an array along the given axis.

**array var(const array &a, bool keepdims, int ddof = 0, StreamOrDevice s = {})**
: Computes the variance of the elements of an array.

**inline array var(const array &a, StreamOrDevice s = {})**
: 

**array var(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, int ddof = 0, StreamOrDevice s = {})**
: Computes the variance of the elements of an array along the given axes.

**array var(const array &a, int axis, bool keepdims = false, int ddof = 0, StreamOrDevice s = {})**
: Computes the variance of the elements of an array along the given axis.

**array std(const array &a, bool keepdims, int ddof = 0, StreamOrDevice s = {})**
: Computes the standard deviation of the elements of an array.

**inline array std(const array &a, StreamOrDevice s = {})**
: 

**array std(const array &a, const [std](#_CPPv4StRK5arrayRKNSt6vectorIiEEbi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, int ddof = 0, StreamOrDevice s = {})**
: Computes the standard deviation of the elements of an array along the given axes.

**array std(const array &a, int axis, bool keepdims = false, int ddof = 0, StreamOrDevice s = {})**
: Computes the standard deviation of the elements of an array along the given axis.

**array prod(const array &a, bool keepdims, StreamOrDevice s = {})**
: The product of all elements of the array.

**inline array prod(const array &a, StreamOrDevice s = {})**
: 

**array prod(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: The product of the elements of an array along the given axes.

**array prod(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: The product of the elements of an array along the given axis.

**array max(const array &a, bool keepdims, StreamOrDevice s = {})**
: The maximum of all elements of the array.

**inline array max(const array &a, StreamOrDevice s = {})**
: 

**array max(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: The maximum of the elements of an array along the given axes.

**array max(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: The maximum of the elements of an array along the given axis.

**array min(const array &a, bool keepdims, StreamOrDevice s = {})**
: The minimum of all elements of the array.

**inline array min(const array &a, StreamOrDevice s = {})**
: 

**array min(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: The minimum of the elements of an array along the given axes.

**array min(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: The minimum of the elements of an array along the given axis.

**array hanning(int M, StreamOrDevice s = {})**
: Returns the Hanning window of size M.

**array hamming(int M, StreamOrDevice s = {})**
: Returns the Hamming window of size M.

**array bartlett(int M, StreamOrDevice s = {})**
: Returns the bartlett window of size M.

**array blackman(int M, StreamOrDevice s = {})**
: Returns the Blackmann window of size M.

**array argmin(const array &a, bool keepdims, StreamOrDevice s = {})**
: Returns the index of the minimum value in the array.

**inline array argmin(const array &a, StreamOrDevice s = {})**
: 

**array argmin(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: Returns the indices of the minimum values along a given axis.

**array argmax(const array &a, bool keepdims, StreamOrDevice s = {})**
: Returns the index of the maximum value in the array.

**inline array argmax(const array &a, StreamOrDevice s = {})**
: 

**array argmax(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: Returns the indices of the maximum values along a given axis.

**array sort(const array &a, StreamOrDevice s = {})**
: Returns a sorted copy of the flattened array. 
The sort is stable and NaN values are placed at the end.

**array sort(const array &a, int axis, StreamOrDevice s = {})**
: Returns a sorted copy of the array along a given axis. 
The sort is stable and NaN values are placed at the end.

**array argsort(const array &a, StreamOrDevice s = {})**
: Returns indices that sort the flattened array. 
The sort is stable and NaN values are placed at the end.

**array argsort(const array &a, int axis, StreamOrDevice s = {})**
: Returns indices that sort the array along a given axis. 
The sort is stable and NaN values are placed at the end.

**array partition(const array &a, int kth, StreamOrDevice s = {})**
: Returns a partitioned copy of the flattened array such that the smaller kth elements are first.

**array partition(const array &a, int kth, int axis, StreamOrDevice s = {})**
: Returns a partitioned copy of the array along a given axis such that the smaller kth elements are first.

**array argpartition(const array &a, int kth, StreamOrDevice s = {})**
: Returns indices that partition the flattened array such that the smaller kth elements are first.

**array argpartition(const array &a, int kth, int axis, StreamOrDevice s = {})**
: Returns indices that partition the array along a given axis such that the smaller kth elements are first.

**array topk(const array &a, int k, StreamOrDevice s = {})**
: Returns topk elements of the flattened array.

**array topk(const array &a, int k, int axis, StreamOrDevice s = {})**
: Returns topk elements of the array along a given axis.

**array logcumsumexp(const array &a, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative logsumexp of an array.

**array logcumsumexp(const array &a, int axis, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative logsumexp of an array along the given axis.

**array logsumexp(const array &a, bool keepdims, StreamOrDevice s = {})**
: The logsumexp of all elements of the array.

**inline array logsumexp(const array &a, StreamOrDevice s = {})**
: 

**array logsumexp(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool keepdims = false, StreamOrDevice s = {})**
: The logsumexp of the elements of an array along the given axes.

**array logsumexp(const array &a, int axis, bool keepdims = false, StreamOrDevice s = {})**
: The logsumexp of the elements of an array along the given axis.

**array abs(const array &a, StreamOrDevice s = {})**
: Absolute value of elements in an array.

**array negative(const array &a, StreamOrDevice s = {})**
: Negate an array.

**array operator-(const array &a)**
: 

**array sign(const array &a, StreamOrDevice s = {})**
: The sign of the elements in an array.

**array logical_not(const array &a, StreamOrDevice s = {})**
: Logical not of an array.

**array logical_and(const array &a, const array &b, StreamOrDevice s = {})**
: Logical and of two arrays.

**array operator&&(const array &a, const array &b)**
: 

**array logical_or(const array &a, const array &b, StreamOrDevice s = {})**
: Logical or of two arrays.

**array operator||(const array &a, const array &b)**
: 

**array reciprocal(const array &a, StreamOrDevice s = {})**
: The reciprocal (1/x) of the elements in an array.

**array add(const array &a, const array &b, StreamOrDevice s = {})**
: Add two arrays.

**array operator+(const array &a, const array &b)**
: 

**template<typename T>
array operator+([T](#_CPPv4I0Epl5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator+(const array &a, [T](#_CPPv4I0Epl5arrayRK5array1T) b)**
: 

**array subtract(const array &a, const array &b, StreamOrDevice s = {})**
: Subtract two arrays.

**array operator-(const array &a, const array &b)**
: 

**template<typename T>
array operator-([T](#_CPPv4I0Emi5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator-(const array &a, [T](#_CPPv4I0Emi5arrayRK5array1T) b)**
: 

**array multiply(const array &a, const array &b, StreamOrDevice s = {})**
: Multiply two arrays.

**array operator*(const array &a, const array &b)**
: 

**template<typename T>
array operator*([T](#_CPPv4I0Eml5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator*(const array &a, [T](#_CPPv4I0Eml5arrayRK5array1T) b)**
: 

**array divide(const array &a, const array &b, StreamOrDevice s = {})**
: Divide two arrays.

**array operator/(const array &a, const array &b)**
: 

**array operator/(double a, const array &b)**
: 

**array operator/(const array &a, double b)**
: 

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> divmod(const array &a, const array &b, StreamOrDevice s = {})**
: Compute the element-wise quotient and remainder.

**array floor_divide(const array &a, const array &b, StreamOrDevice s = {})**
: Compute integer division. 
Equivalent to doing floor(a / x).

**array remainder(const array &a, const array &b, StreamOrDevice s = {})**
: Compute the element-wise remainder of division.

**array operator%(const array &a, const array &b)**
: 

**template<typename T>
array operator%([T](#_CPPv4I0Erm5array1TRK5array) a, const array &b)**
: 

**template<typename T>
array operator%(const array &a, [T](#_CPPv4I0Erm5arrayRK5array1T) b)**
: 

**array maximum(const array &a, const array &b, StreamOrDevice s = {})**
: Element-wise maximum between two arrays.

**array minimum(const array &a, const array &b, StreamOrDevice s = {})**
: Element-wise minimum between two arrays.

**array floor(const array &a, StreamOrDevice s = {})**
: Floor the element of an array.

**array ceil(const array &a, StreamOrDevice s = {})**
: Ceil the element of an array.

**array square(const array &a, StreamOrDevice s = {})**
: Square the elements of an array.

**array exp(const array &a, StreamOrDevice s = {})**
: Exponential of the elements of an array.

**array sin(const array &a, StreamOrDevice s = {})**
: Sine of the elements of an array.

**array cos(const array &a, StreamOrDevice s = {})**
: Cosine of the elements of an array.

**array tan(const array &a, StreamOrDevice s = {})**
: Tangent of the elements of an array.

**array arcsin(const array &a, StreamOrDevice s = {})**
: Arc Sine of the elements of an array.

**array arccos(const array &a, StreamOrDevice s = {})**
: Arc Cosine of the elements of an array.

**array arctan(const array &a, StreamOrDevice s = {})**
: Arc Tangent of the elements of an array.

**array arctan2(const array &a, const array &b, StreamOrDevice s = {})**
: Inverse tangent of the ratio of two arrays.

**array sinh(const array &a, StreamOrDevice s = {})**
: Hyperbolic Sine of the elements of an array.

**array cosh(const array &a, StreamOrDevice s = {})**
: Hyperbolic Cosine of the elements of an array.

**array tanh(const array &a, StreamOrDevice s = {})**
: Hyperbolic Tangent of the elements of an array.

**array arcsinh(const array &a, StreamOrDevice s = {})**
: Inverse Hyperbolic Sine of the elements of an array.

**array arccosh(const array &a, StreamOrDevice s = {})**
: Inverse Hyperbolic Cosine of the elements of an array.

**array arctanh(const array &a, StreamOrDevice s = {})**
: Inverse Hyperbolic Tangent of the elements of an array.

**array degrees(const array &a, StreamOrDevice s = {})**
: Convert the elements of an array from Radians to Degrees.

**array radians(const array &a, StreamOrDevice s = {})**
: Convert the elements of an array from Degrees to Radians.

**array log(const array &a, StreamOrDevice s = {})**
: Natural logarithm of the elements of an array.

**array log2(const array &a, StreamOrDevice s = {})**
: Log base 2 of the elements of an array.

**array log10(const array &a, StreamOrDevice s = {})**
: Log base 10 of the elements of an array.

**array log1p(const array &a, StreamOrDevice s = {})**
: Natural logarithm of one plus elements in the array: `log(1 + a)`.

**array logaddexp(const array &a, const array &b, StreamOrDevice s = {})**
: Log-add-exp of one elements in the array: `log(exp(a) + exp(b))`.

**array sigmoid(const array &a, StreamOrDevice s = {})**
: Element-wise logistic sigmoid of the array: `1 / (1 + exp(-x)`.

**array erf(const array &a, StreamOrDevice s = {})**
: Computes the error function of the elements of an array.

**array erfinv(const array &a, StreamOrDevice s = {})**
: Computes the inverse error function of the elements of an array.

**array expm1(const array &a, StreamOrDevice s = {})**
: Computes the expm1 function of the elements of an array.

**array stop_gradient(const array &a, StreamOrDevice s = {})**
: Stop the flow of gradients.

**array round(const array &a, int decimals, StreamOrDevice s = {})**
: Round a floating point number.

**inline array round(const array &a, StreamOrDevice s = {})**
: 

**array matmul(const array &a, const array &b, StreamOrDevice s = {})**
: Matrix-matrix multiplication.

**array gather(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &indices, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, const Shape &slice_sizes, StreamOrDevice s = {})**
: Gather array entries given indices and slices.

**inline array gather(const array &a, const array &indices, int axis, const Shape &slice_sizes, StreamOrDevice s = {})**
: 

**array kron(const array &a, const array &b, StreamOrDevice s = {})**
: Compute the Kronecker product of two arrays.

**array take(const array &a, const array &indices, int axis, StreamOrDevice s = {})**
: Take array slices at the given indices of the specified axis.

**array take(const array &a, int index, int axis, StreamOrDevice s = {})**
: 

**array take(const array &a, const array &indices, StreamOrDevice s = {})**
: Take array entries at the given indices treating the array as flattened.

**array take(const array &a, int index, StreamOrDevice s = {})**
: 

**array take_along_axis(const array &a, const array &indices, int axis, StreamOrDevice s = {})**
: Take array entries given indices along the axis.

**array put_along_axis(const array &a, const array &indices, const array &values, int axis, StreamOrDevice s = {})**
: Put the values into the array at the given indices along the axis.

**array scatter_add_axis(const array &a, const array &indices, const array &values, int axis, StreamOrDevice s = {})**
: Add the values into the array at the given indices along the axis.

**array scatter(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &indices, const array &updates, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: Scatter updates to the given indices. 
The parameters `indices` and `axes` determine the locations of `a` that are updated with the values in `updates`. Assuming 1-d `indices` for simplicity, `indices[i]` are the indices on axis `axes[i]` to which the values in `updates` will be applied. Note each array in `indices` is assigned to a corresponding axis and hence `indices.size() == axes.size()`. If an index/axis pair is not provided then indices along that axis are assumed to be zero.
Note the rank of `updates` must be equal to the sum of the rank of the broadcasted `indices` and the rank of `a`. In other words, assuming the arrays in `indices` have the same shape, `updates.ndim() == indices[0].ndim() + a.ndim()`. The leading dimensions of `updates` correspond to the indices, and the remaining `a.ndim()` dimensions are the values that will be applied to the given location in `a`.
For example:
auto in = zeros({4, 4}, float32);
auto indices = array({2});
auto updates = reshape(arange(1, 3, float32), {1, 1, 2});
std::vector<int> axes{0};

auto out = scatter(in, {indices}, updates, axes);

will produce:
array([[0, 0, 0, 0],
       [0, 0, 0, 0],
       [1, 2, 0, 0],
       [0, 0, 0, 0]], dtype=float32)

This scatters the two-element row vector `[1, 2]` starting at the `(2, 0)` position of `a`.
Adding another element to `indices` will scatter into another location of `a`. We also have to add an another update for the new index:
auto in = zeros({4, 4}, float32);
auto indices = array({2, 0});
auto updates = reshape(arange(1, 5, float32), {2, 1, 2});
std::vector<int> axes{0};

auto out = scatter(in, {indices}, updates, axes):

will produce:
array([[3, 4, 0, 0],
       [0, 0, 0, 0],
       [1, 2, 0, 0],
       [0, 0, 0, 0]], dtype=float32)

To control the scatter location on an additional axis, add another index array to `indices` and another axis to `axes`:
auto in = zeros({4, 4}, float32);
auto indices = std::vector{array({2, 0}), array({1, 2})};
auto updates = reshape(arange(1, 5, float32), {2, 1, 2});
std::vector<int> axes{0, 1};

auto out = scatter(in, indices, updates, axes);

will produce:
array([[0, 0, 3, 4],
      [0, 0, 0, 0],
      [0, 1, 2, 0],
      [0, 0, 0, 0]], dtype=float32)

Items in indices are broadcasted together. This means:
auto indices = std::vector{array({2, 0}), array({1})};

is equivalent to:
auto indices = std::vector{array({2, 0}), array({1, 1})};

Note, `scatter` does not perform bounds checking on the indices and updates. Out-of-bounds accesses on `a` are undefined and typically result in unintended or invalid memory writes.

**inline array scatter(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})**
: 

**array scatter_add(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &indices, const array &updates, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: Scatter and add updates to given indices.

**inline array scatter_add(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})**
: 

**array scatter_prod(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &indices, const array &updates, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: Scatter and prod updates to given indices.

**inline array scatter_prod(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})**
: 

**array scatter_max(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &indices, const array &updates, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: Scatter and max updates to given linear indices.

**inline array scatter_max(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})**
: 

**array scatter_min(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &indices, const array &updates, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: Scatter and min updates to given linear indices.

**inline array scatter_min(const array &a, const array &indices, const array &updates, int axis, StreamOrDevice s = {})**
: 

**array masked_scatter(const array &a, const array &mask, const array &src, StreamOrDevice s = {})**
: 

**array sqrt(const array &a, StreamOrDevice s = {})**
: Square root the elements of an array.

**array rsqrt(const array &a, StreamOrDevice s = {})**
: Square root and reciprocal the elements of an array.

**array softmax(const array &a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, bool precise = false, StreamOrDevice s = {})**
: Softmax of an array.

**array softmax(const array &a, bool precise = false, StreamOrDevice s = {})**
: Softmax of an array.

**inline array softmax(const array &a, int axis, bool precise = false, StreamOrDevice s = {})**
: Softmax of an array.

**array power(const array &a, const array &b, StreamOrDevice s = {})**
: Raise elements of a to the power of b element-wise.

**array cumsum(const array &a, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative sum of an array.

**array cumsum(const array &a, int axis, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative sum of an array along the given axis.

**array cumprod(const array &a, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative product of an array.

**array cumprod(const array &a, int axis, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative product of an array along the given axis.

**array cummax(const array &a, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative max of an array.

**array cummax(const array &a, int axis, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative max of an array along the given axis.

**array cummin(const array &a, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative min of an array.

**array cummin(const array &a, int axis, bool reverse = false, bool inclusive = true, StreamOrDevice s = {})**
: Cumulative min of an array along the given axis.

**array conv_general(array input, array weight, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> stride = {}, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> padding_lo = {}, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> padding_hi = {}, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> kernel_dilation = {}, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> input_dilation = {}, int groups = 1, bool flip = false, StreamOrDevice s = {})**
: General convolution with a filter.

**inline array conv_general(const array &input, const array &weight, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> stride = {}, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> padding = {}, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> kernel_dilation = {}, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> input_dilation = {}, int groups = 1, bool flip = false, StreamOrDevice s = {})**
: General convolution with a filter.

**array conv1d(const array &input, const array &weight, int stride = 1, int padding = 0, int dilation = 1, int groups = 1, StreamOrDevice s = {})**
: 1D convolution with a filter

**array conv2d(const array &input, const array &weight, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int> &stride = {1, 1}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int> &padding = {0, 0}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int> &dilation = {1, 1}, int groups = 1, StreamOrDevice s = {})**
: 2D convolution with a filter

**array conv3d(const array &input, const array &weight, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::tuple<int, int, int> &stride = {1, 1, 1}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::tuple<int, int, int> &padding = {0, 0, 0}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::tuple<int, int, int> &dilation = {1, 1, 1}, int groups = 1, StreamOrDevice s = {})**
: 3D convolution with a filter

**array conv_transpose1d(const array &input, const array &weight, int stride = 1, int padding = 0, int dilation = 1, int output_padding = 0, int groups = 1, StreamOrDevice s = {})**
: 1D transposed convolution with a filter

**array conv_transpose2d(const array &input, const array &weight, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int> &stride = {1, 1}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int> &padding = {0, 0}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int> &dilation = {1, 1}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::pair<int, int> &output_padding = {0, 0}, int groups = 1, StreamOrDevice s = {})**
: 2D transposed convolution with a filter

**array conv_transpose3d(const array &input, const array &weight, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::tuple<int, int, int> &stride = {1, 1, 1}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::tuple<int, int, int> &padding = {0, 0, 0}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::tuple<int, int, int> &dilation = {1, 1, 1}, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::tuple<int, int, int> &output_padding = {0, 0, 0}, int groups = 1, StreamOrDevice s = {})**
: 3D transposed convolution with a filter

**array quantized_matmul(array x, array w, array scales, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> biases = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, bool transpose = true, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> group_size = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> bits = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "affine", StreamOrDevice s = {})**
: Quantized matmul multiplies x with a quantized matrix w.

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> quantize(const array &w, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> group_size = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> bits = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "affine", const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> &global_scale = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, StreamOrDevice s = {})**
: Quantize a matrix along its last axis.

**array dequantize(const array &w, const array &scales, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> &biases = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> group_size = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> bits = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "affine", const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> &global_scale = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<Dtype> dtype = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, StreamOrDevice s = {})**
: Dequantize a matrix produced by [quantize()](#group__ops_1gaf70cd9a027e81e11e7f4fc91271e580c)

**array qqmm(array x, array w, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> w_scales = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> group_size = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> bits = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "nvfp4", const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> global_scale_x = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> global_scale_w = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, StreamOrDevice s = {})**
: 

**array from_fp8(array x, Dtype dtype, StreamOrDevice s = {})**
: Convert an E4M3 float8 to the given floating point dtype.

**array to_fp8(array x, StreamOrDevice s = {})**
: Convert a floating point matrix to E4M3 float8.

**array gather_qmm(const array &x, const array &w, const array &scales, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> &biases = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> lhs_indices = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> rhs_indices = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, bool transpose = true, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> group_size = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<int> bits = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::string &mode = "affine", bool sorted_indices = false, StreamOrDevice s = {})**
: Compute matrix products with matrix-level gather.

**array tensordot(const array &a, const array &b, const int axis = 2, StreamOrDevice s = {})**
: Returns a contraction of a and b over multiple dimensions.

**array tensordot(const array &a, const array &b, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes_a, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes_b, StreamOrDevice s = {})**
: 

**array outer(const array &a, const array &b, StreamOrDevice s = {})**
: Compute the outer product of two vectors.

**array inner(const array &a, const array &b, StreamOrDevice s = {})**
: Compute the inner product of two vectors.

**array addmm(array c, array a, array b, const float &alpha = 1.f, const float &beta = 1.f, StreamOrDevice s = {})**
: Compute D = beta * C + alpha * (A @ B)

**array block_masked_mm(array a, array b, int block_size, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> mask_out = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> mask_lhs = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> mask_rhs = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, StreamOrDevice s = {})**
: Compute matrix product with block masking.

**array gather_mm(array a, array b, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> lhs_indices = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::optional<array> rhs_indices = [std](#_CPPv4StRK5arraybi14StreamOrDevice)::nullopt, bool sorted_indices = false, StreamOrDevice s = {})**
: Compute matrix product with matrix-level gather.

**array segmented_mm(array a, array b, array segments, StreamOrDevice s = {})**
: Compute a matrix product but segment the inner dimension and write the result separately for each segment.

**array diagonal(const array &a, int offset = 0, int axis1 = 0, int axis2 = 1, StreamOrDevice s = {})**
: Extract a diagonal or construct a diagonal array.

**array diag(const array &a, int k = 0, StreamOrDevice s = {})**
: Extract diagonal from a 2d array or create a diagonal matrix.

**array trace(const array &a, int offset, int axis1, int axis2, Dtype dtype, StreamOrDevice s = {})**
: Return the sum along a specified diagonal in the given array.

**array trace(const array &a, int offset, int axis1, int axis2, StreamOrDevice s = {})**
: 

**array trace(const array &a, StreamOrDevice s = {})**
: 

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> depends(const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &inputs, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &dependencies)**
: Implements the identity function but allows injecting dependencies to other arrays. 
This ensures that these other arrays will have been computed when the outputs of this function are computed.

**array atleast_1d(const array &a, StreamOrDevice s = {})**
: convert an array to an atleast ndim array

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> atleast_1d(const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &a, StreamOrDevice s = {})**
: 

**array atleast_2d(const array &a, StreamOrDevice s = {})**
: 

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> atleast_2d(const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &a, StreamOrDevice s = {})**
: 

**array atleast_3d(const array &a, StreamOrDevice s = {})**
: 

**[std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> atleast_3d(const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<array> &a, StreamOrDevice s = {})**
: 

**array number_of_elements(const array &a, [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> axes, bool inverted, Dtype dtype = int32, StreamOrDevice s = {})**
: Extract the number of elements along some axes as a scalar array. 
Used to allow shape dependent shapeless compilation (pun intended).

**array conjugate(const array &a, StreamOrDevice s = {})**
: 

**array bitwise_and(const array &a, const array &b, StreamOrDevice s = {})**
: Bitwise and.

**array operator&(const array &a, const array &b)**
: 

**array bitwise_or(const array &a, const array &b, StreamOrDevice s = {})**
: Bitwise inclusive or.

**array operator|(const array &a, const array &b)**
: 

**array bitwise_xor(const array &a, const array &b, StreamOrDevice s = {})**
: Bitwise exclusive or.

**array operator^(const array &a, const array &b)**
: 

**array left_shift(const array &a, const array &b, StreamOrDevice s = {})**
: Shift bits to the left.

**array operator<<(const array &a, const array &b)**
: 

**array right_shift(const array &a, const array &b, StreamOrDevice s = {})**
: Shift bits to the right.

**array operator>>(const array &a, const array &b)**
: 

**array bitwise_invert(const array &a, StreamOrDevice s = {})**
: Invert the bits.

**array operator~(const array &a)**
: 

**array view(const array &a, const Dtype &dtype, StreamOrDevice s = {})**
: 

**array roll(const array &a, int shift, StreamOrDevice s = {})**
: Roll elements along an axis and introduce them on the other side.

**array roll(const array &a, const Shape &shift, StreamOrDevice s = {})**
: 

**array roll(const array &a, int shift, int axis, StreamOrDevice s = {})**
: 

**array roll(const array &a, int shift, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: 

**array roll(const array &a, const Shape &shift, int axis, StreamOrDevice s = {})**
: 

**array roll(const array &a, const Shape &shift, const [std](#_CPPv4StRK5arraybi14StreamOrDevice)::vector<int> &axes, StreamOrDevice s = {})**
: 

**array real(const array &a, StreamOrDevice s = {})**
: 

**array imag(const array &a, StreamOrDevice s = {})**
: 

**array contiguous(const array &a, bool allow_col_major = false, StreamOrDevice s = {})**
: 

** Contents
