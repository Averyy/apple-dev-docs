# MTLTensorPlaneType

**Framework**: Metal  
**Kind**: enum  
**Role**: Enumeration

The possible tensor plane types.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum MTLTensorPlaneType
```

```c
enum MTLTensorPlaneType : NSInteger;
```

## Topics

### Enumeration Cases
- [MTLTensorPlaneType.data](./mtltensorplanetype/data.md)
  The main data plane, which every tensor has
- [MTLTensorPlaneType.scales](./mtltensorplanetype/scales.md)
  The auxiliary plane that stores scale factors for elements in the data plane.
### Initializers
- [init?(rawValue: Int)](./mtltensorplanetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorplanetype)*