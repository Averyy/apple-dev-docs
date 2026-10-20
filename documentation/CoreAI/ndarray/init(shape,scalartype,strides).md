# init(shape:scalarType:strides:)

**Framework**: Core AI  
**Kind**: init  
**Role**: Initializer

Creates an array with the specified shape, scalar type, and strides.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int])
```

#### Discussion

The `shape` and `strides` arrays must have the same number of elements.

## Parameters

- `shape`: The length of each dimension.
- `scalarType`: The scalar element type.
- `strides`: The distance, in elements, between consecutive values along each dimension.

## See Also

### Creating an array
- [init(shape: [Int], scalarType: NDArray.ScalarType)](./init%28shape,scalartype%29.md)
  Creates an array with the specified shape and scalar type.
- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int], interleaveLayout: NDArray.InterleaveLayout)](./init%28shape,scalartype,strides,interleavelayout%29.md)
  Initialize an NDArray with the provided shape, scalar type, strides, and interleaved dimension.
- [init<Scalar>(scalars: some Sequence, shape: [Int])](./init%28scalars,shape%29.md)
  Initialize an ndArray with a copy of some sequence of scalars, stored in the ndArray in row-major order.
- [init(descriptor: consuming NDArrayDescriptor)](./init%28descriptor%29.md)
  Creates an array with the shape and preferred strides from the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/init(shape:scalartype:strides:))*