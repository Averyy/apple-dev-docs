# MPSGraphPaddingStyle

**Framework**: Metal Performance Shaders Graph  
**Kind**: enum  
**Role**: Enumeration

The tensor padding style.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum MPSGraphPaddingStyle
```

```c
enum MPSGraphPaddingStyle : NSUInteger;
```

## Topics

### Enumeration Cases
- [MPSGraphPaddingStyle.ONNX_SAME_LOWER](./mpsgraphpaddingstyle/onnx_same_lower.md)
  Explicit offsets
- [MPSGraphPaddingStyle.TF_SAME](./mpsgraphpaddingstyle/tf_same.md)
  TF_SAME
- [MPSGraphPaddingStyle.TF_VALID](./mpsgraphpaddingstyle/tf_valid.md)
  ONNX_SAME_LOWER
- [MPSGraphPaddingStyle.explicit](./mpsgraphpaddingstyle/explicit.md)
  Explicit
- [MPSGraphPaddingStyle.explicitOffset](./mpsgraphpaddingstyle/explicitoffset.md)
  TF_VALID
### Initializers
- [init?(rawValue: UInt)](./mpsgraphpaddingstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphpaddingstyle)*