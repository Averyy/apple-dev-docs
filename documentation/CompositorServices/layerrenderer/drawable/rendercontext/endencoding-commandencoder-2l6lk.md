# endEncoding(commandEncoder:)

**Framework**: Compositor Services  
**Kind**: method

Finish encoding the render context.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func endEncoding(commandEncoder command_encoder: any MTL4RenderCommandEncoder)
```

#### Discussion

> **Note**: The ownership of the command encoder is passed to the drawable render context, which will call endEncoding on the command encoder.

> **Note**: The command encoder used in the render context has the following constraints: - color texture: colorAttachment[0] should contain the color texture provided by the drawable.
- depth texture: depthAttachment should contain the depth texture provided by the drawable.
- renderTargetArrayLength: should be the same as the number of views in the drawable.
- rasterizationRateMap: should be the one provided by the drawable.
- layer renderer layout: Dedicated and Shared layout is not supported.
- supportColorAttachmentMapping: The render pass descriptor used to create the render encoder should have `supportColorAttachmentMapping` set to true.

## Parameters

- `command_encoder`: The command encoder to use to render the Compositor effects   and present the drawable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/rendercontext/endencoding(commandencoder:)-2l6lk)*