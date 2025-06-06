# init(composition:colorSpace:)

**Framework**: Quartz  
**Kind**: init

Creates a  renderer object  with a composition object and a color space.

**Availability**:
- macOS 10.4+

## Declaration

```swift
init!(composition: QCComposition!, colorSpace: CGColorSpace!)
```

#### Return Value

The initialized `QCRenderer` object or `nil` if initialization is not successful.

#### Discussion

Note that [`snapshotImage()`](qcrenderer/snapshotimage().md) and [`createSnapshotImage(ofType:)`](qcrenderer/createsnapshotimage(oftype:).md) always returns `nil` on such `QCRenderer` instances.

## Parameters

- `composition`: A   object. The composition must  not contain any consumer patches. That is, the composition can receive data, process it, and produce output values, but it cannot perform any rendering.
- `colorSpace`: A Quartz color space object. This must be an RGB color space. Pass   to use the default RGB color space. The color space is used only for the images produced by the  output image ports of the composition. For more information on Quartz color spaces, see  .

## See Also

- [init!(openGLContext: NSOpenGLContext!, pixelFormat: NSOpenGLPixelFormat!, file: String!)](qcrenderer/init(openglcontext:pixelformat:file:).md)
  Creates a  renderer object with an `NSOpenGLContext` object and a composition file.
- [init!(cglContext: CGLContextObj!, pixelFormat: CGLPixelFormatObj!, colorSpace: CGColorSpace!, composition: QCComposition!)](qcrenderer/init(cglcontext:pixelformat:colorspace:composition:).md)
  Creates a  renderer object  with a `CGLContextObj` object, a pixel format, a color space, and a composition object.
- [init!(offScreenWith: NSSize, colorSpace: CGColorSpace!, composition: QCComposition!)](qcrenderer/init(offscreenwith:colorspace:composition:).md)
  Creates an offscreen renderer of a given size with the provided color space and composition object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcrenderer/init(composition:colorspace:))*