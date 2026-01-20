# writeOpenEXRRepresentation(of:to:options:)

**Framework**: Core Image  
**Kind**: method

Renders the image and exports the resulting image data as a file in open EXR format.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func writeOpenEXRRepresentation(of image: CIImage, to url: URL, options: [CIImageRepresentationOption : Any] = [:]) throws
```

## Parameters

- `image`: The image object to render.
- `url`: The file URL at which to write the output HEIF file.
- `options`: A dictionary with additional options for export.

## See Also

- [func tiffRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/tiffrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in TIFF format.
- [func jpegRepresentation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/jpegrepresentation(of:colorspace:options:).md)
  Renders the image and exports the resulting image data in JPEG format.
- [func pngRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/pngrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in PNG format.
- [func heifRepresentation(of: CIImage, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) -> Data?](cicontext/heifrepresentation(of:format:colorspace:options:).md)
  Renders the image and exports the resulting image data in HEIF format.
- [func heif10Representation(of: CIImage, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws -> Data](cicontext/heif10representation(of:colorspace:options:).md)
  Renders the image and exports the resulting image data in HEIF10 format.
- [func openEXRRepresentation(of: CIImage, options: [CIImageRepresentationOption : Any]) throws -> Data](cicontext/openexrrepresentation(of:options:).md)
  Renders the image and exports the resulting image data in open EXR format.
- [func writeTIFFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writetiffrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in TIFF format.
- [func writeJPEGRepresentation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writejpegrepresentation(of:to:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in JPEG format.
- [func writePNGRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writepngrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in PNG format.
- [func writeHEIFRepresentation(of: CIImage, to: URL, format: CIFormat, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writeheifrepresentation(of:to:format:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in HEIF format.
- [func writeHEIF10Representation(of: CIImage, to: URL, colorSpace: CGColorSpace, options: [CIImageRepresentationOption : Any]) throws](cicontext/writeheif10representation(of:to:colorspace:options:).md)
  Renders the image and exports the resulting image data as a file in HEIF10 format.
- [struct CIImageRepresentationOption](ciimagerepresentationoption.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/writeopenexrrepresentation(of:to:options:))*