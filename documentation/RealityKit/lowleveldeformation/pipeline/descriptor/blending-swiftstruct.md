# LowLevelDeformation.Pipeline.Descriptor.Blending

**Framework**: RealityKit  
**Kind**: struct

The blend-shape configuration for a deformation pipeline.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Blending
```

## Topics

### Creating a blending configuration
- [init(blendsNormals: Bool, blendsTangents: Bool, blendsBitangents: Bool)](lowleveldeformation/pipeline/descriptor/blending-swift.struct/init(blendsnormals:blendstangents:blendsbitangents:).md)
  Creates a blending descriptor.
### Configuring blended attributes
- [var blendsNormals: Bool](lowleveldeformation/pipeline/descriptor/blending-swift.struct/blendsnormals.md)
  A Boolean value that indicates whether the pipeline blends normal offsets.
- [var blendsTangents: Bool](lowleveldeformation/pipeline/descriptor/blending-swift.struct/blendstangents.md)
  A Boolean value that indicates whether the pipeline blends tangent offsets.
- [var blendsBitangents: Bool](lowleveldeformation/pipeline/descriptor/blending-swift.struct/blendsbitangents.md)
  A Boolean value that indicates whether the pipeline recomputes bitangents from blended normals and tangents.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var blending: LowLevelDeformation.Pipeline.Descriptor.Blending?](lowleveldeformation/pipeline/descriptor/blending-swift.property.md)
  Blend-shape parameters, or `nil` to omit blending.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/blending-swift.struct)*