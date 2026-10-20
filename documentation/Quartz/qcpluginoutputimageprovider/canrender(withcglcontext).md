# canRender(withCGLContext:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns whether the image data can be rendered into the provided CGL context.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
optional func canRender(withCGLContext cgl_ctx: CGLContextObj!) -> Bool
```

```objc
- (BOOL) canRenderWithCGLContext:(CGLContextObj) cgl_ctx;
```

#### Return Value

[`true`](../../Swift/true.md) if the image can be rendered into this CGL context; otherwise [`false`](../../Swift/false.md), in which case [`render(toBuffer:withBytesPerRow:pixelFormat:forBounds:)`](./render%28tobuffer,withbytesperrow,pixelformat,forbounds%29.md) is called.

#### Discussion

If your image can render using any OpenGL context, simply return [`true`](../../Swift/true.md). If your code requires special extensions, you’ll need to check for them and then provide the appropriate return value. For more information on checking for OpenGL capabilities supported by the hardware, see [OpenGL Programming Guide for Mac](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_intro/opengl_intro.html#//apple_ref/doc/uid/TP40001987).

## Parameters

- `cgl_ctx`: The CGL context that your image will be rendered to.

## See Also

### Providing Information About the Rendering Destination
- [func supportedBufferPixelFormats() -> [Any]!](./supportedbufferpixelformats%28%29.md)
  Returns a list of pixel formats that are supported for rendering to a memory buffer.
- [func supportedRenderedTexturePixelFormats() -> [Any]!](./supportedrenderedtexturepixelformats%28%29.md)
  Returns a list of pixel formats that are supported for rendering to an onscreen OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/canrender(withcglcontext:))*