# init(stacking:alongAxis:)

**Framework**: Core ML  
**Kind**: init

Stacks the given tensors along the `axis` dimension into a new tensor with rank one higher than the current tensor and each tensor.

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
init(stacking tensors: some Collection<MLTensor>, alongAxis axis: Int = 0)
```

#### Discussion

Given that `tensors` all have shape `[A, B, C]`, and `tensors.count = N`, then:

- if `axis == 0` then the resulting tensor will have the shape `[N, A, B, C]`.
- if `axis == 1` then the resulting tensor will have the shape `[A, N, B, C]`.
- etc.

For example:

```swift
// 'x' is [1, 4]
// 'y' is [2, 5]
// 'z' is [3, 6]
MLTensor(stacking: [x, y, z]) // is [[1, 4], [2, 5], [3, 6]]
MLTensor(stacking: [x, y, z], alongAxis: 1) // is [[1, 2, 3], [4, 5, 6]]
```

## Parameters

- `tensors`: The tensors to stack. All tensors must have the same shape and scalar type.
- `axis`: The axis along which to stack. Negative values wrap around but must be in the range  , where    is the rank of the provided tensors.

## See Also

- [init(_:)](mltensor/init(_:).md)
  Creates a one-dimensional tensor from scalars.
- [init(some Collection<MLTensor>, alongAxis: Int)](mltensor/init(_:alongaxis:).md)
  Creates a tensor by stacking the given tensors along the specified axis.
- [init(_:scalarType:)](mltensor/init(_:scalartype:).md)
  Creates a one-dimensional tensor from scalars.
- [init(bytesNoCopy: UnsafeRawBufferPointer, shape: [Int], scalarType: any MLTensorScalar.Type, deallocator: Data.Deallocator)](mltensor/init(bytesnocopy:shape:scalartype:deallocator:).md)
  Creates a tensor with memory content without copying the bytes.
- [init(concatenating: some Collection<MLTensor>, alongAxis: Int)](mltensor/init(concatenating:alongaxis:).md)
  Concatenates `tensors` along the `axis` dimension.
- [init(linearSpaceFrom: Float, through: Float, count: Int)](mltensor/init(linearspacefrom:through:count:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.
- [init<Scalar>(linearSpaceFrom: Scalar, through: Scalar, count: Int, scalarType: Scalar.Type)](mltensor/init(linearspacefrom:through:count:scalartype:).md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.
- [init(ones:scalarType:)](mltensor/init(ones:scalartype:).md)
  Creates a tensor with all scalars set to ones.
- [init<Scalar>(randomNormal: [Int], mean: Scalar, standardDeviation: Scalar, seed: UInt64?, scalarType: Scalar.Type)](mltensor/init(randomnormal:mean:standarddeviation:seed:scalartype:).md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a normal distribution.
- [init(randomUniform:in:seed:scalarType:)](mltensor/init(randomuniform:in:seed:scalartype:).md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(stacking:alongaxis:))*