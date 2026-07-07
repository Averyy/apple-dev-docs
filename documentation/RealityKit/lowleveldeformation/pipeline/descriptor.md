# LowLevelDeformation.Pipeline.Descriptor

**Framework**: RealityKit  
**Kind**: struct

An object that describes the vertex layouts and deformer stages for a pipeline.

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

### Specifying vertex attributes
- [var inputAttributes: [LowLevelDeformation.VertexAttribute]](lowleveldeformation/pipeline/descriptor/inputattributes.md)
  The vertex attributes for the input mesh.
- [var outputAttributes: [LowLevelDeformation.VertexAttribute]](lowleveldeformation/pipeline/descriptor/outputattributes.md)
  The vertex attributes for the output mesh.
### Configuring skinning
- [var skinning: LowLevelDeformation.Pipeline.Descriptor.Skinning?](lowleveldeformation/pipeline/descriptor/skinning-swift.property.md)
  Skinning parameters, or `nil` to omit skinning.
- [LowLevelDeformation.Pipeline.Descriptor.Skinning](lowleveldeformation/pipeline/descriptor/skinning-swift.struct.md)
  The skinning stage configuration for a deformation pipeline.
### Structures
- [LowLevelDeformation.Pipeline.Descriptor.BlendShape](lowleveldeformation/pipeline/descriptor/blendshape-swift.struct.md)
  The blend-shape configuration for a deformation pipeline.
- [LowLevelDeformation.Pipeline.Descriptor.Renormalization](lowleveldeformation/pipeline/descriptor/renormalization-swift.struct.md)
  An object that describes which vertex attributes to renormalize to unit length after deformation.
### Initializers
- [init(inputAttributes: [LowLevelDeformation.VertexAttribute], outputAttributes: [LowLevelDeformation.VertexAttribute], blendShape: LowLevelDeformation.Pipeline.Descriptor.BlendShape?, skinning: LowLevelDeformation.Pipeline.Descriptor.Skinning?, renormalization: LowLevelDeformation.Pipeline.Descriptor.Renormalization?)](lowleveldeformation/pipeline/descriptor/init(inputattributes:outputattributes:blendshape:skinning:renormalization:).md)
  Creates a pipeline descriptor.
### Instance Properties
- [var blendShape: LowLevelDeformation.Pipeline.Descriptor.BlendShape?](lowleveldeformation/pipeline/descriptor/blendshape-swift.property.md)
  Blend-shape parameters, or `nil` to omit blend-shape deformation.
- [var renormalization: LowLevelDeformation.Pipeline.Descriptor.Renormalization?](lowleveldeformation/pipeline/descriptor/renormalization-swift.property.md)
  Renormalization parameters, or `nil` to omit renormalization.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor)*