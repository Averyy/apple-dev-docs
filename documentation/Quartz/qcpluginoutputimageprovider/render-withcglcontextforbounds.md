# render(withCGLContext:forBounds:)

**Framework**: Quartz  
**Kind**: method

Renders a subregion of the image to the provided CGL context.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func render(withCGLContext cgl_ctx: CGLContextObj!, forBounds bounds: NSRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if successful; [`false`](https://developer.apple.com/documentation/Swift/false) on failure or if the image provider doesn’t support GPU rendering.

#### Discussion

The view port is set for you. The model view and projection  matrixes are set to the identity.

Your OpenGL code should save and restore all states  for those that are part of `GL_CURRENT_BIT` (vertex position, color, texture, and so on). Also use CGL macros instead of changing the current context, by including this statement:

`#import <OpenGL/CGLMacro.h>`

For more details, see [`Quartz Composer Custom Patch Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer_Patch_PlugIn_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004787).

## Parameters

- `cgl_ctx`: The CGL context to render to.
- `bounds`: The bounds of the subregion.

## See Also

- [func render(toBuffer: UnsafeMutableRawPointer!, withBytesPerRow: Int, pixelFormat: String!, forBounds: NSRect) -> Bool](qcpluginoutputimageprovider/render(tobuffer:withbytesperrow:pixelformat:forbounds:).md)
  Renders a subregion of the image into  the supplied memory buffer using the specified pixel format.
- [func copyRenderedTexture(forCGLContext: CGLContextObj!, pixelFormat: String!, bounds: NSRect, isFlipped: UnsafeMutablePointer<ObjCBool>!) -> GLuint](qcpluginoutputimageprovider/copyrenderedtexture(forcglcontext:pixelformat:bounds:isflipped:).md)
  Returns the name of an OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that contains a subregion of the image in a given pixel format.
- [func releaseRenderedTexture(GLuint, forCGLContext: CGLContextObj!)](qcpluginoutputimageprovider/releaserenderedtexture(_:forcglcontext:).md)
  Releases the previously copied texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/render(withcglcontext:forbounds:))*