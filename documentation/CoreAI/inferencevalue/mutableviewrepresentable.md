# InferenceValue.MutableViewRepresentable

**Framework**: Core AI  
**Kind**: protocol  
**Role**: Protocol

A type that can provide a mutable view of itself as an inference value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
protocol MutableViewRepresentable : ~Copyable
```

## Topics

### Creating a mutable view
- [func mutableView() -> InferenceValue.MutableView](./mutableviewrepresentable/mutableview%28%29.md)

## Relationships

### Conforming Types
- [NDArray](../ndarray.md)

## See Also

### Adopting representable protocols
- [InferenceValue.ViewRepresentable](./viewrepresentable.md)
  A type that can provide a read-only view of itself as an inference value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreai/inferencevalue/mutableviewrepresentable)*