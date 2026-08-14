# LowLevelRenderPipelineState.Descriptor

**Framework**: RealityKit  
**Kind**: struct

The inputs required to compile a render pipeline state.

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

### Creating a descriptor
- [init(mesh: LowLevelMeshResource.Descriptor, material: LowLevelMaterialResource, renderTargets: LowLevelRenderTarget.DescriptorSet, blending: LowLevelRenderPipelineState.Descriptor.Blending?)](lowlevelrenderpipelinestate/descriptor/init(mesh:material:rendertargets:blending:).md)
  Creates a descriptor for the given mesh format, material, render targets, and optional blending configuration.
### Configuring the pipeline
- [var mesh: LowLevelMeshResource.Descriptor?](lowlevelrenderpipelinestate/descriptor/mesh.md)
  The vertex format of the mesh this pipeline renders.
- [var renderTargets: LowLevelRenderTarget.DescriptorSet](lowlevelrenderpipelinestate/descriptor/rendertargets.md)
  The set of render target descriptors this pipeline state is compatible with.
- [var blending: LowLevelRenderPipelineState.Descriptor.Blending?](lowlevelrenderpipelinestate/descriptor/blending-swift.property.md)
  The blending configuration, or `nil` for opaque draws.
- [LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct.md)
  An alpha blending mode for transparent draw calls.
- [var writeMask: MTLColorWriteMask](lowlevelrenderpipelinestate/descriptor/writemask.md)
  The color channels written to the output attachment.
### Instance Properties
- [var material: LowLevelMaterialResource](lowlevelrenderpipelinestate/descriptor/material.md)
  The compiled material for this pipeline state.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor)*