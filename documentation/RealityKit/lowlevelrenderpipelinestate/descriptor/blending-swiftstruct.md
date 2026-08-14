# LowLevelRenderPipelineState.Descriptor.Blending

**Framework**: RealityKit  
**Kind**: struct

An alpha blending mode for transparent draw calls.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Blending
```

## Topics

### Creating a blending mode
- [static var sourceOver: LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/sourceover.md)
  Standard source-over alpha blending with pre-multiplied alpha.
- [static var add: LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/add.md)
  Additive blending that combines source and destination colors.
### Type Methods
- [static func custom(sourceRGBBlendFactor: MTLBlendFactor, destinationRGBBlendFactor: MTLBlendFactor, rgbBlendOperation: MTLBlendOperation, sourceAlphaBlendFactor: MTLBlendFactor, destinationAlphaBlendFactor: MTLBlendFactor, alphaBlendOperation: MTLBlendOperation) -> LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct/custom(sourcergbblendfactor:destinationrgbblendfactor:rgbblendoperation:sourcealphablendfactor:destinationalphablendfactor:alphablendoperation:).md)
  Creates a custom blending configuration with explicit Metal blend factors and operations.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var mesh: LowLevelMeshResource.Descriptor?](lowlevelrenderpipelinestate/descriptor/mesh.md)
  The vertex format of the mesh this pipeline renders.
- [var renderTargets: LowLevelRenderTarget.DescriptorSet](lowlevelrenderpipelinestate/descriptor/rendertargets.md)
  The set of render target descriptors this pipeline state is compatible with.
- [var blending: LowLevelRenderPipelineState.Descriptor.Blending?](lowlevelrenderpipelinestate/descriptor/blending-swift.property.md)
  The blending configuration, or `nil` for opaque draws.
- [var writeMask: MTLColorWriteMask](lowlevelrenderpipelinestate/descriptor/writemask.md)
  The color channels written to the output attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/blending-swift.struct)*