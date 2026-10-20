# MLCPaddingType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A padding type that you specify for a padding layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCPaddingType
```

```c
enum MLCPaddingType : int32_t;
```

## Topics

### Enumeration Cases
- [MLCPaddingType.zero](./mlcpaddingtype/zero.md)
- [MLCPaddingType.reflect](./mlcpaddingtype/reflect.md)
- [MLCPaddingType.symmetric](./mlcpaddingtype/symmetric.md)
- [MLCPaddingType.constant](./mlcpaddingtype/constant.md)
- [var debugDescription: String](./mlcpaddingtype/debugdescription.md)
  A textual description of the padding type, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](./mlcpaddingtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Supporting Types
- [enum MLCPaddingPolicy](./mlcpaddingpolicy-3hic8.md)
  A padding policy that you specify for a convolution or pooling layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpaddingtype)*