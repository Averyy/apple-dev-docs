# init(openGLContext:pixelFormat:file:)

**Framework**: Quartz  
**Kind**: init

Creates a  renderer object with an `NSOpenGLContext` object and a composition file.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init!(openGLContext context: NSOpenGLContext!, pixelFormat format: NSOpenGLPixelFormat!, file path: String!)
```

#### Return Value

An initialized `QCRenderer` object or `nil` if initialization is not successful.

## Parameters

- `context`: An   object. The object that you supply must have both a color and a depth buffer.
- `format`: An     object.
- `path`: A string that specifies the location of a composition( ) file.

## See Also

- [init!(composition: QCComposition!, colorSpace: CGColorSpace!)](qcrenderer/init(composition:colorspace:).md)
  Creates a  renderer object  with a composition object and a color space.
- [init!(cglContext: CGLContextObj!, pixelFormat: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)](qcrenderer/init(cglcontext:pixelformat:colorspace:composition:).md)
  Creates a  renderer object  with a `CGLContextObj` object, a pixel format, a color space, and a composition object.
- [init!(offScreenWith: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)](qcrenderer/init(offscreenwith:colorspace:composition:).md)
  Creates an offscreen renderer of a given size with the provided color space and composition object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/init(openglcontext:pixelformat:file:))*