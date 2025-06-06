# init(shape:scalars:scalarType:)

**Framework**: Core ML  
**Kind**: init

Creates a tensor with the specified shape and contiguous scalars in row-major order.

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
init<Scalar>(shape: [Int], scalars: some Collection, scalarType: Scalar.Type = Scalar.self) where Scalar : MLTensorScalar
```

## Parameters

- `shape`: The dimensions of the tensor.
- `scalars`: The scalar contents of the tensor. The product of the dimensions of the shape must equal the number of scalars.
- `scalarType`: The scalar type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(shape:scalars:scalartype:))*