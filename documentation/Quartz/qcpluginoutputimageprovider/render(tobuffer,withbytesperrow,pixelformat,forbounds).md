# render(toBuffer:withBytesPerRow:pixelFormat:forBounds:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Renders a subregion of the image into  the supplied memory buffer using the specified pixel format.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
optional func render(toBuffer baseAddress: UnsafeMutableRawPointer!, withBytesPerRow rowBytes: Int, pixelFormat format: String!, forBounds bounds: NSRect) -> Bool
```

```objc
- (BOOL) renderToBuffer:(void *) baseAddress withBytesPerRow:(NSUInteger) rowBytes pixelFormat:(NSString *) format forBounds:(NSRect) bounds;
```

## Return Value

[`true`](../../Swift/true.md) if the image is rendered successfully into the buffer; [`false`](../../Swift/false.md) on failure or if the image provider doesn’t support CPU rendering.

## Discussion

The Quartz Composer engine calls this method when it needs pixels. It gives you the base address, the number of row bytes, and the format. Then, you write pixels to the buffer.

## Parameters

- `baseAddress`: The base address of the memory buffer. The Quartz Composer engine passes you an address that is aligned on a 16-byte boundary.
- `rowBytes`: The number of bytes per row of the image data. The Quartz Composer engine guarantees this value is a multiple of 16.
- `format`: The pixel format of the image data.
- `bounds`: The bounds of the subregion.

## See Also

### Rendering an Image to a Destination
- [func copyRenderedTexture(forCGLContext: CGLContextObj!, pixelFormat: String!, bounds: NSRect, isFlipped: UnsafeMutablePointer<ObjCBool>!) -> GLuint](./copyrenderedtexture%28forcglcontext,pixelformat,bounds,isflipped%29.md)
  Returns the name of an OpenGL texture of type `GL_TEXTURE_RECTANGLE_EXT` that contains a subregion of the image in a given pixel format.
- [func render(withCGLContext: CGLContextObj!, forBounds: NSRect) -> Bool](./render%28withcglcontext,forbounds%29.md)
  Renders a subregion of the image to the provided CGL context.
- [func releaseRenderedTexture(GLuint, forCGLContext: CGLContextObj!)](./releaserenderedtexture%28_,forcglcontext%29.md)
  Releases the previously copied texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginoutputimageprovider/render(tobuffer:withbytesperrow:pixelformat:forbounds:))*