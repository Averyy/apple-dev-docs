---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/free-functions"
framework: "mlx-swift/MLX"
---

# Free Functions

**Framework**: mlx-swift/MLX  
**Role**: API Collection

Free functions in MLX.

#### Overview

MLX has a wide variety of free functions, categorized below.  [`MLXArray`](./mlxarray.md) has some identical operations as methods for convenience.

## Topics

### Element-wise Arithmetic Free Functions
- [func abs(MLXArray, stream: StreamOrDevice) -> MLXArray](./abs%28_,stream%29.md)
  Element-wise absolute value.
- [func acos(MLXArray, stream: StreamOrDevice) -> MLXArray](./acos%28_,stream%29.md)
  Element-wise inverse cosine.
- [func acosh(MLXArray, stream: StreamOrDevice) -> MLXArray](./acosh%28_,stream%29.md)
  Element-wise inverse hyperbolic cosine.
- [func add(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./add%28_,_,stream%29.md)
  Element-wise addition.
- [func asin(MLXArray, stream: StreamOrDevice) -> MLXArray](./asin%28_,stream%29.md)
  Element-wise inverse sine.
- [func asinh(MLXArray, stream: StreamOrDevice) -> MLXArray](./asinh%28_,stream%29.md)
  Element-wise inverse hyperbolic sine.
- [func atan(MLXArray, stream: StreamOrDevice) -> MLXArray](./atan%28_,stream%29.md)
  Element-wise inverse tangent.
- [func atanh(MLXArray, stream: StreamOrDevice) -> MLXArray](./atanh%28_,stream%29.md)
  Element-wise inverse hyperbolic tangent.
- [func ceil(MLXArray, stream: StreamOrDevice) -> MLXArray](./ceil%28_,stream%29.md)
  Element-wise ceil.
- [func clip(MLXArray, min: some ScalarOrArray, max: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,min,max,stream%29.md)
  Clip the values of the array between the given minimum and maximum.
- [func clip(MLXArray, max: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./clip%28_,max,stream%29.md)
  Clip the values of the array up to the given maximum.
- [func cos(MLXArray, stream: StreamOrDevice) -> MLXArray](./cos%28_,stream%29.md)
  Element-wise cosine.
- [func cosh(MLXArray, stream: StreamOrDevice) -> MLXArray](./cosh%28_,stream%29.md)
  Element-wise hyperbolic cosine.
- [func divide(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./divide%28_,_,stream%29.md)
  Element-wise division.
- [func erf(MLXArray, stream: StreamOrDevice) -> MLXArray](./erf%28_,stream%29.md)
  Element-wise error function.
- [func erfInverse(MLXArray, stream: StreamOrDevice) -> MLXArray](./erfinverse%28_,stream%29.md)
  Element-wise inverse of [`erf(_:stream:)`](./erf%28_,stream%29.md).
- [func exp(MLXArray, stream: StreamOrDevice) -> MLXArray](./exp%28_,stream%29.md)
  Element-wise exponential.
- [func expm1(MLXArray, stream: StreamOrDevice) -> MLXArray](./expm1%28_,stream%29.md)
  Element-wise exponential minus 1.
- [func floor(MLXArray, stream: StreamOrDevice) -> MLXArray](./floor%28_,stream%29.md)
  Element-wise floor.
- [func floorDivide(MLXArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./floordivide%28_,_,stream%29.md)
  Element-wise integer division..
- [func log(MLXArray, stream: StreamOrDevice) -> MLXArray](./log%28_,stream%29.md)
  Element-wise natural logarithm.
- [func log10(MLXArray, stream: StreamOrDevice) -> MLXArray](./log10%28_,stream%29.md)
  Element-wise base-10 logarithm.
- [func log1p(MLXArray, stream: StreamOrDevice) -> MLXArray](./log1p%28_,stream%29.md)
  Element-wise natural log of one plus the array.
- [func log2(MLXArray, stream: StreamOrDevice) -> MLXArray](./log2%28_,stream%29.md)
  Element-wise base-2 logarithm.
- [func logAddExp(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./logaddexp%28_,_,stream%29.md)
  Element-wise log-add-exp.
- [func logicalNot(MLXArray, stream: StreamOrDevice) -> MLXArray](./logicalnot%28_,stream%29.md)
  Element-wise logical not.
- [func matmul(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./matmul%28_,_,stream%29.md)
  Matrix multiplication.
- [func maximum(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./maximum%28_,_,stream%29.md)
  Element-wise maximum.
- [func minimum(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./minimum%28_,_,stream%29.md)
  Element-wise minimum.
- [func multiply(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./multiply%28_,_,stream%29.md)
  Element-wise multiplication.
- [func negative(MLXArray, stream: StreamOrDevice) -> MLXArray](./negative%28_,stream%29.md)
  Element-wise negation.
- [func notEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./notequal%28_,_,stream%29.md)
  Element-wise not equal.
- [func pow(MLXArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./pow%28_,_,stream%29-7pe7j.md)
  Element-wise power operation.
- [func pow(some ScalarOrArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./pow%28_,_,stream%29-49xi0.md)
  Element-wise power operation.
- [func pow(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./pow%28_,_,stream%29-8ie9c.md)
  Element-wise power operation.
- [func reciprocal(MLXArray, stream: StreamOrDevice) -> MLXArray](./reciprocal%28_,stream%29.md)
  Element-wise reciprocal.
- [func remainder(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./remainder%28_,_,stream%29.md)
  Element-wise remainder of division.
- [func round(MLXArray, decimals: Int, stream: StreamOrDevice) -> MLXArray](./round%28_,decimals,stream%29.md)
  Round to the given number of decimals.
- [func rsqrt(MLXArray, stream: StreamOrDevice) -> MLXArray](./rsqrt%28_,stream%29.md)
  Element-wise reciprocal and square root.
- [func sigmoid(MLXArray, stream: StreamOrDevice) -> MLXArray](./sigmoid%28_,stream%29.md)
  Element-wise logistic sigmoid.
- [func sign(MLXArray, stream: StreamOrDevice) -> MLXArray](./sign%28_,stream%29.md)
  Element-wise sign.
- [func sin(MLXArray, stream: StreamOrDevice) -> MLXArray](./sin%28_,stream%29.md)
  Element-wise sine.
- [func sinh(MLXArray, stream: StreamOrDevice) -> MLXArray](./sinh%28_,stream%29.md)
  Element-wise hyperbolic sine.
- [func softmax(MLXArray, precise: Bool, stream: StreamOrDevice) -> MLXArray](./softmax%28_,precise,stream%29.md)
  Perform the softmax along the given axis.
- [func softmax(MLXArray, axis: Int, precise: Bool, stream: StreamOrDevice) -> MLXArray](./softmax%28_,axis,precise,stream%29.md)
  Perform the softmax along the given axis.
- [func softmax(MLXArray, axes: some Collection<Int>, precise: Bool, stream: StreamOrDevice) -> MLXArray](./softmax%28_,axes,precise,stream%29.md)
  Perform the softmax along the given axis.
- [func sqrt(MLXArray, stream: StreamOrDevice) -> MLXArray](./sqrt%28_,stream%29.md)
  Element-wise square root
- [func square(MLXArray, stream: StreamOrDevice) -> MLXArray](./square%28_,stream%29.md)
  Element-wise square.
- [func subtract(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./subtract%28_,_,stream%29.md)
  Element-wise subtraction.
- [func tan(MLXArray, stream: StreamOrDevice) -> MLXArray](./tan%28_,stream%29.md)
  Element-wise tangent.
- [func tanh(MLXArray, stream: StreamOrDevice) -> MLXArray](./tanh%28_,stream%29.md)
  Element-wise hyperbolic tangent.
- [func which(MLXArray, some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./which%28_,_,_,stream%29.md)
  Alias for [`where(_:_:_:stream:)`](./where%28_,_,_,stream%29.md) – select from `x` or `y` according to `condition`.
### Convolution
- [func conv1d(MLXArray, MLXArray, stride: Int, padding: Int, dilation: Int, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv1d%28_,_,stride,padding,dilation,groups,stream%29.md)
  1D convolution over an input with several channels.
- [func conv2d(MLXArray, MLXArray, stride: IntOrPair, padding: IntOrPair, dilation: IntOrPair, groups: Int, stream: StreamOrDevice) -> MLXArray](./conv2d%28_,_,stride,padding,dilation,groups,stream%29.md)
  2D convolution over an input with several channels.
- [func convolve(some ScalarOrArray, some ScalarOrArray, mode: ConvolveMode, stream: StreamOrDevice) -> MLXArray](./convolve%28_,_,mode,stream%29.md)
  The discrete convolution of 1D arrays.
### Cumulative
- [func cummax(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements along the given axis.
- [func cummax(MLXArray, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummax%28_,reverse,inclusive,stream%29.md)
  Return the cumulative maximum of the elements over the flattened array.
- [func cummin(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummin%28_,axis,reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements along the given axis.
- [func cummin(MLXArray, reverse: Bool, inclusive: Bool, stream: StreamOrDevice) -> MLXArray](./cummin%28_,reverse,inclusive,stream%29.md)
  Return the cumulative minimum of the elements over the flattened array.
- [func cumprod(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumprod%28_,axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements along the given axis.
- [func cumprod(MLXArray, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumprod%28_,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative product of the elements over the flattened array.
- [func cumsum(MLXArray, axis: Int, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumsum%28_,axis,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements along the given axis.
- [func cumsum(MLXArray, reverse: Bool, inclusive: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./cumsum%28_,reverse,inclusive,dtype,stream%29.md)
  Return the cumulative sum of the elements over the flattened array.
### Indexes
- [func argMax(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28_,axis,keepdims,stream%29.md)
  Indices of the maximum values along the axis.
- [func argMax(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmax%28_,keepdims,stream%29.md)
  Indices of the maximum value over the entire array.
- [func argMin(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmin%28_,axis,keepdims,stream%29.md)
  Indices of the minimum values along the axis.
- [func argMin(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./argmin%28_,keepdims,stream%29.md)
  Indices of the minimum value over the entire array.
- [func argPartition(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,axis,stream%29.md)
  Returns the indices that partition the array.
- [func argPartition(MLXArray, kth: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,stream%29.md)
  Returns the indices that partition the flattened array.
- [func argSort(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./argsort%28_,axis,stream%29.md)
  Returns the indices that sort the array.
- [func argSort(MLXArray, stream: StreamOrDevice) -> MLXArray](./argsort%28_,stream%29.md)
  Returns the indices that sort the array.
- [func takeAlong(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./takealong%28_,_,axis,stream%29.md)
  Take values along an axis at the specified indices.
- [func takeAlong(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./takealong%28_,_,stream%29.md)
  Take values along an axis at the specified indices from a flattened array.
- [func take(MLXArray, MLXArray, stream: StreamOrDevice) -> MLXArray](./take%28_,_,stream%29.md)
  Take elements from flattened 1-D array.
- [func take(MLXArray, MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./take%28_,_,axis,stream%29.md)
  Take elements along an axis.
- [func top(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./top%28_,k,stream%29.md)
  Returns the `k` largest elements from the flattened input along a given axis.
- [func top(MLXArray, k: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./top%28_,k,axis,stream%29.md)
  Returns the `k` largest elements from the input along a given axis.
### Factory
- [func zeros(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./zeros%28_,type,stream%29.md)
  Construct an array of zeros.
- [func zeros(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./zeros%28like,dtype,stream%29.md)
  Construct an array of zeros.
- [func ones(some Collection<Int>, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./ones%28_,type,stream%29.md)
  Construct an array of ones.
- [func ones(like: MLXArray, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./ones%28like,dtype,stream%29.md)
  Construct an array of ones.
- [func eye(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./eye%28_,m,k,type,stream%29.md)
  Create an identity matrix or a general diagonal matrix.
- [func full(some Collection<Int>, values: some ScalarOrArray, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./full%28_,values,type,stream%29.md)
  Construct an array with the given value.
- [func full(some Collection<Int>, values: some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./full%28_,values,stream%29.md)
  Construct an array with the given value.
- [func identity(Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./identity%28_,type,stream%29.md)
  Create a square identity matrix.
- [func linspace<T>(T, T, count: Int, endpoint: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./linspace%28_,_,count,endpoint,dtype,stream%29-2b6eu.md)
  Generate `count` evenly spaced numbers over interval `[start, stop]`.
- [func linspace<T>(T, T, count: Int, endpoint: Bool, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./linspace%28_,_,count,endpoint,dtype,stream%29-8k1d2.md)
  Generate `count` evenly spaced numbers over interval `[start, stop]`.
- [func repeated(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./repeated%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [func repeated(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./repeated%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [func `repeat`(MLXArray, count: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./repeat%28_,count,axis,stream%29.md)
  Repeat an array along a specified axis.
- [func `repeat`(MLXArray, count: Int, stream: StreamOrDevice) -> MLXArray](./repeat%28_,count,stream%29.md)
  Repeat a flattened array along axis 0.
- [func tri(Int, m: Int?, k: Int, type: (some HasDType).Type, stream: StreamOrDevice) -> MLXArray](./tri%28_,m,k,type,stream%29.md)
  An array with ones at and below the given diagonal and zeros elsewhere.
- [func tril(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./tril%28_,k,stream%29.md)
  Zeros the array above the given diagonal.
- [func triu(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./triu%28_,k,stream%29.md)
  Zeros the array below the given diagonal.
### I/O
- [func loadArray(url: URL, stream: StreamOrDevice) throws -> MLXArray](./loadarray%28url,stream%29.md)
  Load array from a binary file in `.npy` format.
- [func loadArrays(url: URL, stream: StreamOrDevice) throws -> [String : MLXArray]](./loadarrays%28url,stream%29.md)
  Load dictionary of [`MLXArray`](./mlxarray.md) from a `safetensors` file.
- [func loadArraysAndMetadata(url: URL, stream: StreamOrDevice) throws -> ([String : MLXArray], [String : String])](./loadarraysandmetadata%28url,stream%29.md)
  Load dictionary of [`MLXArray`](./mlxarray.md) and metadata `[String:String]` from a `safetensors` file.
- [func save(array: MLXArray, url: URL, stream: StreamOrDevice) throws](./save%28array,url,stream%29.md)
  Save array to a binary file in `.npy` format.
- [func save(arrays: [String : MLXArray], metadata: [String : String], url: URL, stream: StreamOrDevice) throws](./save%28arrays,metadata,url,stream%29.md)
  Save dictionary of arrays in `safetensors` format.
### Logical
- [func all(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func all(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axis,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func allClose(MLXArray, some ScalarOrArray, rtol: Double, atol: Double, equalNaN: Bool, stream: StreamOrDevice) -> MLXArray](./allclose%28_,_,rtol,atol,equalnan,stream%29.md)
  Approximate comparison of two arrays.
- [func any(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(MLXArray, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func any(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axis,keepdims,stream%29.md)
  An `or` reduction over the given axes.
- [func arrayEqual(MLXArray, some ScalarOrArray, equalNAN: Bool, stream: StreamOrDevice) -> MLXArray](./arrayequal%28_,_,equalnan,stream%29.md)
  Array equality check.
- [func equal(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./equal%28_,_,stream%29.md)
  Element-wise equality.
- [func greater(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./greater%28_,_,stream%29.md)
  Element-wise greater than.
- [func greaterEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./greaterequal%28_,_,stream%29.md)
  Element-wise less greater than or equal.
- [func less(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./less%28_,_,stream%29.md)
  Element-wise less than.
- [func lessEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./lessequal%28_,_,stream%29.md)
  Element-wise less than or equal.
- [func logicalNot(MLXArray, stream: StreamOrDevice) -> MLXArray](./logicalnot%28_,stream%29.md)
  Element-wise logical not.
- [func notEqual(some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./notequal%28_,_,stream%29.md)
  Element-wise not equal.
- [func `where`(MLXArray, some ScalarOrArray, some ScalarOrArray, stream: StreamOrDevice) -> MLXArray](./where%28_,_,_,stream%29.md)
  Select from `x` or `y` according to `condition`.
### Logical Reduction
- [func all(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./all%28_,axes,keepdims,stream%29.md)
  An `and` reduction over the given axes.
- [func any(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./any%28_,axes,keepdims,stream%29.md)
  An `or` reduction over the given axes.
### Aggregating Reduction
- [func logSumExp(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./logsumexp%28_,axes,keepdims,stream%29.md)
  A `log-sum-exp` reduction over the given axes.
- [func product(MLXArray, axis: Int, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./product%28_,axis,keepdims,stream%29.md)
  A `product` reduction over the given axis.
- [func max(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./max%28_,axes,keepdims,stream%29.md)
  A `max` reduction over the given axes.
- [func mean(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./mean%28_,axes,keepdims,stream%29.md)
  A `mean` reduction over the given axes.
- [func min(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./min%28_,axes,keepdims,stream%29.md)
  A `min` reduction over the given axes.
- [func sum(MLXArray, axes: some Collection<Int>, keepDims: Bool, stream: StreamOrDevice) -> MLXArray](./sum%28_,axes,keepdims,stream%29.md)
  Sum reduce the array over the given axes.
- [func variance(MLXArray, axes: some Collection<Int>, keepDims: Bool, ddof: Int, stream: StreamOrDevice) -> MLXArray](./variance%28_,axes,keepdims,ddof,stream%29.md)
  Compute the variance(s) over the given axes
### Shapes
- [func asStrided(MLXArray, (some Collection<Int>)?, strides: (some Collection<Int>)?, offset: Int, stream: StreamOrDevice) -> MLXArray](./asstrided%28_,_,strides,offset,stream%29.md)
  Create a view into the array with the given shape and strides.
- [func broadcast(MLXArray, to: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./broadcast%28_,to,stream%29.md)
  Broadcast an array to the given shape.
- [func concatenated(some Collection<MLXArray>, axis: Int, stream: StreamOrDevice) -> MLXArray](./concatenated%28_,axis,stream%29.md)
  Concatenate the arrays along the given axis.
- [func expandedDimensions(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28_,axes,stream%29.md)
  Add a size one dimension at the given axis.
- [func expandedDimensions(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./expandeddimensions%28_,axis,stream%29.md)
  Add a size one dimension at the given axis.
- [func movedAxis(MLXArray, source: Int, destination: Int, stream: StreamOrDevice) -> MLXArray](./movedaxis%28_,source,destination,stream%29.md)
  Move an axis to a new position.
- [func padded(MLXArray, width: IntOrPair, mode: PadMode, value: MLXArray?, stream: StreamOrDevice) -> MLXArray](./padded%28_,width,mode,value,stream%29.md)
  Pad an array with a constant value.
- [func padded(MLXArray, widths: some Collection<IntOrPair>, mode: PadMode, value: MLXArray?, stream: StreamOrDevice) -> MLXArray](./padded%28_,widths,mode,value,stream%29.md)
  Pad an array with a constant value.
- [func reshaped(MLXArray, some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./reshaped%28_,_,stream%29-9w4n3.md)
  Reshape an array while preserving the size.
- [func reshaped(MLXArray, Int..., stream: StreamOrDevice) -> MLXArray](./reshaped%28_,_,stream%29-96lgr.md)
  Reshape an array while preserving the size.
- [func split(MLXArray, indices: some Collection<Int>, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28_,indices,axis,stream%29.md)
  Split an array along a given axis.
- [func split(MLXArray, parts: Int, axis: Int, stream: StreamOrDevice) -> [MLXArray]](./split%28_,parts,axis,stream%29.md)
  Split an array into equal size pieces along a given axis.
- [func split(MLXArray, axis: Int, stream: StreamOrDevice) -> (MLXArray, MLXArray)](./split%28_,axis,stream%29.md)
  Split an array into 2 equal size pieces along a given axis.
- [func squeezed(MLXArray, stream: StreamOrDevice) -> MLXArray](./squeezed%28_,stream%29.md)
  Remove all length one axes from an array.
- [func squeezed(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./squeezed%28_,axis,stream%29.md)
  Remove length one axes from an array.
- [func squeezed(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./squeezed%28_,axes,stream%29.md)
  Remove length one axes from an array.
- [func stacked(some Collection<MLXArray>, axis: Int, stream: StreamOrDevice) -> MLXArray](./stacked%28_,axis,stream%29.md)
  Stacks the arrays along a new axis.
- [func swappedAxes(MLXArray, Int, Int, stream: StreamOrDevice) -> MLXArray](./swappedaxes%28_,_,_,stream%29.md)
  Swap two axes of an array.
- [func transposed(MLXArray, stream: StreamOrDevice) -> MLXArray](./transposed%28_,stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./transposed%28_,axis,stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(MLXArray, axes: some Collection<Int>, stream: StreamOrDevice) -> MLXArray](./transposed%28_,axes,stream%29.md)
  Transpose the dimensions of the array.
- [func transposed(MLXArray, Int..., stream: StreamOrDevice) -> MLXArray](./transposed%28_,_,stream%29.md)
- [func T(MLXArray, stream: StreamOrDevice) -> MLXArray](./t%28_,stream%29.md)
  Transpose the dimensions of the array.
### Sorting
- [func argSort(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./argsort%28_,axis,stream%29.md)
  Returns the indices that sort the array.
- [func argPartition(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./argpartition%28_,kth,axis,stream%29.md)
  Returns the indices that partition the array.
- [func sorted(MLXArray, stream: StreamOrDevice) -> MLXArray](./sorted%28_,stream%29.md)
  Returns a sorted copy of the flattened array.
- [func sorted(MLXArray, axis: Int, stream: StreamOrDevice) -> MLXArray](./sorted%28_,axis,stream%29.md)
  Returns a sorted copy of the array.
- [func partitioned(MLXArray, kth: Int, stream: StreamOrDevice) -> MLXArray](./partitioned%28_,kth,stream%29.md)
  Returns a partitioned copy of the flattened array such that the smaller `kth` elements are first.
- [func partitioned(MLXArray, kth: Int, axis: Int, stream: StreamOrDevice) -> MLXArray](./partitioned%28_,kth,axis,stream%29.md)
  Returns a partitioned copy of the array such that the smaller `kth` elements are first.
### Quantization
- [func quantizedQuantizedMM(MLXArray, MLXArray, scales: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScaleX: MLXArray?, globalScaleW: MLXArray?, stream: StreamOrDevice) -> MLXArray](./quantizedquantizedmm%28_,_,scales,groupsize,bits,mode,globalscalex,globalscalew,stream%29.md)
  Perform a matrix multiplication using a possibly quantized weight matrix `w` and a non-quantized input `x`. The input `x` is quantized on the fly. The weight matrix `w` is used as-is if it is already quantized; otherwise, it is quantized on the fly.
- [func quantized(MLXArray, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScale: MLXArray?, stream: StreamOrDevice) -> (wq: MLXArray, scales: MLXArray, biases: MLXArray?)](./quantized%28_,groupsize,bits,mode,globalscale,stream%29.md)
  Quantize the matrix `w` using `bits` bits per element.
- [func quantizedMatmul(MLXArray, MLXArray, scales: MLXArray, biases: MLXArray?, transpose: Bool, groupSize: Int?, bits: Int?, mode: QuantizationMode, stream: StreamOrDevice) -> MLXArray](./quantizedmatmul%28_,_,scales,biases,transpose,groupsize,bits,mode,stream%29.md)
- [func dequantized(MLXArray, scales: MLXArray, biases: MLXArray?, groupSize: Int?, bits: Int?, mode: QuantizationMode, globalScale: MLXArray?, dtype: DType?, stream: StreamOrDevice) -> MLXArray](./dequantized%28_,scales,biases,groupsize,bits,mode,globalscale,dtype,stream%29.md)
  Dequantize the matrix `w` using the provided `scales` and `biases` and the `group_size` and `bits` configuration.
### Evaluation and Transformation
- [func eval(MLXArray...)](./eval%28_%29-91pbd.md)
  Evaluate one or more `MLXArray`
- [func eval(some Collection<MLXArray>)](./eval%28_%29-45gpq.md)
  Evaluate one or more `MLXArray`
- [func eval(Any...)](./eval%28_%29-3b2g9.md)
  Evaluate one or more `MLXArray`.
- [func eval(some Sequence<Any>)](./eval%28_%29-3odmu.md)
  Evaluate one or more `MLXArray`.
- [func asyncEval(some Collection<MLXArray>)](./asynceval%28_%29-488lb.md)
  Evaluate one or more `MLXArray` asynchronously.
- [func asyncEval(Any...)](./asynceval%28_%29-6j4zg.md)
  Evaluate one or more `MLXArray` asynchronously.
- [func asyncEval(some Sequence<Any>)](./asynceval%28_%29-2zqay.md)
  Evaluate one or more `MLXArray` asynchronously.
- [func grad((MLXArray) -> MLXArray) -> (MLXArray) -> MLXArray](./grad%28_%29-r8dv.md)
- [func grad((MLXArray) -> [MLXArray]) -> (MLXArray) -> [MLXArray]](./grad%28_%29-7z6i.md)
- [func grad(([MLXArray]) -> [MLXArray], argumentNumbers: some Collection<Int>) -> ([MLXArray]) -> [MLXArray]](./grad%28_,argumentnumbers%29-5qg53.md)
- [func grad(([MLXArray]) -> MLXArray, argumentNumbers: some Collection<Int>) -> ([MLXArray]) -> MLXArray](./grad%28_,argumentnumbers%29-qlix.md)
- [func valueAndGrad<T>((NestedDictionary<String, MLXArray>, T) -> [MLXArray]) -> (NestedDictionary<String, MLXArray>, T) -> ([MLXArray], NestedDictionary<String, MLXArray>)](./valueandgrad%28_%29.md)
  Returns a function that computes the gradient and result of `f`, computing the gradient with respect to the [`NestedDictionary`](./nesteddictionary.md).
- [func valueAndGrad(([MLXArray]) -> [MLXArray], argumentNumbers: some Collection<Int>) -> ([MLXArray]) -> ([MLXArray], [MLXArray])](./valueandgrad%28_,argumentnumbers%29.md)
- [func stopGradient(MLXArray, stream: StreamOrDevice) -> MLXArray](./stopgradient%28_,stream%29.md)
  Stop gradients from being computed.
- [func jvp(([MLXArray]) -> [MLXArray], primals: some Collection<MLXArray>, tangents: some Collection<MLXArray>) -> ([MLXArray], [MLXArray])](./jvp%28_,primals,tangents%29.md)
  Compute the Jacobian-vector product.
- [func vjp(([MLXArray]) -> [MLXArray], primals: some Collection<MLXArray>, cotangents: some Collection<MLXArray>) -> ([MLXArray], [MLXArray])](./vjp%28_,primals,cotangents%29.md)
  Compute the vector-Jacobian product.
### Device
- [func using<R>(device: Device, fn: () throws -> R) rethrows -> R](./using%28device,fn%29.md)
  Execute a block of code using a specific device.
### Other
- [func depends(input: MLXArray, dependencies: [MLXArray]) -> MLXArray](./depends%28input,dependencies%29.md)
  Insert dependencies between arrays in the graph. The outputs are identical to `input` but with dependencies on `dependencies`.
- [func depends(inputs: [MLXArray], dependencies: [MLXArray]) -> [MLXArray]](./depends%28inputs,dependencies%29.md)
  Insert dependencies between arrays in the graph. The outputs are identical to `inputs` but with dependencies on `dependencies`.
- [func diag(MLXArray, k: Int, stream: StreamOrDevice) -> MLXArray](./diag%28_,k,stream%29.md)
  Extract a diagonal or construct a diagonal matrix.
- [func diagonal(MLXArray, offset: Int, axis1: Int, axis2: Int, stream: StreamOrDevice) -> MLXArray](./diagonal%28_,offset,axis1,axis2,stream%29.md)
  Return specified diagonals.
- [func einsum(String, operands: some Collection<MLXArray>, stream: StreamOrDevice) -> MLXArray](./einsum%28_,operands,stream%29.md)
  Perform the Einstein summation convention on the operands.
- [func einsum(String, MLXArray..., stream: StreamOrDevice) -> MLXArray](./einsum%28_,_,stream%29.md)
  Perform the Einstein summation convention on the operands.
- [func hadamardTransform(MLXArray, scale: Float?, stream: StreamOrDevice) -> MLXArray](./hadamardtransform%28_,scale,stream%29.md)
  Perform the Walsh-Hadamard transform along the final axis.
- [func view(MLXArray, dtype: DType, stream: StreamOrDevice) -> MLXArray](./view%28_,dtype,stream%29.md)
  View the array as a different type.
- [func setErrorHandler(((UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void)?, data: UnsafeMutableRawPointer?, dtor: ((UnsafeMutableRawPointer?) -> Void)?)](./seterrorhandler%28_,data,dtor%29.md)
  Sets the error handler. The default error handler will simply print out the error, then exit.
- [let fatalErrorHandler: (UnsafePointer<CChar>?, UnsafeMutableRawPointer?) -> Void](./fatalerrorhandler.md)
  An error handler that calls `fatalError`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/free-functions)*