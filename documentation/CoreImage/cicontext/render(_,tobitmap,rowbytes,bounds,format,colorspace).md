# render(_:toBitmap:rowBytes:bounds:format:colorSpace:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Renders to the given bitmap.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func render(_ image: CIImage, toBitmap data: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)
```

```objc
- (void) render:(CIImage *) image toBitmap:(void *) data rowBytes:(ptrdiff_t) rowBytes bounds:(CGRect) bounds format:(CIFormat) format colorSpace:(CGColorSpaceRef) colorSpace;
```

## Parameters

- `image`: A Core Image image object.
- `data`: Storage for the bitmap data.
- `rowBytes`: The bytes per row.
- `bounds`: The bounds of the bitmap data.
- `format`: The format of the bitmap data.
- `colorSpace`: The color space for the data. Pass `NULL` if you want to use the output color space of the context.

## See Also

### Rendering Images
- [func createCGImage(CIImage, from: CGRect) -> CGImage?](./createcgimage%28_,from%29.md)
  Creates a Core Graphics image from a region of a Core Image image instance.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage?](./createcgimage%28_,from,format,colorspace%29.md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?](./createcgimage%28_,from,format,colorspace,deferred%29.md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [func render(CIImage, to: CVPixelBuffer)](./render%28_,to%29.md)
  Renders an image into a pixel buffer.
- [func render(CIImage, to: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](./render%28_,to,bounds,colorspace%29-2k8l2.md)
  Renders a region of an image into a pixel buffer.
- [func render(CIImage, to: IOSurfaceRef, bounds: CGRect, colorSpace: CGColorSpace?)](./render%28_,to,bounds,colorspace%29-54b9l.md)
  Renders a region of an image into an IOSurface object.
- [func render(CIImage, to: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?, bounds: CGRect, colorSpace: CGColorSpace)](./render%28_,to,commandbuffer,bounds,colorspace%29.md)
  Renders a region of an image to a Metal texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/render(_:tobitmap:rowbytes:bounds:format:colorspace:))*