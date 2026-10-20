# init(_:alongAxis:)

**Framework**: Core ML  
**Kind**: init  
**Role**: Initializer

Creates a tensor by stacking the given tensors along the specified axis.

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
init(_ elements: some Collection<MLTensor>, alongAxis axis: Int = 0)
```

## Parameters

- `axis`: The axis along which to stack. Negative values wrap around.

## See Also

### Creating a tensor
- [init(_:)](./init%28_%29.md)
  Creates a one-dimensional tensor from scalars.
- [init(_:scalarType:)](./init%28_,scalartype%29.md)
  Creates a one-dimensional tensor from scalars.
- [init(bytesNoCopy: UnsafeRawBufferPointer, shape: [Int], scalarType: any MLTensorScalar.Type, deallocator: Data.Deallocator)](./init%28bytesnocopy,shape,scalartype,deallocator%29.md)
  Creates a tensor with memory content without copying the bytes.
- [init(concatenating: some Collection<MLTensor>, alongAxis: Int)](./init%28concatenating,alongaxis%29.md)
  Concatenates `tensors` along the `axis` dimension.
- [init(linearSpaceFrom: Float, through: Float, count: Int)](./init%28linearspacefrom,through,count%29.md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.
- [init<Scalar>(linearSpaceFrom: Scalar, through: Scalar, count: Int, scalarType: Scalar.Type)](./init%28linearspacefrom,through,count,scalartype%29.md)
  Creates a one-dimensional tensor representing a sequence from a starting value, up to and including an end value, spaced evenly to generate the number of values specified.
- [init(ones:scalarType:)](./init%28ones,scalartype%29.md)
  Creates a tensor with all scalars set to ones.
- [init<Scalar>(randomNormal: [Int], mean: Scalar, standardDeviation: Scalar, seed: UInt64?, scalarType: Scalar.Type)](./init%28randomnormal,mean,standarddeviation,seed,scalartype%29.md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a normal distribution.
- [init(randomUniform:in:seed:scalarType:)](./init%28randomuniform,in,seed,scalartype%29.md)
  Creates a tensor with the specified shape, randomly sampling scalar values from a uniform distribution in `bounds`.
- [init(rangeFrom: Float, to: Float, by: Float.Stride)](./init%28rangefrom,to,by%29.md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [init<Scalar>(rangeFrom: Scalar, to: Scalar, by: Scalar.Stride, scalarType: Scalar.Type)](./init%28rangefrom,to,by,scalartype%29.md)
  Creates a one-dimensional tensor representing a sequence from a starting value to, but not including, an end value, stepping by the specified amount.
- [init(repeating: Float, shape: [Int])](./init%28repeating,shape%29.md)
  Creates a tensor with the specified shape and a single, repeated scalar value.
- [init<Scalar>(repeating: Scalar, shape: [Int], scalarType: Scalar.Type)](./init%28repeating,shape,scalartype%29.md)
  Creates a tensor with the specified shape and a single, repeated scalar value.
- [init(shape: [Int], data: Data, scalarType: any MLTensorScalar.Type)](./init%28shape,data,scalartype%29.md)
  Creates a tensor by copying the given block of data.
- [init(shape: [Int], scalars: some Collection<Float>)](./init%28shape,scalars%29.md)
  Creates a tensor with the specified shape and contiguous scalars in first-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(_:alongaxis:))*