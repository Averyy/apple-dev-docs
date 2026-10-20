# BNNS.DescriptorType

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the input and output types of an arithmetic operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
enum DescriptorType
```

## Topics

### Descriptor Types
- [BNNS.DescriptorType.constant](./descriptortype/constant.md)
  A constant that doesn’t have a gradient.
- [BNNS.DescriptorType.parameter](./descriptortype/parameter.md)
  A parameter that’s trainable, such as weights or bias.
- [BNNS.DescriptorType.sample](./descriptortype/sample.md)
  A sample such as input or output.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/descriptortype)*