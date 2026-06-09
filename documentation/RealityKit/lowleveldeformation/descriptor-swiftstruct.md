# LowLevelDeformation.Descriptor

**Framework**: RealityKit  
**Kind**: struct

An object that describes the per-frame data requirements for a [`LowLevelDeformation`](lowleveldeformation.md).

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

## Topics

### Creating a descriptor
- [init(vertexCount: Int, blending: LowLevelDeformation.Descriptor.Blending?, skinning: LowLevelDeformation.Descriptor.Skinning?, renormalizing: LowLevelDeformation.Descriptor.Renormalizing?)](lowleveldeformation/descriptor-swift.struct/init(vertexcount:blending:skinning:renormalizing:).md)
  Creates a deformation descriptor.
### Specifying the vertex count
- [var vertexCount: Int](lowleveldeformation/descriptor-swift.struct/vertexcount.md)
  The number of vertices in the input and output meshes.
### Configuring blending
- [var blending: LowLevelDeformation.Descriptor.Blending?](lowleveldeformation/descriptor-swift.struct/blending-swift.property.md)
  The blend-shape configuration, or `nil` if blending is not used.
- [LowLevelDeformation.Descriptor.Blending](lowleveldeformation/descriptor-swift.struct/blending-swift.struct.md)
  The blend-shape data dimensions for a [`LowLevelDeformation`](lowleveldeformation.md).
### Configuring skinning
- [var skinning: LowLevelDeformation.Descriptor.Skinning?](lowleveldeformation/descriptor-swift.struct/skinning-swift.property.md)
  The skinning configuration, or `nil` if skinning is not used.
- [LowLevelDeformation.Descriptor.Skinning](lowleveldeformation/descriptor-swift.struct/skinning-swift.struct.md)
  The skinning data dimensions for a [`LowLevelDeformation`](lowleveldeformation.md).
### Configuring renormalizing
- [var renormalizing: LowLevelDeformation.Descriptor.Renormalizing?](lowleveldeformation/descriptor-swift.struct/renormalizing-swift.property.md)
  The renormalization configuration, or `nil` if renormalization is not used.
- [LowLevelDeformation.Descriptor.Renormalizing](lowleveldeformation/descriptor-swift.struct/renormalizing-swift.struct.md)
  The renormalization data dimensions for a [`LowLevelDeformation`](lowleveldeformation.md).

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let descriptor: LowLevelDeformation.Descriptor](lowleveldeformation/descriptor-swift.property.md)
  The descriptor used to create this deformation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/descriptor-swift.struct)*