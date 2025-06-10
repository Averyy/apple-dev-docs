# MLTensor

**Framework**: Core ML  
**Kind**: struct

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

### Operators
- [static func * (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/*(_:_:)-1ovun.md)
  Computes element-wise multiplication.
- [static func * (MLTensor, MLTensor) -> MLTensor](mltensor/*(_:_:)-3pdvi.md)
  Computes element-wise multiplication.
- [static func * (some MLTensorScalar & Numeric, MLTensor) -> MLTensor](mltensor/*(_:_:)-9w6om.md)
  Computes element-wise multiplication.
- [static func *= (inout MLTensor, MLTensor)](mltensor/*=(_:_:).md)
  Computes element-wise multiplication.
- [static func + (some MLTensorScalar & Numeric, MLTensor) -> MLTensor](mltensor/+(_:_:)-64bxm.md)
  Computes element-wise addition.
- [static func + (MLTensor, MLTensor) -> MLTensor](mltensor/+(_:_:)-83w29.md)
  Computes element-wise addition.
- [static func + (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/+(_:_:)-958w1.md)
  Computes element-wise addition.
- [static func += (inout MLTensor, MLTensor)](mltensor/+=(_:_:).md)
  Computes element-wise addition.
- [static func - (MLTensor) -> MLTensor](mltensor/-(_:).md)
  Returns the negation of the tensor.
- [static func - (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/-(_:_:)-65yzi.md)
  Computes element-wise subtraction.
- [static func - (some MLTensorScalar & Numeric, MLTensor) -> MLTensor](mltensor/-(_:_:)-6en2e.md)
  Computes element-wise subtraction.
- [static func - (MLTensor, MLTensor) -> MLTensor](mltensor/-(_:_:)-7jko5.md)
  Computes element-wise subtraction.
- [static func -= (inout MLTensor, MLTensor)](mltensor/-=(_:_:).md)
  Computes element-wise subtraction.
- [static func .! (MLTensor) -> MLTensor](mltensor/'.!(_:).md)
  Computes logical not on the tensor’s elements.
- [static func .!= (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/'.!=(_:_:)-90xyy.md)
  Computes element-wise inequality between two tensors.
- [static func .!= (MLTensor, MLTensor) -> MLTensor](mltensor/'.!=(_:_:)-9i2ns.md)
  Computes element-wise inequality between two tensors.
- [static func .& (MLTensor, MLTensor) -> MLTensor](mltensor/'.&(_:_:).md)
  Computes element-wise logical AND where both operands are expected contain Boolean scalar elements.
- [static func .== (MLTensor, MLTensor) -> MLTensor](mltensor/'.==(_:_:)-8ejfu.md)
  Computes element-wise equality between two tensors.
- [static func .== (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/'.==(_:_:)-9lqot.md)
  Computes element-wise equality between two tensors.
- [static func .> (MLTensor, MLTensor) -> MLTensor](mltensor/'._(_:_:)-32m7y.md)
  Computes element-wise greater comparison between two tensors.
- [static func .> (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/'._(_:_:)-6llkp.md)
  Computes element-wise greater comparison between two tensors.
- [static func .< (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/'._(_:_:)-7406y.md)
  Computes element-wise less comparison between two tensors.
- [static func .< (MLTensor, MLTensor) -> MLTensor](mltensor/'._(_:_:)-7b1mq.md)
  Computes element-wise less comparison between two tensors.
- [static func .| (MLTensor, MLTensor) -> MLTensor](mltensor/'._(_:_:)-7z7ks.md)
  Computes element-wise logical OR where both operands are expected contain Boolean scalar elements.
- [static func .^ (MLTensor, MLTensor) -> MLTensor](mltensor/'._(_:_:)-8il7w.md)
  Computes element-wise logical XOR where both operands are expected contain Boolean scalar elements.
- [static func .<= (MLTensor, MLTensor) -> MLTensor](mltensor/'._=(_:_:)-1rc0m.md)
  Computes element-wise less than or equal to comparison between two tensors.
- [static func .>= (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/'._=(_:_:)-2zak0.md)
  Computes element-wise greater than or equal to comparison between two tensors.
- [static func .<= (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/'._=(_:_:)-4y1x4.md)
  Computes element-wise less than or equal to comparison between two tensors.
- [static func .>= (MLTensor, MLTensor) -> MLTensor](mltensor/'._=(_:_:)-78naz.md)
  Computes element-wise greater than or equal to comparison between two tensors.
- [static func / (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/_(_:_:)-11647.md)
  Computes element-wise division.
- [static func % (MLTensor, MLTensor) -> MLTensor](mltensor/_(_:_:)-1ipto.md)
  Computes element-wise remainder of division.
- [static func % (some MLTensorScalar & Numeric, MLTensor) -> MLTensor](mltensor/_(_:_:)-1oy6l.md)
  Computes element-wise remainder of division.
- [static func / (MLTensor, MLTensor) -> MLTensor](mltensor/_(_:_:)-3fkva.md)
  Computes element-wise division.
- [static func % (MLTensor, some MLTensorScalar & Numeric) -> MLTensor](mltensor/_(_:_:)-4w3ly.md)
  Computes element-wise remainder of division.
- [static func / (some MLTensorScalar & Numeric, MLTensor) -> MLTensor](mltensor/_(_:_:)-78x58.md)
  Computes element-wise division.
- [static func %= (inout MLTensor, MLTensor)](mltensor/_=(_:_:)-3xllm.md)
  Computes element-wise remainder of division.
- [static func /= (inout MLTensor, MLTensor)](mltensor/_=(_:_:)-53k1k.md)
  Computes element-wise multiplication.
### Initializers
- [init<ShapedArray>(ShapedArray)](mltensor/init(_:)-179ei.md)
  Creates a tensor from a ML shaped array.
- [init(some Collection<Float>)](mltensor/init(_:)-3nevy.md)
  Creates a one-dimensional tensor from scalars.
- [init(some Collection<Int32>)](mltensor/init(_:)-949ue.md)
  Creates a one-dimensional tensor from scalars.
- [init(some Collection<MLTensor>, alongAxis: Int)](mltensor/init(_:alongaxis:).md)
  Creates a tensor by stacking the given tensors along the specified axis.
- [init<Scalar>(Scalar, scalarType: Scalar.Type)](mltensor/init(_:scalartype:)-3f5yt.md)
  Creates a zero-dimensional tensor from a scalar value.
- [init<Scalar>(some Collection, scalarType: Scalar.Type)](mltensor/init(_:scalartype:)-3qoyj.md)
  Creates a one-dimensional tensor from scalars.
- [init(bytesNoCopy: UnsafeRawBufferPointer, shape: [Int], scalarType: any MLTensorScalar.Type, deallocator: Data.Deallocator)](mltensor/init(bytesnocopy:shape:scalartype:deallocator:).md)
  Creates a tensor with memory content without copying the bytes.
- [init(concatenating: some Collection<MLTensor>, alongAxis: Int)](mltensor/init(concatenating:alongaxis:).md)
  Concatenates `tensors` along the `axis` dimension.
- [init(linearSpaceFrom: Float, through: Float, count: Int)](mltensor/init(linearspacefrom:through:count:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.
- [init<Scalar>(linearSpaceFrom: Scalar, through: Scalar, count: Int, scalarType: Scalar.Type)](mltensor/init(linearspacefrom:through:count:scalartype:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.
- [init<Scalar>(ones: [Int], scalarType: Scalar.Type)](mltensor/init(ones:scalartype:)-6pvyp.md)
  Creates a tensor with all scalars set to ones.
- [init<Scalar>(ones: [Int], scalarType: Scalar.Type)](mltensor/init(ones:scalartype:)-8sg3n.md)
  Creates a tensor with all scalars set to one.
- [init<Scalar>(randomNormal: [Int], mean: Scalar, standardDeviation: Scalar, seed: UInt64?, scalarType: Scalar.Type)](mltensor/init(randomnormal:mean:standarddeviation:seed:scalartype:).md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a normal distribution.
- [init<Scalar>(randomUniform: [Int], in: ClosedRange<Scalar>, seed: UInt64?, scalarType: Scalar.Type)](mltensor/init(randomuniform:in:seed:scalartype:)-4ktle.md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a uniform distribution in `bounds`.
- [init<Scalar>(randomUniform: [Int], in: Range<Scalar>, seed: UInt64?, scalarType: Scalar.Type)](mltensor/init(randomuniform:in:seed:scalartype:)-9sn38.md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a uniform distribution in `bounds`.
- [init(rangeFrom: Float, to: Float, by: Float.Stride)](mltensor/init(rangefrom:to:by:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [init<Scalar>(rangeFrom: Scalar, to: Scalar, by: Scalar.Stride, scalarType: Scalar.Type)](mltensor/init(rangefrom:to:by:scalartype:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [init(repeating: Float, shape: [Int])](mltensor/init(repeating:shape:).md)
  Creates a tensor with the specified shape and a single, repeated scalar value.
- [init<Scalar>(repeating: Scalar, shape: [Int], scalarType: Scalar.Type)](mltensor/init(repeating:shape:scalartype:).md)
  Creates a tensor with the specified shape and a single, repeated scalar value.
- [init(shape: [Int], data: Data, scalarType: any MLTensorScalar.Type)](mltensor/init(shape:data:scalartype:).md)
  Creates a tensor by copying the given block of data.
- [init(shape: [Int], scalars: some Collection<Float>)](mltensor/init(shape:scalars:).md)
  Creates a tensor with the specified shape and contiguous scalars in first-major order.
- [init<Scalar>(shape: [Int], scalars: some Collection, scalarType: Scalar.Type)](mltensor/init(shape:scalars:scalartype:).md)
  Creates a tensor with the specified shape and contiguous scalars in row-major order.
- [init(stacking: some Collection<MLTensor>, alongAxis: Int)](mltensor/init(stacking:alongaxis:).md)
  Stacks the given tensors along the `axis` dimension into a new tensor with rank one higher than the current tensor and each tensor.
- [init(unsafeUninitializedShape: [Int], scalarType: any MLTensorScalar.Type, initializingWith: (UnsafeMutableRawBufferPointer) throws -> Void) rethrows](mltensor/init(unsafeuninitializedshape:scalartype:initializingwith:).md)
  Creates a tensor with the specified shape, then calls the given closure with a buffer covering the tensor’s uninitialized memory.
- [init<Scalar>(zeros: [Int], scalarType: Scalar.Type)](mltensor/init(zeros:scalartype:)-2afw9.md)
  Creates a tensor with all scalars set to zero.
- [init<Scalar>(zeros: [Int], scalarType: Scalar.Type)](mltensor/init(zeros:scalartype:)-50e0f.md)
  Creates a tensor with all scalars set to zero.
### Instance Properties
- [var isScalar: Bool](mltensor/isscalar.md)
  A Boolean value indicating whether the tensor is a scalar (when the `rank` is equal to `0`) or not.
- [var rank: Int](mltensor/rank.md)
  The number of dimensions of the tensor.
- [var scalarCount: Int](mltensor/scalarcount.md)
  The number of scalar elements in the tensor.
- [var scalarType: any MLTensorScalar.Type](mltensor/scalartype.md)
  The type of scalars in the tensor.
- [var shape: [Int]](mltensor/shape.md)
  The shape of the tensor.
### Instance Methods
- [func abs() -> MLTensor](mltensor/abs.md)
  Computes the absolute of the tensor’s elements.
- [func acos() -> MLTensor](mltensor/acos.md)
  Computes the inverse cosine of the tensor’s elements.
- [func acosh() -> MLTensor](mltensor/acosh.md)
  Computes the inverse hyperbolic cosine of the tensor’s elements.
- [func all(alongAxes: Int..., keepRank: Bool) -> MLTensor](mltensor/all(alongaxes:keeprank:)-2d8f6.md)
  Computes logical AND on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.
- [func all(alongAxes: [Int], keepRank: Bool) -> MLTensor](mltensor/all(alongaxes:keeprank:)-7qb8a.md)
  Computes logical AND on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.
- [func all(keepRank: Bool) -> MLTensor](mltensor/all(keeprank:).md)
  Computes logical AND on elements across all axes of a tensor where the scalar type of the tensor is expected to be Boolean.
- [func any(alongAxes: Int..., keepRank: Bool) -> MLTensor](mltensor/any(alongaxes:keeprank:)-2ovx0.md)
  Computes logical OR on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.
- [func any(alongAxes: [Int], keepRank: Bool) -> MLTensor](mltensor/any(alongaxes:keeprank:)-8lpdi.md)
  Computes logical OR on elements across the specified axes of a tensor where the scalar type of the tensor is expected to be Boolean.
- [func any(keepRank: Bool) -> MLTensor](mltensor/any(keeprank:).md)
  Computes logical OR on elements across all dimensions of a tensor where the scalar type of the tensor is expected to be Boolean.
- [func argmax() -> MLTensor](mltensor/argmax.md)
  Returns the index of the maximum value of the flattened scalars.
- [func argmax(alongAxis: Int, keepRank: Bool) -> MLTensor](mltensor/argmax(alongaxis:keeprank:).md)
  Returns the indices of the maximum values along the specified axis.
- [func argmin() -> MLTensor](mltensor/argmin.md)
  Returns the index of the minimum value of the flattened scalars.
- [func argmin(alongAxis: Int, keepRank: Bool) -> MLTensor](mltensor/argmin(alongaxis:keeprank:).md)
  Returns the indices of the minimum values along the specified axis.
- [func argsort(alongAxis: Int, descendingOrder: Bool) -> MLTensor](mltensor/argsort(alongaxis:descendingorder:).md)
  Returns the indices (or arguments) of a tensor that give its sorted order along the specified axis.
- [func asin() -> MLTensor](mltensor/asin.md)
  Computes the inverse sine of the tensor’s elements.
- [func asinh() -> MLTensor](mltensor/asinh.md)
  Computes the inverse hyperbolic sine of the tensor’s elements.
- [func atan() -> MLTensor](mltensor/atan.md)
  Computes the inverse tangent of the tensor’s elements.
- [func atanh() -> MLTensor](mltensor/atanh.md)
  Computes the inverse hyperbolic tangent of the tensor’s elements.
- [func bandPart(lowerBandCount: Int, upperBandCount: Int) -> MLTensor](mltensor/bandpart(lowerbandcount:upperbandcount:).md)
  Returns a new tensor with the same shape where everything outside a central band in each innermost matrix is set to zero.
- [func cast(like: MLTensor) -> MLTensor](mltensor/cast(like:).md)
  Casts the elements of the tensor to the scalar type of the given array.
- [func cast<Scalar>(to: Scalar.Type) -> MLTensor](mltensor/cast(to:).md)
  Casts the elements of the tensor to the given scalar type.
- [func ceil() -> MLTensor](mltensor/ceil.md)
  Computes the ceiling of the tensor’s elements.
- [func clamped(to: PartialRangeFrom<Float>) -> MLTensor](mltensor/clamped(to:)-1dntg.md)
  Clamps all elements to the given lower bound, inclusively.
- [func clamped(to: PartialRangeThrough<Float>) -> MLTensor](mltensor/clamped(to:)-1objz.md)
  Clamps all elements to the given upper bound, inclusively.
- [func clamped(to: ClosedRange<Float>) -> MLTensor](mltensor/clamped(to:)-8wqqn.md)
  Clamps all elements to the given lower and upper bounds, inclusively.
- [func concatenated(with: MLTensor, alongAxis: Int) -> MLTensor](mltensor/concatenated(with:alongaxis:).md)
  Returns a concatenated tensor along the specified axis.
- [func cos() -> MLTensor](mltensor/cos.md)
  Computes the cosine of the tensor’s elements.
- [func cosh() -> MLTensor](mltensor/cosh.md)
  Computes the hyperbolic cosine of the tensor’s elements.
- [func cumulativeProduct(alongAxis: Int) -> MLTensor](mltensor/cumulativeproduct(alongaxis:).md)
  Computes the cumulative product along the specified axis.
- [func cumulativeSum(alongAxis: Int) -> MLTensor](mltensor/cumulativesum(alongaxis:).md)
  Computes the cumulative sum along the specified axis.
- [func exp() -> MLTensor](mltensor/exp.md)
  Computes the natural exponent of the tensor’s elements.
- [func exp2() -> MLTensor](mltensor/exp2.md)
  Computes the exponent with base two of the tensor’s elements.
- [func expandingShape(at: Int...) -> MLTensor](mltensor/expandingshape(at:)-1daz8.md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.
- [func expandingShape(at: [Int]) -> MLTensor](mltensor/expandingshape(at:)-j7nc.md)
  Returns a shape-expanded tensor with a dimension of 1 inserted at the specified shape indices.
- [func flattened() -> MLTensor](mltensor/flattened.md)
  Reshape to a one-dimensional tensor.
- [func floor() -> MLTensor](mltensor/floor.md)
  Computes the floor of the tensor’s elements.
- [func gathering(atIndices: MLTensor) -> MLTensor](mltensor/gathering(atindices:).md)
  Returns a tensor by gathering slices at the specified indices.
- [func gathering(atIndices: MLTensor, alongAxis: Int) -> MLTensor](mltensor/gathering(atindices:alongaxis:).md)
  Returns a tensor by gathering slices along the given axis at the specified indices.
- [func log() -> MLTensor](mltensor/log.md)
  Computes the natural logarithm of the tensor’s elements.
- [func matmul(MLTensor) -> MLTensor](mltensor/matmul(_:).md)
  Multiplies two tensors together using matrix multiplication.
- [func max(alongAxes: [Int], keepRank: Bool) -> MLTensor](mltensor/max(alongaxes:keeprank:)-23p32.md)
  Returns the maximum values along the specified axes.
- [func max(alongAxes: Int..., keepRank: Bool) -> MLTensor](mltensor/max(alongaxes:keeprank:)-m8re.md)
  Returns the maximum values along the specified axes.
- [func max(keepRank: Bool) -> MLTensor](mltensor/max(keeprank:).md)
  Returns the maximum value in the array.
- [func mean(alongAxes: [Int], keepRank: Bool) -> MLTensor](mltensor/mean(alongaxes:keeprank:)-2ii3s.md)
  Returns the mean along the specified axes.
- [func mean(alongAxes: Int..., keepRank: Bool) -> MLTensor](mltensor/mean(alongaxes:keeprank:)-67zvf.md)
  Returns the mean along the specified axes.
- [func mean(keepRank: Bool) -> MLTensor](mltensor/mean(keeprank:).md)
  Returns the mean along all axes.
- [func min(alongAxes: Int..., keepRank: Bool) -> MLTensor](mltensor/min(alongaxes:keeprank:)-5dbgj.md)
  Returns the minimum values along the specified axes.
- [func min(alongAxes: [Int], keepRank: Bool) -> MLTensor](mltensor/min(alongaxes:keeprank:)-62xw5.md)
  Returns the minimum values along the specified axes.
- [func min(keepRank: Bool) -> MLTensor](mltensor/min(keeprank:).md)
  Returns the minimum value in the array.
- [func padded(forSizes: [(before: Int, after: Int)], mode: MLTensor.PaddingMode) -> MLTensor](mltensor/padded(forsizes:mode:).md)
  Returns a padded tensor according to the specified padding sizes and mode.
- [func padded(forSizes: [(before: Int, after: Int)], with: Float) -> MLTensor](mltensor/padded(forsizes:with:).md)
  Returns a tensor padded with the given constant according to the specified padding sizes.
- [func pow(some MLTensorScalar & Numeric) -> MLTensor](mltensor/pow(_:)-1yxrh.md)
  Computes element-wise power of each element with `exponent`.
- [func pow(MLTensor) -> MLTensor](mltensor/pow(_:)-44j8r.md)
  Computes element-wise power of each element with `exponent`.
- [func product(alongAxes: Int..., keepRank: Bool) -> MLTensor](mltensor/product(alongaxes:keeprank:)-157l4.md)
  Returns the product along the specified axes.
- [func product(alongAxes: [Int], keepRank: Bool) -> MLTensor](mltensor/product(alongaxes:keeprank:)-8k0j4.md)
  Returns the product along the specified axes.
- [func product(keepRank: Bool) -> MLTensor](mltensor/product(keeprank:).md)
  Returns the product along all axes.
- [func reciprocal() -> MLTensor](mltensor/reciprocal.md)
  Computes the reciprocal of the tensor’s elements.
- [func replacing(atIndices: MLTensor, with: some MLTensorScalar, alongAxis: Int) -> MLTensor](mltensor/replacing(atindices:with:alongaxis:).md)
  Replaces slices along the specified indices with the given replacement values.
- [func replacing(with: MLTensor, atIndices: MLTensor, alongAxis: Int) -> MLTensor](mltensor/replacing(with:atindices:alongaxis:).md)
  Replaces slices along the specified indices with the given replacement values.
- [func replacing(with: MLTensor, where: MLTensor) -> MLTensor](mltensor/replacing(with:where:)-1mnn.md)
  Returns a new tensor replacing values from `other` with the corresponding element in `self` where the associated element in `mask` is `true`.
- [func replacing(with: some MLTensorScalar, where: MLTensor) -> MLTensor](mltensor/replacing(with:where:)-8kotd.md)
  Returns a new tensor replacing the value of `other` with the corresponding element in `self` where the associated element in `mask` is `true`.
- [func reshaped(to: [Int]) -> MLTensor](mltensor/reshaped(to:).md)
  Reshape to the specified shape.
- [func resized(to: (newHeight: Int, newWidth: Int), method: MLTensor.ResizeMethod) -> MLTensor](mltensor/resized(to:method:).md)
  Resize the tensor’s spatial dimensions to size using the specified method.
- [func reversed(alongAxes: Int...) -> MLTensor](mltensor/reversed(alongaxes:)-2zg3v.md)
  Returns a new tensor with the specified dimensions reversed.
- [func reversed(alongAxes: [Int]) -> MLTensor](mltensor/reversed(alongaxes:)-5h7to.md)
  Returns a new tensor with the specified dimensions reversed.
- [func round() -> MLTensor](mltensor/round.md)
  Rounds the tensor’s elements.
- [func rsqrt() -> MLTensor](mltensor/rsqrt.md)
  Computes reverse square root of the tensor’s elements.
- [func shapedArray<Scalar>(of: Scalar.Type) async -> MLShapedArray<Scalar>](mltensor/shapedarray(of:).md)
  Returns a materialized representation of the tensor.
- [func sign() -> MLTensor](mltensor/sign.md)
  Returns the sign of the tensor’s elements.
- [func sin() -> MLTensor](mltensor/sin.md)
  Computes sine of the tensor’s elements.
- [func sinh() -> MLTensor](mltensor/sinh.md)
  Computes hyperbolic sine of the tensor’s elements.
- [func softmax(alongAxis: Int) -> MLTensor](mltensor/softmax(alongaxis:).md)
  Computes the softmax of the specified tensor along the specified axis.
- [func split(count: Int, alongAxis: Int) -> [MLTensor]](mltensor/split(count:alongaxis:).md)
  Splits a tensor into multiple tensors. The tensor is split along dimension `axis` into `count` smaller tensors.
- [func split(sizes: [Int], alongAxis: Int) -> [MLTensor]](mltensor/split(sizes:alongaxis:).md)
  Splits a tensor into multiple tensors. The tensor is split  into `sizes.shape[0]` parts.
- [func squareRoot() -> MLTensor](mltensor/squareroot.md)
  Computes square root of the tensor’s elements.
- [func squared() -> MLTensor](mltensor/squared.md)
  Computes square of the tensor’s elements.
- [func squeezingShape() -> MLTensor](mltensor/squeezingshape.md)
  Removes all dimensions of size 1 from the shape of the tensor.
- [func squeezingShape(at: Int...) -> MLTensor](mltensor/squeezingshape(at:)-4lgo4.md)
  Removes the specified dimensions of size 1 from the shape of the tensor.
- [func squeezingShape(at: [Int]) -> MLTensor](mltensor/squeezingshape(at:)-8u1e.md)
  Removes the specified dimensions of size 1 from the shape of the tensor.
- [func sum(alongAxes: Int..., keepRank: Bool) -> MLTensor](mltensor/sum(alongaxes:keeprank:)-1c1j6.md)
  Returns the sum along the specified axes.
- [func sum(alongAxes: [Int], keepRank: Bool) -> MLTensor](mltensor/sum(alongaxes:keeprank:)-58tnj.md)
  Returns the sum along the specified axes.
- [func sum(keepRank: Bool) -> MLTensor](mltensor/sum(keeprank:).md)
  Returns the sum along all axes.
- [func tan() -> MLTensor](mltensor/tan.md)
  Computes tangent of the tensor’s elements.
- [func tanh() -> MLTensor](mltensor/tanh.md)
  Computes hyperbolic tangent of the tensor’s elements.
- [func tiled(multiples: [Int]) -> MLTensor](mltensor/tiled(multiples:).md)
  Returns a tensor by replicating its elements multiple times.
- [func topK(Int) -> (values: MLTensor, indices: MLTensor)](mltensor/topk(_:).md)
  Returns the  largest values along the last axis of the tensor.
- [func transposed() -> MLTensor](mltensor/transposed.md)
  Permutes the tensor with dimensions permuted in reverse order.
- [func transposed(permutation: [Int]) -> MLTensor](mltensor/transposed(permutation:)-5t35l.md)
  Permutes the dimensions of the tensor in the specified order.
- [func transposed(permutation: Int...) -> MLTensor](mltensor/transposed(permutation:)-5w0x9.md)
  Permutes the dimensions of the tensor in the specified order.
- [func unstacked(alongAxis: Int) -> [MLTensor]](mltensor/unstacked(alongaxis:).md)
  Unpacks the given dimension of a rank-`R` tensor into multiple rank-`(R-1)` tensors.
### Subscripts
- [subscript((any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:).md)
- [subscript((UnboundedRange_) -> (), (any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:_:).md)
- [subscript((any MLTensorRangeExpression)?, (UnboundedRange_) -> (), (any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:_:_:).md)
- [subscript((any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, (UnboundedRange_) -> (), (any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:_:_:_:).md)
- [subscript((any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, (any MLTensorRangeExpression)?, (UnboundedRange_) -> (), (any MLTensorRangeExpression)?...) -> MLTensor](mltensor/subscript(_:_:_:_:_:).md)
### Enumerations
- [MLTensor.PaddingMode](mltensor/paddingmode.md)
  A mode that dictates how a tensor is padded.
- [MLTensor.ResizeMethod](mltensor/resizemethod.md)
  A resize algorithm.
### Default Implementations
- [CustomReflectable Implementations](mltensor/customreflectable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [ExpressibleByBooleanLiteral](../Swift/ExpressibleByBooleanLiteral.md)
- [ExpressibleByFloatLiteral](../Swift/ExpressibleByFloatLiteral.md)
- [ExpressibleByIntegerLiteral](../Swift/ExpressibleByIntegerLiteral.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol MLTensorScalar](mltensorscalar.md)
  A type that represents the tensor scalar types supported by the framework. Don’t use this type directly.
- [protocol MLTensorRangeExpression](mltensorrangeexpression.md)
  A type that can be used to slice a dimension of a tensor. Don’t use this type directly.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor)*