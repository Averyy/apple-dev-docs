# init(shape:scalarType:)

**Framework**: Core AI  
**Kind**: init

Creates an array with the specified shape and scalar type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(shape: [Int], scalarType: NDArray.ScalarType)
```

#### Discussion

This initializer creates an array with contiguous, row-major strides.

## Parameters

- `shape`: The length of each dimension.
- `scalarType`: The scalar element type.

## See Also

- [init(shape: [Int], scalarType: NDArray.ScalarType, strides: [Int])](ndarray/init(shape:scalartype:strides:).md)
  Creates an array with the specified shape, scalar type, and strides.
- [init(descriptor: consuming NDArrayDescriptor)](ndarray/init(descriptor:).md)
  Creates an array with the shape and preferred strides from the specified descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/ndarray/init(shape:scalartype:))*