# LowLevelRenderer.RenderState

**Framework**: RealityKit  
**Kind**: struct

The per-frame render state passed to the `render(using:_:)` callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct RenderState
```

#### Overview

`RenderState` is non-copyable and non-escapable; it is only valid for the duration of the `render(using:_:)` callback. Use its methods to encode individual draw calls, or access `encoder` to issue custom Metal commands between draws.

## Topics

### Accessing the encoder
- [var encoder: any MTLRenderCommandEncoder](lowlevelrenderer/renderstate/encoder.md)
  The underlying Metal render command encoder for this render pass.
### Rendering mesh instances
- [func render(meshInstancesArrayIndex: Int, meshInstanceIndex: Int)](lowlevelrenderer/renderstate/render(meshinstancesarrayindex:meshinstanceindex:).md)
  Encodes a draw call for a single mesh instance.
- [func render(meshInstancesArrayIndex: Int, range: Range<Int>)](lowlevelrenderer/renderstate/render(meshinstancesarrayindex:range:).md)
  Encodes draw calls for a contiguous range of mesh instances.
- [func reset()](lowlevelrenderer/renderstate/reset.md)
  Resets the render encoder state to renderer defaults.

## See Also

- [func render(using: any MTLCommandBuffer, (inout LowLevelRenderer.RenderState) -> ())](lowlevelrenderer/render(using:_:).md)
  Encodes draw calls for the frame into the given command buffer using a caller-controlled render callback.
- [LowLevelRenderer.Resources](lowlevelrenderer/resources.md)
  Prepared GPU resources for a renderer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrenderer/renderstate)*