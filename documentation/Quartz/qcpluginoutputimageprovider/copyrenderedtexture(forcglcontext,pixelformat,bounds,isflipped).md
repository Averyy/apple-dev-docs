# copyRenderedTexture(forCGLContext:pixelFormat:bounds:isFlipped:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Returns the name of an OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that contains a subregion of the image in a given pixel format.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
optional func copyRenderedTexture(forCGLContext cgl_ctx: CGLContextObj!, pixelFormat format: String!, bounds: NSRect, isFlipped flipped: UnsafeMutablePointer<ObjCBool>!) -> GLuint
```

```objc
- (GLuint) copyRenderedTextureForCGLContext:(CGLContextObj) cgl_ctx pixelFormat:(NSString *) format bounds:(NSRect) bounds isFlipped:(BOOL *) flipped;
```

## Return Value

The name of an OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that contains a subregion of the image in a given pixel format or `0` if the texture can’t be provided.

## Discussion

Implement this method if you want to create the texture yourself or use framebuffer objects (FBO). Use `<OpenGL/CGLMacro.h>` to send commands to the OpenGL context. Make sure to preserve all the OpenGL states except the ones defined by `GL_CURRENT_BIT`.

## Parameters

- `cgl_ctx`: The CGL context to render to.
- `format`: A string that represents the pixel format of the texture.
- `bounds`: The bounds of the subregion of the image.
- `flipped`: Set to [`true`](../../Swift/true.md) on output if the contents of the returned texture are vertically flipped.

## See Also

### Rendering an Image to a Destination
- [func render(toBuffer: UnsafeMutableRawPointer!, withBytesPerRow: Int, pixelFormat: String!, forBounds: NSRect) -> Bool](./render%28tobuffer,withbytesperrow,pixelformat,forbounds%29.md)
  Renders a subregion of the image into  the supplied memory buffer using the specified pixel format.
- [func render(withCGLContext: CGLContextObj!, forBounds: NSRect) -> Bool](./render%28withcglcontext,forbounds%29.md)
  Renders a subregion of the image to the provided CGL context.
- [func releaseRenderedTexture(GLuint, forCGLContext: CGLContextObj!)](./releaserenderedtexture%28_,forcglcontext%29.md)
  Releases the previously copied texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/copyrenderedtexture(forcglcontext:pixelformat:bounds:isflipped:))*