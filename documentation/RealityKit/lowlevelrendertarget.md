# LowLevelRenderTarget

**Framework**: RealityKit  
**Kind**: class

An object that describes the pixel format configuration for a render pass’s color and depth attachments.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelRenderTarget
```

#### Overview

`LowLevelRenderTarget.Descriptor` is analogous to `MTLRenderPassDescriptor`’s attachment descriptors — it specifies the `MTLPixelFormat` for color and depth targets, and the MSAA sample count. Build a [`LowLevelRenderTarget.DescriptorSet`](lowlevelrendertarget/descriptorset.md) from one or more descriptors and provide it when creating a `LowLevelRenderPipelineState` and a `LowLevelMeshInstanceArray`.

## Topics

### Describing the render target
- [LowLevelRenderTarget.Descriptor](lowlevelrendertarget/descriptor.md)
  A color and depth pixel format combination for a render pass.
- [LowLevelRenderTarget.DescriptorSet](lowlevelrendertarget/descriptorset.md)
  An unordered set of render target descriptors that defines the output format combination a pipeline state or mesh instance array is compatible with.

## See Also

- [class LowLevelRenderPipelineState](lowlevelrenderpipelinestate.md)
  A compiled Metal render pipeline state for a specific mesh descriptor, material, and render target configuration.
- [class LowLevelArgumentTable](lowlevelargumenttable.md)
  A table of buffer slices and textures bound to a single shader function stage.
- [struct LowLevelMaterialParameterMapping](lowlevelmaterialparametermapping.md)
  A mapping of named buffer and texture parameters to binding indices for a compiled shader function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendertarget)*