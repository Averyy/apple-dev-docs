# InferenceValue.ViewRepresentable

**Framework**: Core AI  
**Kind**: protocol

A type that can provide a read-only view of itself as an inference value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
protocol ViewRepresentable : ~Copyable
```

## Topics

### Creating a view
- [func view() -> InferenceValue.View](inferencevalue/viewrepresentable/view.md)

## Relationships

### Conforming Types
- [NDArray](ndarray.md)

## See Also

- [InferenceValue.MutableViewRepresentable](inferencevalue/mutableviewrepresentable.md)
  A type that can provide a mutable view of itself as an inference value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/viewrepresentable)*