# init(_:scalarType:)

**Framework**: Core ML  
**Kind**: init

Creates a zero-dimensional tensor from a scalar value.

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
init<Scalar>(_ value: Scalar, scalarType: Scalar.Type = Scalar.self) where Scalar : MLTensorScalar
```

## Parameters

- `value`: The value.
- `scalarType`: The scalar type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(_:scalartype:)-3f5yt)*