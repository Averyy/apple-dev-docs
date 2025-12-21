# init(rangeFrom:to:by:)

**Framework**: Core ML  
**Kind**: init

Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.

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
init(rangeFrom start: Float, to end: Float, by stride: Float.Stride)
```

## Parameters

- `start`: The starting value to use for the sequence. If the sequence contains any values, the first one is  .
- `end`: An end value to limit the sequence.   is never an element of the resulting sequence.
- `stride`: The amount to step by with each iteration.   must be positive.

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(rangefrom:to:by:))*