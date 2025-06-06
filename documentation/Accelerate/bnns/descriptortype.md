# BNNS.DescriptorType

**Framework**: Accelerate  
**Kind**: enum

Constants that describe the input and output types of an arithmetic operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
enum DescriptorType
```

## Topics

### Descriptor Types
- [BNNS.DescriptorType.constant](bnns/descriptortype/constant.md)
  A constant that doesn’t have a gradient.
- [BNNS.DescriptorType.parameter](bnns/descriptortype/parameter.md)
  A parameter that’s trainable, such as weights or bias.
- [BNNS.DescriptorType.sample](bnns/descriptortype/sample.md)
  A sample such as input or output.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/descriptortype)*