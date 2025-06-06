# render(toBuffer:withBytesPerRow:pixelFormat:forBounds:)

**Framework**: Quartz  
**Kind**: method

Renders a subregion of the image into  the supplied memory buffer using the specified pixel format.

**Availability**:
- macOS 10.4+

## Declaration

```swift
optional func render(toBuffer baseAddress: UnsafeMutableRawPointer!, withBytesPerRow rowBytes: Int, pixelFormat format: String!, forBounds bounds: NSRect) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the image is rendered successfully into the buffer; [`false`](https://developer.apple.com/documentation/swift/false) on failure or if the image provider doesn’t support CPU rendering.

#### Discussion

The Quartz Composer engine calls this method when it needs pixels. It gives you the base address, the number of row bytes, and the format. Then, you write pixels to the buffer.

## Parameters

- `baseAddress`: The base address of the memory buffer. The Quartz Composer engine passes you an address that is aligned on a 16-byte boundary.
- `rowBytes`: The number of bytes per row of the image data. The Quartz Composer engine guarantees this value is a multiple of 16.
- `format`: The pixel format of the image data.
- `bounds`: The bounds of the subregion.

## See Also

- [func copyRenderedTexture(forCGLContext: CGLContextObj!, pixelFormat: String!, bounds: NSRect, isFlipped: UnsafeMutablePointer<ObjCBool>!) -> GLuint](qcpluginoutputimageprovider/copyrenderedtexture(forcglcontext:pixelformat:bounds:isflipped:).md)
  Returns the name of an OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that contains a subregion of the image in a given pixel format.
- [func render(withCGLContext: CGLContextObj!, forBounds: NSRect) -> Bool](qcpluginoutputimageprovider/render(withcglcontext:forbounds:).md)
  Renders a subregion of the image to the provided CGL context.
- [func releaseRenderedTexture(GLuint, forCGLContext: CGLContextObj!)](qcpluginoutputimageprovider/releaserenderedtexture(_:forcglcontext:).md)
  Releases the previously copied texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/render(tobuffer:withbytesperrow:pixelformat:forbounds:))*