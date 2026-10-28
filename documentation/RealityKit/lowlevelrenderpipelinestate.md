# LowLevelRenderPipelineState

**Framework**: RealityKit  
**Kind**: class  
**Role**: Class

A compiled Metal render pipeline state for a specific mesh descriptor, material, and render target configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final class LowLevelRenderPipelineState
```

## Overview

The mesh descriptor, material, render target descriptors, and blending are specified via the descriptor and cannot be changed after the pipeline state is created.

Create a `LowLevelRenderPipelineState` using [`makeRenderPipelineState(descriptor:)`](./lowlevelrendercontext/makerenderpipelinestate%28descriptor%29.md).

## Topics

### Creating a pipeline state
- [LowLevelRenderPipelineState.Descriptor](./lowlevelrenderpipelinestate/descriptor.md)
  The inputs required to compile a render pipeline state.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Pipeline and render targets
- [class LowLevelRenderTarget](./lowlevelrendertarget.md)
  An object that describes the pixel format configuration for a render pass’s color and depth attachments.
- [class LowLevelArgumentTable](./lowlevelargumenttable.md)
  A table of buffer slices and textures bound to a single shader function.
- [struct LowLevelMaterialParameterMapping](./lowlevelmaterialparametermapping.md)
  A mapping of named buffer and texture parameters to binding indices for a compiled shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderpipelinestate)*