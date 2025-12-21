# endEncoding(commandEncoder:)

**Framework**: Compositor Services  
**Kind**: method

Finish encoding the render context.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func endEncoding(commandEncoder command_encoder: any MTL4RenderCommandEncoder)
```

#### Discussion

`endEncoding(commandEncoder:)` passes the ownership of the command encoder to the drawable render context and calls [`endEncoding()`](https://developer.apple.com/documentation/Metal/MTLCommandEncoder/endEncoding()) on the command encoder. The command encoder used in the render context has the following constraints:

- The `colorAttachment[0]` contains the color texture provided by the layer renderer drawable.
- The [`depthAttachment`](https://developer.apple.com/documentation/Metal/MTLRenderPassDescriptor/depthAttachment) contains the depth texture provided by the layer renderer drawable.
- The [`renderTargetArrayLength`](https://developer.apple.com/documentation/Metal/MTLRenderPassDescriptor/renderTargetArrayLength) is the same as the number of views in the layer renderer drawable.
- The [`rasterizationRateMap`](https://developer.apple.com/documentation/Metal/MTLRenderPassDescriptor/rasterizationRateMap) matches the one provided by the layer renderer drawable.
- The API doesn’t support dedicated and shared layouts.

If the render encoder has multiple color attachments, set [`supportColorAttachmentMapping`](https://developer.apple.com/documentation/Metal/MTL4RenderPassDescriptor/supportColorAttachmentMapping) to `true` to avoid Metal API validation errors.

For testing performance of this method, always test your app on-device rather than in Simulator. However, if you need to iterate on your code in development, you can disable API validation in Xcode, or separate the rendering into multiple render encoders for other color attachments.

## See Also

- [func drawMaskOnStencilAttachment(commandEncoder: any MTL4RenderCommandEncoder, value: UInt8)](layerrenderer/drawable/rendercontext/drawmaskonstencilattachment(commandencoder:value:)-7npim.md)
  Store the value parameter in the stencil texture in the pixels that the Compositor displays onscreen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/rendercontext/endencoding(commandencoder:)-2l6lk)*