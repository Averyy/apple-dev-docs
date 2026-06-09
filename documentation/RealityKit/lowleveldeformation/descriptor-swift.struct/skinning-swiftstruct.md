# LowLevelDeformation.Descriptor.Skinning

**Framework**: RealityKit  
**Kind**: struct

The skinning data dimensions for a [`LowLevelDeformation`](lowleveldeformation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Skinning
```

## Topics

### Creating a skinning descriptor
- [init(jointTransformCount: Int, influencesPerVertex: Int)](lowleveldeformation/descriptor-swift.struct/skinning-swift.struct/init(jointtransformcount:influencespervertex:).md)
  Creates a skinning descriptor.
### Configuring skinning parameters
- [var jointTransformCount: Int](lowleveldeformation/descriptor-swift.struct/skinning-swift.struct/jointtransformcount.md)
  The number of joint transforms.
- [var influencesPerVertex: Int](lowleveldeformation/descriptor-swift.struct/skinning-swift.struct/influencespervertex.md)
  The number of joint influences per vertex.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var skinning: LowLevelDeformation.Descriptor.Skinning?](lowleveldeformation/descriptor-swift.struct/skinning-swift.property.md)
  The skinning configuration, or `nil` if skinning is not used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/descriptor-swift.struct/skinning-swift.struct)*