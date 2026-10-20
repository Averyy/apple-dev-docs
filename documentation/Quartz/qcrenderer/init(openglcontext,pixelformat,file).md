# init(openGLContext:pixelFormat:file:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Creates a  renderer object with an `NSOpenGLContext` object and a composition file.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init!(openGLContext context: NSOpenGLContext!, pixelFormat format: NSOpenGLPixelFormat!, file path: String!)
```

```objc
- (id) initWithOpenGLContext:(NSOpenGLContext *) context pixelFormat:(NSOpenGLPixelFormat *) format file:(NSString *) path;
```

#### Return Value

An initialized `QCRenderer` object or `nil` if initialization is not successful.

## Parameters

- `context`: An [`NSOpenGLContext`](../../AppKit/nsopenglcontext.md) object. The object that you supply must have both a color and a depth buffer.
- `format`: An  [`NSOpenGLPixelFormat`](../../AppKit/nsopenglpixelformat.md)  object.
- `path`: A string that specifies the location of a composition(`.qtz`) file.

## See Also

### Creating and Initializing a Renderer
- [init!(composition: QCComposition!, colorSpace: CGColorSpace!)](./init%28composition,colorspace%29.md)
  Creates a  renderer object  with a composition object and a color space.
- [init!(cglContext: CGLContextObj!, pixelFormat: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)](./init%28cglcontext,pixelformat,colorspace,composition%29-7at42.md)
  Creates a  renderer object  with a `CGLContextObj` object, a pixel format, a color space, and a composition object.
- [init!(offScreenWith: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)](./init%28offscreenwith,colorspace,composition%29.md)
  Creates an offscreen renderer of a given size with the provided color space and composition object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/init(openglcontext:pixelformat:file:))*