# LowLevelDeformation.Descriptor

**Framework**: RealityKit  
**Kind**: struct

An object that describes the per-frame data requirements for a [`LowLevelDeformation`](lowleveldeformation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

## Topics

### Specifying the vertex count
- [var vertexCount: Int](lowleveldeformation/descriptor-swift.struct/vertexcount.md)
  The number of vertices in the input and output meshes.
### Configuring skinning
- [var skinning: LowLevelDeformation.Descriptor.Skinning?](lowleveldeformation/descriptor-swift.struct/skinning-swift.property.md)
  The skinning configuration, or `nil` if skinning is not used.
- [LowLevelDeformation.Descriptor.Skinning](lowleveldeformation/descriptor-swift.struct/skinning-swift.struct.md)
  The skinning data dimensions for a [`LowLevelDeformation`](lowleveldeformation.md).
### Structures
- [LowLevelDeformation.Descriptor.BlendShape](lowleveldeformation/descriptor-swift.struct/blendshape-swift.struct.md)
  The blend-shape data dimensions for a [`LowLevelDeformation`](lowleveldeformation.md).
- [LowLevelDeformation.Descriptor.Renormalization](lowleveldeformation/descriptor-swift.struct/renormalization-swift.struct.md)
  The renormalization data dimensions for a [`LowLevelDeformation`](lowleveldeformation.md).
### Initializers
- [init(vertexCount: Int, blendShape: LowLevelDeformation.Descriptor.BlendShape?, skinning: LowLevelDeformation.Descriptor.Skinning?, renormalization: LowLevelDeformation.Descriptor.Renormalization?)](lowleveldeformation/descriptor-swift.struct/init(vertexcount:blendshape:skinning:renormalization:).md)
  Creates a deformation descriptor.
### Instance Properties
- [var blendShape: LowLevelDeformation.Descriptor.BlendShape?](lowleveldeformation/descriptor-swift.struct/blendshape-swift.property.md)
  The blend-shape configuration, or `nil` if blend-shape deformation is not used.
- [var renormalization: LowLevelDeformation.Descriptor.Renormalization?](lowleveldeformation/descriptor-swift.struct/renormalization-swift.property.md)
  The renormalization configuration, or `nil` if renormalization is not used.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let descriptor: LowLevelDeformation.Descriptor](lowleveldeformation/descriptor-swift.property.md)
  The descriptor used to create this deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/descriptor-swift.struct)*