# releaseRenderedTexture(_:forCGLContext:)

**Framework**: Quartz  
**Kind**: method

Releases the previously copied texture.

**Availability**:
- macOS 10.5+

## Declaration

```swift
optional func releaseRenderedTexture(_ name: GLuint, forCGLContext cgl_ctx: CGLContextObj!)
```

#### Discussion

Your OpenGL code should save and restore all states  for those that are part of `GL_CURRENT_BIT` (vertex position, color, texture, and so on). Also use CGL macros instead of changing the current context, by including this statement:

`#import <OpenGL/CGLMacro.h>`

For more details, see [`Quartz Composer Custom Patch Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer_Patch_PlugIn_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004787).

## Parameters

- `name`: The name of the previously bound texture.
- `cgl_ctx`: The CGL context.

## See Also

- [func render(toBuffer: UnsafeMutableRawPointer!, withBytesPerRow: Int, pixelFormat: String!, forBounds: NSRect) -> Bool](qcpluginoutputimageprovider/render(tobuffer:withbytesperrow:pixelformat:forbounds:).md)
  Renders a subregion of the image into  the supplied memory buffer using the specified pixel format.
- [func copyRenderedTexture(forCGLContext: CGLContextObj!, pixelFormat: String!, bounds: NSRect, isFlipped: UnsafeMutablePointer<ObjCBool>!) -> GLuint](qcpluginoutputimageprovider/copyrenderedtexture(forcglcontext:pixelformat:bounds:isflipped:).md)
  Returns the name of an OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that contains a subregion of the image in a given pixel format.
- [func render(withCGLContext: CGLContextObj!, forBounds: NSRect) -> Bool](qcpluginoutputimageprovider/render(withcglcontext:forbounds:).md)
  Renders a subregion of the image to the provided CGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/releaserenderedtexture(_:forcglcontext:))*