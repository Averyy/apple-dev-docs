# renderTargets

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The set of render target descriptors this pipeline state is compatible with.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var renderTargets: LowLevelRenderTarget.DescriptorSet { get set }
```

## See Also

### Configuring the pipeline
- [var mesh: LowLevelMeshResource.Descriptor?](./mesh.md)
  The vertex format of the mesh this pipeline renders.
- [var blending: LowLevelRenderPipelineState.Descriptor.Blending?](./blending-swift.property.md)
  The blending configuration, or `nil` for opaque draws.
- [LowLevelRenderPipelineState.Descriptor.Blending](./blending-swift.struct.md)
  An alpha blending mode for transparent draw calls.
- [var writeMask: MTLColorWriteMask](./writemask.md)
  The color channels written to the output attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/rendertargets)*