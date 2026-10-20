# MLTensor.PaddingMode

**Framework**: Core ML  
**Kind**: enum  
**Role**: Enumeration

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

### Padding modes
- [MLTensor.PaddingMode.constant(_:)](./paddingmode/constant%28_%29.md)
  Pads the input tensor boundaries with a constant value.
- [MLTensor.PaddingMode.reflection](./paddingmode/reflection.md)
  Pads the input tensor using the reflection of the input boundary.
- [MLTensor.PaddingMode.symmetric](./paddingmode/symmetric.md)
  Pads the input tensor using the reflection of the input, including the edge value.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Padding the tensor
- [func padded(forSizes: [(before: Int, after: Int)], mode: MLTensor.PaddingMode) -> MLTensor](./padded%28forsizes,mode%29.md)
  Returns a padded tensor according to the specified padding sizes and mode.
- [func padded(forSizes: [(before: Int, after: Int)], with: Float) -> MLTensor](./padded%28forsizes,with%29.md)
  Returns a tensor padded with the given constant according to the specified padding sizes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mltensor/paddingmode)*