# heif10Representation(of:colorSpace:options:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Renders the image and exports the resulting image data in HEIF10 format.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
func heif10Representation(of image: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any] = [:]) throws -> Data
```

```objc
- (NSData *) HEIF10RepresentationOfImage:(CIImage *) image colorSpace:(CGColorSpaceRef) colorSpace options:(NSDictionary<NSString *,id> *) options error:(NSError **) errorPtr;
```

## Parameters

- `image`: The image object to render.
- `colorSpace`: The color space in which to render the output image.
- `options`: A dictionary with additional options for export.

## See Also

### Rendering Images for Data or File Export
- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./tiffrepresentation%28of,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./jpegrepresentation%28of,colorspace,options%29.md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./pngrepresentation%28of,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data in PNG format.
- [func heifRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](./heifrepresentation%28of,format,colorspace,options%29.md)
  Renders the image and exports the resulting image data in HEIF format.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/heif10representation(of:colorspace:options:))*