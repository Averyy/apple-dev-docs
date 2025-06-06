# init(offScreenWith:colorSpace:composition:)

**Framework**: Quartz  
**Kind**: init

Creates an offscreen renderer of a given size with the provided color space and composition object.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init!(offScreenWith size: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)
```

#### Return Value

The initialized `QCRenderer` object or `nil` if initialization is not successful.

#### Discussion

This method creates an internal OpenGL context and pixel buffer. Because offscreen rendering is performed on the GPU, the maximum rendering size is limited to the GPU capacity. On typical hardware, the limit is at least 2048 by 2048, but is often 4096 by 4096. The available VRAM affects performance.

## Parameters

- `size`: The size of the offscreen renderer.
- `colorSpace`: A Quartz color space object. This must be an RGB color space. Pass   to use the default RGB color space. For more information on Quartz color spaces, see  .
- `composition`: A   object.

## See Also

- [init!(composition: QCComposition!, colorSpace: CGColorSpace!)](qcrenderer/init(composition:colorspace:).md)
  Creates a  renderer object  with a composition object and a color space.
- [init!(openGLContext: NSOpenGLContext!, pixelFormat: NSOpenGLPixelFormat!, file: String!)](qcrenderer/init(openglcontext:pixelformat:file:).md)
  Creates a  renderer object with an `NSOpenGLContext` object and a composition file.
- [init!(cglContext: CGLContextObj!, pixelFormat: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)](qcrenderer/init(cglcontext:pixelformat:colorspace:composition:).md)
  Creates a  renderer object  with a `CGLContextObj` object, a pixel format, a color space, and a composition object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/init(offscreenwith:colorspace:composition:))*