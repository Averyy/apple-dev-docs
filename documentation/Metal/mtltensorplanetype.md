# MTLTensorPlaneType

**Framework**: Metal  
**Kind**: enum

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

## Topics

### Enumeration Cases
- [MTLTensorPlaneType.data](mtltensorplanetype/data.md)
  The main data plane, which every tensor has
- [MTLTensorPlaneType.scales](mtltensorplanetype/scales.md)
  The auxiliary plane that stores scale factors for elements in the data plane.
### Initializers
- [init?(rawValue: Int)](mtltensorplanetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensorplanetype)*