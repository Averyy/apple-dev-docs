# writeMask

**Framework**: RealityKit  
**Kind**: property

The color channels written to the output attachment.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var writeMask: MTLColorWriteMask { get set }
```

#### Discussion

Defaults to `.all`. Set this to a subset of channels to write only specific components.

## See Also

- [var mesh: LowLevelMeshResource.Descriptor?](lowlevelrenderpipelinestate/descriptor/mesh.md)
  The vertex format of the mesh this pipeline renders.
- [var renderTargets: LowLevelRenderTarget.DescriptorSet](lowlevelrenderpipelinestate/descriptor/rendertargets.md)
  The set of render target descriptors this pipeline state is compatible with.
- [var blending: LowLevelRenderPipelineState.Descriptor.Blending?](lowlevelrenderpipelinestate/descriptor/blending-swift.property.md)
  The blending configuration, or `nil` for opaque draws.
- [LowLevelRenderPipelineState.Descriptor.Blending](lowlevelrenderpipelinestate/descriptor/blending-swift.struct.md)
  An alpha blending mode for transparent draw calls.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate/descriptor/writemask)*