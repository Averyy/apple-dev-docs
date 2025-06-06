# MLTensor.PaddingMode

**Framework**: Core ML  
**Kind**: enum

A mode that dictates how a tensor is padded.

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
enum PaddingMode
```

## Topics

### Enumeration Cases
- [MLTensor.PaddingMode.constant(_:)](mltensor/paddingmode/constant(_:).md)
  Pads the input tensor boundaries with a constant value.
- [MLTensor.PaddingMode.reflection](mltensor/paddingmode/reflection.md)
  Pads the input tensor using the reflection of the input boundary.
- [MLTensor.PaddingMode.symmetric](mltensor/paddingmode/symmetric.md)
  Pads the input tensor using the reflection of the input, including the edge value.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/paddingmode)*