# init(cglContext:pixelFormat:colorSpace:composition:)

**Framework**: Quartz  
**Kind**: init

Creates a  renderer object  with a `CGLContextObj` object, a pixel format, a color space, and a composition object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(cglContext context: CGLContextObj!, pixelFormat format: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)
```

#### Return Value

The initialized `QCRenderer` object or `nil` if initialization is not successful.

## Parameters

- `context`: A    object. The object that you supply must have both a color and a depth buffer.
- `format`: A     object.
- `colorSpace`: A Quartz color space object. This must be an RGB color space. Pass   to use the default RGB color space. For more information on Quartz color spaces, see  .
- `composition`: A   object.

## See Also

- [init!(composition: QCComposition!, colorSpace: CGColorSpace!)](qcrenderer/init(composition:colorspace:).md)
  Creates a  renderer object  with a composition object and a color space.
- [init!(openGLContext: NSOpenGLContext!, pixelFormat: NSOpenGLPixelFormat!, file: String!)](qcrenderer/init(openglcontext:pixelformat:file:).md)
  Creates a  renderer object with an `NSOpenGLContext` object and a composition file.
- [init!(offScreenWith: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)](qcrenderer/init(offscreenwith:colorspace:composition:).md)
  Creates an offscreen renderer of a given size with the provided color space and composition object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/init(cglcontext:pixelformat:colorspace:composition:))*