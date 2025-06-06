# init(_:scalarType:)

**Framework**: Core ML  
**Kind**: init

Creates a one-dimensional tensor from scalars.

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
init<Scalar>(_ scalars: some Collection, scalarType: Scalar.Type = Scalar.self) where Scalar : MLTensorScalar
```

## Parameters

- `scalars`: A collection of scalars.
- `scalarType`: The scalar type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/init(_:scalartype:)-3qoyj)*