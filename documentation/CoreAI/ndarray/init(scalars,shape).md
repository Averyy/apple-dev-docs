# init(scalars:shape:)

**Framework**: Core AI  
**Kind**: init  
**Role**: Initializer

Initialize an ndArray with a copy of some sequence of scalars, stored in the ndArray in row-major order.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init<Scalar>(scalars: some Sequence, shape: [Int]) where Scalar : BitwiseCopyable
```

#### Discussion

This utility will construct an ndArray with a copy of the contents of some sequence. For example to make an int32 ndArray with increasing values:

```swift
var ndArray = NDArray(scalars: (0..<4) as Range<Int32>, shape: [2, 2])
// The resulting NDArray has contents:
[[0, 1], [2, 3]]
```

## Parameters

- `scalars`: A sequence of scalars to be copied into the new ndArray. Note that `Scalar` must be a type that corresponds to a scalar type found on the [`NDArray.ScalarType`](./scalartype-swift.enum.md) enum.
- `shape`: The shape of the new ndArray. The ndArray will be stored in row-major order and the scalars will be assigned in row-major order.

## See Also

### Creating an array
- [init(shape: [Int], scalarType: NDArray.ScalarType)](./init%28shape,scalartype%29.md)
  Creates an array with the specified shape and scalar type.
- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int])](./init%28shape,scalartype,strides%29.md)
  Creates an array with the specified shape, scalar type, and strides.
- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int], interleaveLayout: NDArray.InterleaveLayout)](./init%28shape,scalartype,strides,interleavelayout%29.md)
  Initialize an NDArray with the provided shape, scalar type, strides, and interleaved dimension.
- [init(descriptor: consuming NDArrayDescriptor)](./init%28descriptor%29.md)
  Creates an array with the shape and preferred strides from the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/init(scalars:shape:))*