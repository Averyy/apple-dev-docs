# canRender(withCGLContext:)

**Framework**: Quartz  
**Kind**: method

Returns whether the image data can be rendered into the provided CGL context.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func canRender(withCGLContext cgl_ctx: CGLContextObj!) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the image can be rendered into this CGL context; otherwise [`false`](https://developer.apple.com/documentation/swift/false), in which case [`render(toBuffer:withBytesPerRow:pixelFormat:forBounds:)`](qcpluginoutputimageprovider/render(tobuffer:withbytesperrow:pixelformat:forbounds:).md) is called.

#### Discussion

If your image can render using any OpenGL context, simply return [`true`](https://developer.apple.com/documentation/swift/true). If your code requires special extensions, you’ll need to check for them and then provide the appropriate return value. For more information on checking for OpenGL capabilities supported by the hardware, see [`OpenGL Programming Guide for Mac`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_intro/opengl_intro.html#//apple_ref/doc/uid/TP40001987).

## Parameters

- `cgl_ctx`: The CGL context that your image will be rendered to.

## See Also

- [func supportedBufferPixelFormats() -> [Any]!](qcpluginoutputimageprovider/supportedbufferpixelformats.md)
  Returns a list of pixel formats that are supported for rendering to a memory buffer.
- [func supportedRenderedTexturePixelFormats() -> [Any]!](qcpluginoutputimageprovider/supportedrenderedtexturepixelformats.md)
  Returns a list of pixel formats that are supported for rendering to an onscreen OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/canrender(withcglcontext:))*