# LowLevelRenderTarget.Descriptor

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

A color and depth pixel format combination for a render pass.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Descriptor
```

## Overview

Use [`renderTargetDescriptor`](../lowlevelrenderer/configuration/rendertargetdescriptor.md) to obtain a descriptor from each renderer configuration you plan to use. Collect one or more descriptors into a [`LowLevelRenderTarget.DescriptorSet`](./descriptorset.md), then pass the set to [`makeRenderPipelineState(descriptor:)`](../lowlevelrendercontext/makerenderpipelinestate%28descriptor%29.md) and [`makeMeshInstanceArray(renderTargets:count:)`](../lowlevelrendercontext/makemeshinstancearray%28rendertargets,count%29.md).

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Describing the render target
- [LowLevelRenderTarget.DescriptorSet](./descriptorset.md)
  An unordered set of render target descriptors that defines the output format combination a pipeline state or mesh instance array is compatible with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendertarget/descriptor)*