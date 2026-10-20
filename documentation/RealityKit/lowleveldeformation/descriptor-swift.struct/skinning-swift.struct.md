# LowLevelDeformation.Descriptor.Skinning

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The skinning data dimensions for a [`LowLevelDeformation`](../../lowleveldeformation.md).

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Skinning
```

## Topics

### Creating a skinning descriptor
- [init(jointTransformCount: Int, influencesPerVertex: Int)](./skinning-swift.struct/init%28jointtransformcount,influencespervertex%29.md)
  Creates a skinning descriptor.
### Configuring skinning parameters
- [var jointTransformCount: Int](./skinning-swift.struct/jointtransformcount.md)
  The number of joint transforms.
- [var influencesPerVertex: Int](./skinning-swift.struct/influencespervertex.md)
  The number of joint influences per vertex.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring skinning
- [var skinning: LowLevelDeformation.Descriptor.Skinning?](./skinning-swift.property.md)
  The skinning configuration, or `nil` if skinning is not used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/descriptor-swift.struct/skinning-swift.struct)*