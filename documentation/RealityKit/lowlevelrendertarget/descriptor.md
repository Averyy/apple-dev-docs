# LowLevelRenderTarget.Descriptor

**Framework**: RealityKit  
**Kind**: struct

A color and depth pixel format combination for a render pass.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Descriptor
```

#### Overview

Use [`renderTargetDescriptor`](lowlevelrenderer/configuration/rendertargetdescriptor.md) to obtain a descriptor from each renderer configuration you plan to use. Collect one or more descriptors into a [`LowLevelRenderTarget.DescriptorSet`](lowlevelrendertarget/descriptorset.md), then pass the set to [`makeRenderPipelineState(descriptor:)`](lowlevelrendercontext/makerenderpipelinestate(descriptor:).md) and [`makeMeshInstanceArray(renderTargets:count:)`](lowlevelrendercontext/makemeshinstancearray(rendertargets:count:).md).

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [LowLevelRenderTarget.DescriptorSet](lowlevelrendertarget/descriptorset.md)
  An unordered set of render target descriptors that defines the output format combination a pipeline state or mesh instance array is compatible with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendertarget/descriptor)*