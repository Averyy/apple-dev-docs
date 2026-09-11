# mesh

**Framework**: RealityKit  
**Kind**: property

The vertex format of the mesh this pipeline renders.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var mesh: LowLevelMeshResource.Descriptor? { get set }
```

## See Also

- [var renderTargets: LowLevelRenderTarget.DescriptorSet](lowlevelrenderpipelinestate/descriptor/rendertargets.md)
  The set of render target descriptors this pipeline state is compatible with.
- [var blending: LowLevelRenderPipelineState.Descriptor.Blending?](lowlevelrenderpipelinestate/descriptor/blending-swift.property.md)
  The blending configuration, or `nil` for opaque draws.
- [LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct.md)
  An alpha blending mode for transparent draw calls.
- [var writeMask: MTLColorWriteMask](lowlevelrenderpipelinestate/descriptor/writemask.md)
  The color channels written to the output attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/mesh)*