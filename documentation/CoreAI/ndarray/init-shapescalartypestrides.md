# init(shape:scalarType:strides:)

**Framework**: Core AI  
**Kind**: init

Creates an array with the specified shape, scalar type, and strides.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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

- [init(shape: [Int], scalarType: NDArray.ScalarType)](ndarray/init(shape:scalartype:).md)
  Creates an array with the specified shape and scalar type.
- [init(descriptor: consuming NDArrayDescriptor)](ndarray/init(descriptor:).md)
  Creates an array with the shape and preferred strides from the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/init(shape:scalartype:strides:))*