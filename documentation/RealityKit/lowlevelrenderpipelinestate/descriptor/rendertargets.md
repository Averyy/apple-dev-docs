# renderTargets

**Framework**: RealityKit  
**Kind**: property

The set of render target descriptors this pipeline state is compatible with.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var renderTargets: LowLevelRenderTarget.DescriptorSet { get set }
```

## See Also

- [var mesh: LowLevelMeshResource.Descriptor?](lowlevelrenderpipelinestate/descriptor/mesh.md)
  The vertex format of the mesh this pipeline renders.
- [var blending: LowLevelRenderPipelineState.Descriptor.Blending?](lowlevelrenderpipelinestate/descriptor/blending-swift.property.md)
  The blending configuration, or `nil` for opaque draws.
- [LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct.md)
  An alpha blending mode for transparent draw calls.
- [var writeMask: MTLColorWriteMask](lowlevelrenderpipelinestate/descriptor/writemask.md)
  The color channels written to the output attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/rendertargets)*