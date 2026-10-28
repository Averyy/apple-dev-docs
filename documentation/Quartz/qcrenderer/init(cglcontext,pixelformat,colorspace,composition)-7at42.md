# init(cglContext:pixelFormat:colorSpace:composition:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Creates a  renderer object  with a `CGLContextObj` object, a pixel format, a color space, and a composition object.

**Availability**:
- macOS 10.5+ - Deprecated in 10.14

> **Deprecated**: Quartz Composer OpenGL API deprecated. (Define QC_SILENCE_GL_DEPRECATION to silence these warnings)

## Declaration

```swift
init!(cglContext context: CGLContextObj!, pixelFormat format: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)
```

```objc
- (id) initWithCGLContext:(CGLContextObj) context pixelFormat:(CGLPixelFormatObj) format colorSpace:(CGColorSpaceRef) colorSpace composition:(QCComposition *) composition;
```

## Return Value

The initialized `QCRenderer` object or `nil` if initialization is not successful.

## Parameters

- `context`: A  `CGLContextObj` object. The object that you supply must have both a color and a depth buffer.
- `format`: A  `CGLPixelFormatObj`  object.
- `colorSpace`: A Quartz color space object. This must be an RGB color space. Pass `NULL` to use the default RGB color space. For more information on Quartz color spaces, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).
- `composition`: A [`QCComposition`](../qccomposition.md) object.

## See Also

### Creating and Initializing a Renderer
- [init!(composition: QCComposition!, colorSpace: CGColorSpace!)](./init%28composition,colorspace%29.md)
  Creates a  renderer object  with a composition object and a color space.
- [init!(openGLContext: NSOpenGLContext!, pixelFormat: NSOpenGLPixelFormat!, file: String!)](./init%28openglcontext,pixelformat,file%29.md)
  Creates a  renderer object with an `NSOpenGLContext` object and a composition file.
- [init!(offScreenWith: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)](./init%28offscreenwith,colorspace,composition%29.md)
  Creates an offscreen renderer of a given size with the provided color space and composition object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/init(cglcontext:pixelformat:colorspace:composition:)-7at42)*