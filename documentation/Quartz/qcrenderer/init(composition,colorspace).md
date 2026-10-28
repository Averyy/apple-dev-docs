# init(composition:colorSpace:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Creates a  renderer object  with a composition object and a color space.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
init!(composition: QCComposition!, colorSpace: CGColorSpace!)
```

```objc
- (id) initWithComposition:(QCComposition *) composition colorSpace:(CGColorSpaceRef) colorSpace;
```

## Return Value

The initialized `QCRenderer` object or `nil` if initialization is not successful.

## Discussion

Note that [`snapshotImage()`](./snapshotimage%28%29.md) and [`createSnapshotImage(ofType:)`](./createsnapshotimage%28oftype%29.md) always returns `nil` on such `QCRenderer` instances.

## Parameters

- `composition`: A [`QCComposition`](../qccomposition.md) object. The composition must  not contain any consumer patches. That is, the composition can receive data, process it, and produce output values, but it cannot perform any rendering.
- `colorSpace`: A Quartz color space object. This must be an RGB color space. Pass `NULL` to use the default RGB color space. The color space is used only for the images produced by the  output image ports of the composition. For more information on Quartz color spaces, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066).

## See Also

### Creating and Initializing a Renderer
- [init!(openGLContext: NSOpenGLContext!, pixelFormat: NSOpenGLPixelFormat!, file: String!)](./init%28openglcontext,pixelformat,file%29.md)
  Creates a  renderer object with an `NSOpenGLContext` object and a composition file.
- [init!(cglContext: CGLContextObj!, pixelFormat: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)](./init%28cglcontext,pixelformat,colorspace,composition%29-7at42.md)
  Creates a  renderer object  with a `CGLContextObj` object, a pixel format, a color space, and a composition object.
- [init!(offScreenWith: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)](./init%28offscreenwith,colorspace,composition%29.md)
  Creates an offscreen renderer of a given size with the provided color space and composition object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/init(composition:colorspace:))*