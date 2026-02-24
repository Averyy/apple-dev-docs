# createCGImage(_:from:format:colorSpace:)

**Framework**: Core Image  
**Kind**: method

Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling the pixel format and color space of the `CGImage`.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func createCGImage(_ image: CIImage, from fromRect: CGRect, format: CIFormat, colorSpace: CGColorSpace?) -> CGImage?
```

#### Return Value

 Returns a new `CGImage` instance. You are responsible for releasing the returned image when you no longer need it. The returned value will be `null` if the extent is empty or too big.

## Parameters

- `image`: A [`CIImage`](ciimage.md) image instance for which to create a `CGImage`.
- `fromRect`: The `CGRect` region of the `image` to use. This region relative to the cartesean coordinate system of `image`. This region will be intersected with integralized and intersected with `image.extent`.
- `format`: A [`CIFormat`](ciformat.md) to specify the pixel format of the created `CGImage`. For example, if `kCIFormatRGBX16` is specified, then the created `CGImage` will be 16 bits-per-component and opaque.
- `colorSpace`: The `CGColorSpace` for the output image. This color space must have either `CGColorSpaceModel.rgb` or `CGColorSpaceModel.monochrome` and be compatible with the specified pixel format.

## See Also

- [func createCGImage(CIImage, from: CGRect) -> CGImage?](cicontext/createcgimage(_:from:).md)
  Creates a Core Graphics image from a region of a Core Image image instance.
- [func createCGImage(CIImage, from: CGRect, format: CIFormat, colorSpace: CGColorSpace?, deferred: Bool) -> CGImage?](cicontext/createcgimage(_:from:format:colorspace:deferred:).md)
  Creates a Core Graphics image from a region of a Core Image image instance with an option for controlling when the image is rendered.
- [func render(CIImage, toBitmap: UnsafeMutableRawPointer, rowBytes: Int, bounds: CGRect, format: CIFormat, colorSpace: CGColorSpace?)](cicontext/render(_:tobitmap:rowbytes:bounds:format:colorspace:).md)
  Renders to the given bitmap.
- [func render(CIImage, to: CVPixelBuffer)](cicontext/render(_:to:).md)
  Renders an image into a pixel buffer.
- [func render(CIImage, to: CVPixelBuffer, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/render(_:to:bounds:colorspace:)-2k8l2.md)
  Renders a region of an image into a pixel buffer.
- [func render(CIImage, to: IOSurfaceRef, bounds: CGRect, colorSpace: CGColorSpace?)](cicontext/render(_:to:bounds:colorspace:)-54b9l.md)
  Renders a region of an image into an IOSurface object.
- [func render(CIImage, to: any MTLTexture, commandBuffer: (any MTLCommandBuffer)?, bounds: CGRect, colorSpace: CGColorSpace)](cicontext/render(_:to:commandbuffer:bounds:colorspace:).md)
  Renders a region of an image to a Metal texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/createcgimage(_:from:format:colorspace:))*