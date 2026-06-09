# MTLTensorPlaneType

**Framework**: Metal  
**Kind**: enum

The possible tensor plane types.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
enum MTLTensorPlaneType
```

## Topics

### Enumeration Cases
- [MTLTensorPlaneType.data](mtltensorplanetype/data.md)
  The data plane. This is the main plane of a tensor. Tensors always have a data plane.
- [MTLTensorPlaneType.scales](mtltensorplanetype/scales.md)
  The scale auxiliary plane. Contains scale factors for elements in the data plane.
### Initializers
- [init?(rawValue: Int)](mtltensorplanetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorplanetype)*