# render(withCGLContext:forBounds:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Renders a subregion of the image to the provided CGL context.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
optional func render(withCGLContext cgl_ctx: CGLContextObj!, forBounds bounds: NSRect) -> Bool
```

```objc
- (BOOL) renderWithCGLContext:(CGLContextObj) cgl_ctx forBounds:(NSRect) bounds;
```

#### Return Value

[`true`](../../Swift/true.md) if successful; [`false`](../../Swift/false.md) on failure or if the image provider doesn’t support GPU rendering.

#### Discussion

The view port is set for you. The model view and projection  matrixes are set to the identity.

Your OpenGL code should save and restore all states *except* for those that are part of `GL_CURRENT_BIT` (vertex position, color, texture, and so on). Also use CGL macros instead of changing the current context, by including this statement:

`#import <OpenGL/CGLMacro.h>`

For more details, see [Quartz Composer Custom Patch Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer_Patch_PlugIn_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004787).

## Parameters

- `cgl_ctx`: The CGL context to render to.
- `bounds`: The bounds of the subregion.

## See Also

### Rendering an Image to a Destination
- [func render(toBuffer: UnsafeMutableRawPointer!, withBytesPerRow: Int, pixelFormat: String!, forBounds: NSRect) -> Bool](./render%28tobuffer,withbytesperrow,pixelformat,forbounds%29.md)
  Renders a subregion of the image into  the supplied memory buffer using the specified pixel format.
- [func copyRenderedTexture(forCGLContext: CGLContextObj!, pixelFormat: String!, bounds: NSRect, isFlipped: UnsafeMutablePointer<ObjCBool>!) -> GLuint](./copyrenderedtexture%28forcglcontext,pixelformat,bounds,isflipped%29.md)
  Returns the name of an OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that contains a subregion of the image in a given pixel format.
- [func releaseRenderedTexture(GLuint, forCGLContext: CGLContextObj!)](./releaserenderedtexture%28_,forcglcontext%29.md)
  Releases the previously copied texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/render(withcglcontext:forbounds:))*