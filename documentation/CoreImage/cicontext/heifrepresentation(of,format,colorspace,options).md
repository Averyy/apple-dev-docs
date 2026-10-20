# heifRepresentation(of:format:colorSpace:options:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Renders the image and exports the resulting image data in HEIF format.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13.4+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func heifRepresentation(of image: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) -> Data?
```

```objc
- (NSData *) HEIFRepresentationOfImage:(CIImage *) image format:(CIFormat) format colorSpace:(CGColorSpaceRef) colorSpace options:(NSDictionary<NSString *,id> *) options;
```

#### Return Value

A data representation of the rendered image in HEIF format, or `nil` if the image could not be rendered.

#### Discussion

To render an image for export, the image’s contents must not be empty and its [`extent`](../ciimage/extent.md) dimensions must be finite. To export after applying a filter whose output has infinite extent, see the [`clampedToExtent()`](../ciimage/clampedtoextent%28%29.md) method.

## Parameters

- `image`: The image object to render.
- `format`: The pixel format for the output image.
- `colorSpace`: The color space in which to render the output image. This color space must conform to either the [`CGColorSpaceModel.rgb`](../../CoreGraphics/cgcolorspacemodel/rgb.md) or [`CGColorSpaceModel.monochrome`](../../CoreGraphics/cgcolorspacemodel/monochrome.md) model and must be compatible with the specified pixel format.
- `options`: A dictionary with additional options for export. Supported keys include [`kCGImageDestinationLossyCompressionQuality`](../../ImageIO/kcgimagedestinationlossycompressionquality.md), [`avDepthData`](../ciimagerepresentationoption/avdepthdata.md), [`depthImage`](../ciimagerepresentationoption/depthimage.md), and [`disparityImage`](../ciimagerepresentationoption/disparityimage.md).

## See Also

### Rendering Images for Data or File Export
- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./tiffrepresentation%28of,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./jpegrepresentation%28of,colorspace,options%29.md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./pngrepresentation%28of,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data in PNG format.
- [func heif10Representation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws -> Data](./heif10representation%28of,colorspace,options%29.md)
  Renders the image and exports the resulting image data in HEIF10 format.
- [func openEXRRepresentation(of: CIImage, options: [CIImageRepresentationOption : Any]) throws -> Data](./openexrrepresentation%28of,options%29.md)
  Renders the image and exports the resulting image data in open EXR format.
- [func writeTIFFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./writetiffrepresentation%28of,to,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in TIFF format.
- [func writeJPEGRepresentation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./writejpegrepresentation%28of,to,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in JPEG format.
- [func writePNGRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./writepngrepresentation%28of,to,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in PNG format.
- [func writeHEIFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./writeheifrepresentation%28of,to,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in HEIF format.
- [func writeHEIF10Representation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](./writeheif10representation%28of,to,colorspace,options%29.md)
  Renders the image and exports the resulting image data as a file in HEIF10 format.
- [func writeOpenEXRRepresentation(of: CIImage, to: URL, options: [CIImageRepresentationOption : Any]) throws](./writeopenexrrepresentation%28of,to,options%29.md)
  Renders the image and exports the resulting image data as a file in open EXR format.
- [struct CIImageRepresentationOption](../ciimagerepresentationoption.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/heifrepresentation(of:format:colorspace:options:))*