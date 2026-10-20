# writeMask

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The color channels written to the output attachment.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var writeMask: MTLColorWriteMask { get set }
```

#### Discussion

Defaults to `.all`. Set this to a subset of channels to write only specific components.

## See Also

### Configuring the pipeline
- [var mesh: LowLevelMeshResource.Descriptor?](./mesh.md)
  The vertex format of the mesh this pipeline renders.
- [var renderTargets: LowLevelRenderTarget.DescriptorSet](./rendertargets.md)
  The set of render target descriptors this pipeline state is compatible with.
- [var blending: LowLevelRenderPipelineState.Descriptor.Blending?](./blending-swift.property.md)
  The blending configuration, or `nil` for opaque draws.
- [LowLevelRenderPipelineState.Descriptor.Blending](./blending-swift.struct.md)
  An alpha blending mode for transparent draw calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/writemask)*