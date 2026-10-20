# LowLevelRenderPipelineState.Descriptor.Blending

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An alpha blending mode for transparent draw calls.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Blending
```

## Topics

### Creating a blending mode
- [static var sourceOver: LowLevelRenderPipelineState.Descriptor.Blending](./blending-swift.struct/sourceover.md)
  Standard source-over alpha blending with pre-multiplied alpha.
- [static var add: LowLevelRenderPipelineState.Descriptor.Blending](./blending-swift.struct/add.md)
  Additive blending that combines source and destination colors.
### Type Methods
- [static func custom(sourceRGBBlendFactor: MTLBlendFactor, destinationRGBBlendFactor: MTLBlendFactor, rgbBlendOperation: MTLBlendOperation, sourceAlphaBlendFactor: MTLBlendFactor, destinationAlphaBlendFactor: MTLBlendFactor, alphaBlendOperation: MTLBlendOperation) -> LowLevelRenderPipelineState.Descriptor.Blending](./blending-swift.struct/custom%28sourcergbblendfactor,destinationrgbblendfactor,rgbblendoperation,sourcealphablendfactor,destinationalphablendfactor,alphablendoperation%29.md)
  Creates a custom blending configuration with explicit Metal blend factors and operations.

## Relationships

### Conforms To
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring the pipeline
- [var mesh: LowLevelMeshResource.Descriptor?](./mesh.md)
  The vertex format of the mesh this pipeline renders.
- [var renderTargets: LowLevelRenderTarget.DescriptorSet](./rendertargets.md)
  The set of render target descriptors this pipeline state is compatible with.
- [var blending: LowLevelRenderPipelineState.Descriptor.Blending?](./blending-swift.property.md)
  The blending configuration, or `nil` for opaque draws.
- [var writeMask: MTLColorWriteMask](./writemask.md)
  The color channels written to the output attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/blending-swift.struct)*