# MLTensor

**Framework**: Core ML  
**Kind**: struct  
**Role**: Structure

A multi-dimensional array of numerical or Boolean scalars tailored to ML use cases, containing methods to perform transformations and mathematical operations efficiently using a ML compute device.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct MLTensor
```

## Topics

### Creating a tensor
- [init(_:)](./mltensor/init%28_%29.md)
  Creates a one-dimensional tensor from scalars.
- [init(some Collection<MLTensor>, alongAxis: Int)](./mltensor/init%28_,alongaxis%29.md)
  Creates a tensor by stacking the given tensors along the specified axis.
- [init(_:scalarType:)](./mltensor/init%28_,scalartype%29.md)
  Creates a one-dimensional tensor from scalars.
- [init(bytesNoCopy: UnsafeRawBufferPointer, shape: [Int], scalarType: any MLTensorScalar.Type, deallocator: Data.Deallocator)](./mltensor/init%28bytesnocopy,shape,scalartype,deallocator%29.md)
  Creates a tensor with memory content without copying the bytes.
- [init(concatenating: some Collection<MLTensor>, alongAxis: Int)](./mltensor/init%28concatenating,alongaxis%29.md)
  Concatenates `tensors` along the `axis` dimension.
- [init(linearSpaceFrom: Float, through: Float, count: Int)](./mltensor/init%28linearspacefrom,through,count%29.md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.
- [init<Scalar>(linearSpaceFrom: Scalar, through: Scalar, count: Int, scalarType: Scalar.Type)](./mltensor/init%28linearspacefrom,through,count,scalartype%29.md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.
- [init(ones:scalarType:)](./mltensor/init%28ones,scalartype%29.md)
  Creates a tensor with all scalars set to ones.
- [init<Scalar>(randomNormal: [Int], mean: Scalar, standardDeviation: Scalar, seed: UInt64?, scalarType: Scalar.Type)](./mltensor/init%28randomnormal,mean,standarddeviation,seed,scalartype%29.md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a normal distribution.
- [init(randomUniform:in:seed:scalarType:)](./mltensor/init%28randomuniform,in,seed,scalartype%29.md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a uniform distribution in `bounds`.
- [init(rangeFrom: Float, to: Float, by: Float.Stride)](./mltensor/init%28rangefrom,to,by%29.md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [init<Scalar>(rangeFrom: Scalar, to: Scalar, by: Scalar.Stride, scalarType: Scalar.Type)](./mltensor/init%28rangefrom,to,by,scalartype%29.md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [init(repeating: Float, shape: [Int])](./mltensor/init%28repeating,shape%29.md)
  Creates a tensor with the specified shape and a single, repeated scalar value.
- [init<Scalar>(repeating: Scalar, shape: [Int], scalarType: Scalar.Type)](./mltensor/init%28repeating,shape,scalartype%29.md)
  Creates a tensor with the specified shape and a single, repeated scalar value.
- [init(shape: [Int], data: Data, scalarType: any MLTensorScalar.Type)](./mltensor/init%28shape,data,scalartype%29.md)
  Creates a tensor by copying the given block of data.
- [init(shape: [Int], scalars: some Collection<Float>)](./mltensor/init%28shape,scalars%29.md)
  Creates a tensor with the specified shape and contiguous scalars in first-major order.
- [init<Scalar>(shape: [Int], scalars: some Collection, scalarType: Scalar.Type)](./mltensor/init%28shape,scalars,scalartype%29.md)
  Creates a tensor with the specified shape and contiguous scalars in row-major order.
- [init(stacking: some Collection<MLTensor>, alongAxis: Int)](./mltensor/init%28stacking,alongaxis%29.md)
  Stacks the given tensors along the `axis` dimension into a new tensor with rank one higher than the current tensor and each tensor.
- [init(unsafeUninitializedShape: [Int], scalarType: any MLTensorScalar.Type, initializingWith: (UnsafeMutableRawBufferPointer) throws -> Void) rethrows](./mltensor/init%28unsafeuninitializedshape,scalartype,initializingwith%29.md)
  Creates a tensor with the specified shape, then calls the given closure with a buffer covering the tensor’s uninitialized memory.
- [init(zeros:scalarType:)](./mltensor/init%28zeros,scalartype%29.md)
  Creates a tensor with all scalars set to zero.
### Accessing tensor properties
- [var isScalar: Bool](./mltensor/isscalar.md)
  A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.
- [var rank: Int](./mltensor/rank.md)
  The number of dimensions of the tensor.
- [var scalarCount: Int](./mltensor/scalarcount.md)
  The number of scalar elements in the tensor.
- [var scalarType: any MLTensorScalar.Type](./mltensor/scalartype.md)
  The type of scalars in the tensor.
- [var shape: [Int]](./mltensor/shape.md)
  The shape of the tensor.
### Getting the sum
- [func sum(alongAxes:keepRank:)](./mltensor/sum%28alongaxes,keeprank%29.md)
  Returns the sum along the specified axes.
- [func sum(keepRank: Bool) -> MLTensor](./mltensor/sum%28keeprank%29.md)
  Returns the sum along all axes.
### Performing a logical AND operation
- [func all(alongAxes:keepRank:)](./mltensor/all%28alongaxes,keeprank%29.md)
  Computes logical AND on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.
- [func all(keepRank: Bool) -> MLTensor](./mltensor/all%28keeprank%29.md)
  Computes logical AND on elements across all axes of a tensor where the scalar type of the tensor is expected to be Boolean.
### Performing a logical OR operation
- [func any(alongAxes:keepRank:)](./mltensor/any%28alongaxes,keeprank%29.md)
  Computes logical OR on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.
- [func any(keepRank: Bool) -> MLTensor](./mltensor/any%28keeprank%29.md)
  Computes logical OR on elements across all dimensions of a tensor where the scalar type of the tensor is expected to be Boolean.
### Accessing the indicies
- [func argmax() -> MLTensor](./mltensor/argmax%28%29.md)
  Returns the index of the maximum value of the flattened scalars.
- [func argmax(alongAxis: Int, keepRank: Bool) -> MLTensor](./mltensor/argmax%28alongaxis,keeprank%29.md)
  Returns the indices of the maximum values along the specified axis.
- [func argmin() -> MLTensor](./mltensor/argmin%28%29.md)
  Returns the index of the minimum value of the flattened scalars.
- [func argmin(alongAxis: Int, keepRank: Bool) -> MLTensor](./mltensor/argmin%28alongaxis,keeprank%29.md)
  Returns the indices of the minimum values along the specified axis.
- [func argsort(alongAxis: Int, descendingOrder: Bool) -> MLTensor](./mltensor/argsort%28alongaxis,descendingorder%29.md)
  Returns the indices (or arguments) of a tensor that give its sorted order along the specified axis.
### Casting the elements
- [func cast(like: MLTensor) -> MLTensor](./mltensor/cast%28like%29.md)
  Casts the elements of the tensor to the scalar type of the given array.
- [func cast<Scalar>(to: Scalar.Type) -> MLTensor](./mltensor/cast%28to%29.md)
  Casts the elements of the tensor to the given scalar type.
### Computing the absolute, ceiling and floor
- [func abs() -> MLTensor](./mltensor/abs%28%29.md)
  Computes the absolute of the tensor’s elements.
- [func ceil() -> MLTensor](./mltensor/ceil%28%29.md)
  Computes the ceiling of the tensor’s elements.
- [func floor() -> MLTensor](./mltensor/floor%28%29.md)
  Computes the floor of the tensor’s elements.
### Performing arithmetic operations
- [static *(_:_:)](./mltensor/star%28_,_%29.md)
  Computes element-wise multiplication.
- [static func *= (inout MLTensor, MLTensor)](./mltensor/stareq%28_,_%29.md)
  Computes element-wise multiplication.
- [static +(_:_:)](./mltensor/plus%28_,_%29.md)
  Computes element-wise addition.
- [static func += (inout MLTensor, MLTensor)](./mltensor/pluseq%28_,_%29.md)
  Computes element-wise addition.
- [static func - (MLTensor) -> MLTensor](./mltensor/minus%28_%29.md)
  Returns the negation of the tensor.
- [static -(_:_:)](./mltensor/minus%28_,_%29.md)
  Computes element-wise subtraction.
- [static func -= (inout MLTensor, MLTensor)](./mltensor/minuseq%28_,_%29.md)
  Computes element-wise subtraction.
- [static func .! (MLTensor) -> MLTensor](./mltensor/dotnot%28_%29.md)
  Computes logical not on the tensor’s elements.
- [static .!=(_:_:)](./mltensor/dotnoteq%28_,_%29.md)
  Computes element-wise inequality between two tensors.
- [static func .& (MLTensor, MLTensor) -> MLTensor](./mltensor/dotamp%28_,_%29.md)
  Computes element-wise logical AND where both operands are expected contain Boolean scalar elements.
- [static .==(_:_:)](./mltensor/doteqeq%28_,_%29.md)
  Computes element-wise equality between two tensors.
- [static .>(_:_:)](./mltensor/dotop%28_,_%29-3m3ro.md)
  Computes element-wise greater comparison between two tensors.
- [static .<(_:_:)](./mltensor/dotop%28_,_%29-6kfoh.md)
  Computes element-wise less comparison between two tensors.
- [static func .| (MLTensor, MLTensor) -> MLTensor](./mltensor/dotop%28_,_%29-7z7ks.md)
  Computes element-wise logical OR where both operands are expected contain Boolean scalar elements.
- [static func .^ (MLTensor, MLTensor) -> MLTensor](./mltensor/dotop%28_,_%29-8il7w.md)
  Computes element-wise logical XOR where both operands are expected contain Boolean scalar elements.
- [static .>=(_:_:)](./mltensor/dotopeq%28_,_%29-5qa2u.md)
  Computes element-wise greater than or equal to comparison between two tensors.
- [static .<=(_:_:)](./mltensor/dotopeq%28_,_%29-otif.md)
  Computes element-wise less than or equal to comparison between two tensors.
- [static /(_:_:)](./mltensor/op%28_,_%29-5hhe4.md)
  Computes element-wise division.
- [static %(_:_:)](./mltensor/op%28_,_%29-7cfjs.md)
  Computes element-wise remainder of division.
- [static func %= (inout MLTensor, MLTensor)](./mltensor/opeq%28_,_%29-3xllm.md)
  Computes element-wise remainder of division.
- [static func /= (inout MLTensor, MLTensor)](./mltensor/opeq%28_,_%29-53k1k.md)
  Computes element-wise multiplication.
### Applying trigonometric functions
- [func cos() -> MLTensor](./mltensor/cos%28%29.md)
  Computes the cosine of the tensor’s elements.
- [func cosh() -> MLTensor](./mltensor/cosh%28%29.md)
  Computes the hyperbolic cosine of the tensor’s elements.
- [func acos() -> MLTensor](./mltensor/acos%28%29.md)
  Computes the inverse cosine of the tensor’s elements.
- [func acosh() -> MLTensor](./mltensor/acosh%28%29.md)
  Computes the inverse hyperbolic cosine of the tensor’s elements.
- [func sin() -> MLTensor](./mltensor/sin%28%29.md)
  Computes sine of the tensor’s elements.
- [func sinh() -> MLTensor](./mltensor/sinh%28%29.md)
  Computes hyperbolic sine of the tensor’s elements.
- [func asin() -> MLTensor](./mltensor/asin%28%29.md)
  Computes the inverse sine of the tensor’s elements.
- [func asinh() -> MLTensor](./mltensor/asinh%28%29.md)
  Computes the inverse hyperbolic sine of the tensor’s elements.
- [func tan() -> MLTensor](./mltensor/tan%28%29.md)
  Computes tangent of the tensor’s elements.
- [func tanh() -> MLTensor](./mltensor/tanh%28%29.md)
  Computes hyperbolic tangent of the tensor’s elements.
- [func atan() -> MLTensor](./mltensor/atan%28%29.md)
  Computes the inverse tangent of the tensor’s elements.
- [func atanh() -> MLTensor](./mltensor/atanh%28%29.md)
  Computes the inverse hyperbolic tangent of the tensor’s elements.
### Accessing the minimum, maximum and mean
- [func min(alongAxes:keepRank:)](./mltensor/min%28alongaxes,keeprank%29.md)
  Returns the minimum values along the specified axes.
- [func min(keepRank: Bool) -> MLTensor](./mltensor/min%28keeprank%29.md)
  Returns the minimum value in the array.
- [func max(alongAxes:keepRank:)](./mltensor/max%28alongaxes,keeprank%29.md)
  Returns the maximum values along the specified axes.
- [func max(keepRank: Bool) -> MLTensor](./mltensor/max%28keeprank%29.md)
  Returns the maximum value in the array.
- [func mean(alongAxes:keepRank:)](./mltensor/mean%28alongaxes,keeprank%29.md)
  Returns the mean along the specified axes.
- [func mean(keepRank: Bool) -> MLTensor](./mltensor/mean%28keeprank%29.md)
  Returns the mean along all axes.
### Splitting the tensor
- [func split(count: Int, alongAxis: Int) -> [MLTensor]](./mltensor/split%28count,alongaxis%29.md)
  Splits a tensor into multiple tensors. The tensor is split along dimension `axis` into `count` smaller tensors.
- [func split(sizes: [Int], alongAxis: Int) -> [MLTensor]](./mltensor/split%28sizes,alongaxis%29.md)
  Splits a tensor into multiple tensors. The tensor is split  into `sizes.shape[0]` parts.
### Resizing the tensor
- [func resized(to: (newHeight: Int, newWidth: Int), method: MLTensor.ResizeMethod) -> MLTensor](./mltensor/resized%28to,method%29.md)
  Resize the tensor’s spatial dimensions to size using the specified method.
- [MLTensor.ResizeMethod](./mltensor/resizemethod.md)
  A resize algorithm.
### Padding the tensor
- [func padded(forSizes: [(before: Int, after: Int)], mode: MLTensor.PaddingMode) -> MLTensor](./mltensor/padded%28forsizes,mode%29.md)
  Returns a padded tensor according to the specified padding sizes and mode.
- [func padded(forSizes: [(before: Int, after: Int)], with: Float) -> MLTensor](./mltensor/padded%28forsizes,with%29.md)
  Returns a tensor padded with the given constant according to the specified padding sizes.
- [MLTensor.PaddingMode](./mltensor/paddingmode.md)
  A mode that dictates how a tensor is padded.
### Replacing the tensor values
- [func replacing(atIndices: MLTensor, with: some MLTensorScalar, alongAxis: Int) -> MLTensor](./mltensor/replacing%28atindices,with,alongaxis%29.md)
  Replaces slices along the specified indices with the given replacement values.
- [func replacing(with: MLTensor, atIndices: MLTensor, alongAxis: Int) -> MLTensor](./mltensor/replacing%28with,atindices,alongaxis%29.md)
  Replaces slices along the specified indices with the given replacement values.
- [func replacing(with:where:)](./mltensor/replacing%28with,where%29.md)
  Returns a new tensor replacing values from `other` with the corresponding element in `self` where the associated element in `mask` is `true`.
### Gathering slices
- [func gathering(atIndices: MLTensor) -> MLTensor](./mltensor/gathering%28atindices%29.md)
  Returns a tensor by gathering slices at the specified indices.
- [func gathering(atIndices: MLTensor, alongAxis: Int) -> MLTensor](./mltensor/gathering%28atindices,alongaxis%29.md)
  Returns a tensor by gathering slices along the given axis at the specified indices.
### Transposing the tensor
- [func transposed() -> MLTensor](./mltensor/transposed%28%29.md)
  Permutes the tensor with dimensions permuted in reverse order.
- [func transposed(permutation:)](./mltensor/transposed%28permutation%29.md)
  Permutes the dimensions of the tensor in the specified order.
### Unpacking the tensor
- [func unstacked(alongAxis: Int) -> [MLTensor]](./mltensor/unstacked%28alongaxis%29.md)
  Unpacks the given dimension of a rank-`R` tensor into multiple rank-`(R-1)` tensors.
### Getting the shaped representation of the tensor
- [func shapedArray<Scalar>(of: Scalar.Type) async -> MLShapedArray<Scalar>](./mltensor/shapedarray%28of%29.md)
  Returns a materialized representation of the tensor.
### Removing dimensions from the shape of the tensor
- [func squeezingShape() -> MLTensor](./mltensor/squeezingshape%28%29.md)
  Removes all dimensions of size 1 from the shape of the tensor.
- [func squeezingShape(at:)](./mltensor/squeezingshape%28at%29.md)
  Removes the specified dimensions of size 1 from the shape of the tensor.
### Accessing the product along an axes
- [func product(alongAxes:keepRank:)](./mltensor/product%28alongaxes,keeprank%29.md)
  Returns the product along the specified axes.
- [func product(keepRank: Bool) -> MLTensor](./mltensor/product%28keeprank%29.md)
  Returns the product along all axes.
### Getting the largest values
- [func topK(Int) -> (values: MLTensor, indices: MLTensor)](./mltensor/topk%28_%29.md)
  Returns the *k* largest values along the last axis of the tensor.
### Clamping and concatenating
- [func clamped(to:)](./mltensor/clamped%28to%29.md)
  Clamps all elements to the given lower and upper bounds, inclusively.
- [func concatenated(with: MLTensor, alongAxis: Int) -> MLTensor](./mltensor/concatenated%28with,alongaxis%29.md)
  Returns a concatenated tensor along the specified axis.
### Computing the cumulative value
- [func cumulativeProduct(alongAxis: Int) -> MLTensor](./mltensor/cumulativeproduct%28alongaxis%29.md)
  Computes the cumulative product along the specified axis.
- [func cumulativeSum(alongAxis: Int) -> MLTensor](./mltensor/cumulativesum%28alongaxis%29.md)
  Computes the cumulative sum along the specified axis.
### Computing the exponent, pow and square root
- [func exp() -> MLTensor](./mltensor/exp%28%29.md)
  Computes the natural exponent of the tensor’s elements.
- [func exp2() -> MLTensor](./mltensor/exp2%28%29.md)
  Computes the exponent with base two of the tensor’s elements.
- [func pow(_:)](./mltensor/pow%28_%29.md)
  Computes element-wise power of each element with `exponent`.
- [func rsqrt() -> MLTensor](./mltensor/rsqrt%28%29.md)
  Computes reverse square root of the tensor’s elements.
- [func squared() -> MLTensor](./mltensor/squared%28%29.md)
  Computes square of the tensor’s elements.
- [func squareRoot() -> MLTensor](./mltensor/squareroot%28%29.md)
  Computes square root of the tensor’s elements.
- [func log() -> MLTensor](./mltensor/log%28%29.md)
  Computes the natural logarithm of the tensor’s elements.
- [func round() -> MLTensor](./mltensor/round%28%29.md)
  Rounds the tensor’s elements.
- [func matmul(MLTensor) -> MLTensor](./mltensor/matmul%28_%29.md)
  Multiplies two tensors together using matrix multiplication.
### Accessing the extended tensor, sign and reciprocal
- [func expandingShape(at:)](./mltensor/expandingshape%28at%29.md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.
- [func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor](./mltensor/bandpart%28lowerbandcount,upperbandcount%29.md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.
- [func tiled(multiples: [Int]) -> MLTensor](./mltensor/tiled%28multiples%29.md)
  Returns a tensor by replicating its elements multiple times.
- [func sign() -> MLTensor](./mltensor/sign%28%29.md)
  Returns the sign of the tensor’s elements.
- [func reciprocal() -> MLTensor](./mltensor/reciprocal%28%29.md)
  Computes the reciprocal of the tensor’s elements.
### Reshaping the tensor
- [func flattened() -> MLTensor](./mltensor/flattened%28%29.md)
  Reshape to a one-dimensional tensor.
- [func reshaped(to: [Int]) -> MLTensor](./mltensor/reshaped%28to%29.md)
  Reshape to the specified shape.
### Computing the softmax
- [func softmax(alongAxis: Int) -> MLTensor](./mltensor/softmax%28alongaxis%29.md)
  Computes the softmax of the specified tensor along the specified axis.
### Reversing the tensor
- [func reversed(alongAxes:)](./mltensor/reversed%28alongaxes%29.md)
  Returns a new tensor with the specified dimensions reversed.
### Accessing a multiarray’s elements
- [subscript((any MLTensorRangeExpression)?...) -> MLTensor](./mltensor/subscript%28_%29.md)
- [subscript(UnboundedRange, (any MLTensorRangeExpression)?...) -> MLTensor](./mltensor/subscript%28_,_%29.md)
- [subscript((any MLTensorRangeExpression)?, UnboundedRange, (any MLTensorRangeExpression)?...) -> MLTensor](./mltensor/subscript%28_,_,_%29.md)
- [subscript((any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, UnboundedRange, (any MLTensorRangeExpression)?...) -> MLTensor](./mltensor/subscript%28_,_,_,_%29.md)
- [subscript((any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, UnboundedRange, (any MLTensorRangeExpression)?...) -> MLTensor](./mltensor/subscript%28_,_,_,_,_%29.md)
### Default Implementations
- [CustomReflectable Implementations](./mltensor/customreflectable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomReflectable](../Swift/customreflectable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [ExpressibleByBooleanLiteral](../Swift/expressiblebybooleanliteral.md)
- [ExpressibleByFloatLiteral](../Swift/expressiblebyfloatliteral.md)
- [ExpressibleByIntegerLiteral](../Swift/expressiblebyintegerliteral.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Model tensor
- [protocol MLTensorScalar](./mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.
- [protocol MLTensorRangeExpression](./mltensorrangeexpression.md)
  A type that can be used to slice a dimension of a tensor. Don’t use this type directly.
- [func pointwiseMin(_:_:)](./pointwisemin%28_,_%29.md)
  Computes the element-wise minimum of two tensors.
- [func pointwiseMax(_:_:)](./pointwisemax%28_,_%29.md)
  Computes the element-wise minimum between two tensors.
- [func withMLTensorComputePolicy(_:_:)](./withmltensorcomputepolicy%28_,_%29.md)
  Calls the given closure within a task-local context using the specified compute policy to influence what compute device tensor operations are executed on.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor)*