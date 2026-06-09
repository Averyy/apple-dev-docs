# LowLevelDeformation.Pipeline.Descriptor

**Framework**: RealityKit  
**Kind**: struct

An object that describes the vertex layouts and deformer stages for a pipeline.

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
- [init(inputAttributes: [LowLevelDeformation.VertexAttribute], outputAttributes: [LowLevelDeformation.VertexAttribute], blending: LowLevelDeformation.Pipeline.Descriptor.Blending?, skinning: LowLevelDeformation.Pipeline.Descriptor.Skinning?, renormalizing: LowLevelDeformation.Pipeline.Descriptor.Renormalizing?)](lowleveldeformation/pipeline/descriptor/init(inputattributes:outputattributes:blending:skinning:renormalizing:).md)
  Creates a pipeline descriptor.
### Specifying vertex attributes
- [var inputAttributes: [LowLevelDeformation.VertexAttribute]](lowleveldeformation/pipeline/descriptor/inputattributes.md)
  The vertex attributes for the input mesh.
- [var outputAttributes: [LowLevelDeformation.VertexAttribute]](lowleveldeformation/pipeline/descriptor/outputattributes.md)
  The vertex attributes for the output mesh.
### Configuring blending
- [var blending: LowLevelDeformation.Pipeline.Descriptor.Blending?](lowleveldeformation/pipeline/descriptor/blending-swift.property.md)
  Blend-shape parameters, or `nil` to omit blending.
- [LowLevelDeformation.Pipeline.Descriptor.Blending](lowleveldeformation/pipeline/descriptor/blending-swift.struct.md)
  The blend-shape configuration for a deformation pipeline.
### Configuring skinning
- [var skinning: LowLevelDeformation.Pipeline.Descriptor.Skinning?](lowleveldeformation/pipeline/descriptor/skinning-swift.property.md)
  Skinning parameters, or `nil` to omit skinning.
- [LowLevelDeformation.Pipeline.Descriptor.Skinning](lowleveldeformation/pipeline/descriptor/skinning-swift.struct.md)
  The skinning stage configuration for a deformation pipeline.
### Configuring renormalizing
- [var renormalizing: LowLevelDeformation.Pipeline.Descriptor.Renormalizing?](lowleveldeformation/pipeline/descriptor/renormalizing-swift.property.md)
  Renormalization parameters, or `nil` to omit renormalization.
- [LowLevelDeformation.Pipeline.Descriptor.Renormalizing](lowleveldeformation/pipeline/descriptor/renormalizing-swift.struct.md)
  An object that describes which vertex attributes to renormalize to unit length after deformation.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor)*