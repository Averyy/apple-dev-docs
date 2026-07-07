# init(shape:scalarType:strides:interleaveLayout:)

**Framework**: Core AI  
**Kind**: init

Initialize an NDArray with the provided shape, scalar type, strides, and interleaved dimension.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int], interleaveLayout: NDArray.InterleaveLayout)
```

#### Discussion

`shape` and `strides` must have the same number of elements.

## Parameters

- `shape`: The length of each dimension of the ndArray.
- `scalarType`: The type of elements in the ndArray.
- `strides`: The strides of the ndArray.
- `interleaveLayout`: Which dimension is interleaved and by what factor. See [`NDArray.InterleaveLayout`](ndarray/interleavelayout-swift.struct.md).

## See Also

- [init(shape: [Int], scalarType: NDArray.ScalarType)](ndarray/init(shape:scalartype:).md)
  Creates an array with the specified shape and scalar type.
- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int])](ndarray/init(shape:scalartype:strides:).md)
  Creates an array with the specified shape, scalar type, and strides.
- [init<Scalar>(scalars: some Sequence, shape: [Int])](ndarray/init(scalars:shape:).md)
  Initialize an ndArray with a copy of some sequence of scalars, stored in the ndArray in row-major order.
- [init(descriptor: consuming NDArrayDescriptor)](ndarray/init(descriptor:).md)
  Creates an array with the shape and preferred strides from the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/init(shape:scalartype:strides:interleavelayout:))*