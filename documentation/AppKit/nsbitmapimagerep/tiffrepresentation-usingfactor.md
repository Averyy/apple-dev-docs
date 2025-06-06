# tiffRepresentation(using:factor:)

**Framework**: AppKit  
**Kind**: method

Returns a TIFF representation of the image using the specified compression.

**Availability**:
- macOS ?+

## Declaration

```swift
func tiffRepresentation(using comp: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?
```

#### Discussion

If the compression type isn’t supported for writing TIFF data (for example, [`NSBitmapImageRep.TIFFCompression.next`](nsbitmapimagerep/tiffcompression/next.md)), the stored compression is changed to [`NSBitmapImageRep.TIFFCompression.none`](nsbitmapimagerep/tiffcompression/none.md) before the TIFF representation is generated.

If a problem is encountered during generation of the TIFF, [`tiffRepresentation(using:factor:)`](nsbitmapimagerep/tiffrepresentation(using:factor:).md) raises an [`NSTIFFException`](nstiffexception.md) or an [`NSBadBitmapParametersException`](nsbadbitmapparametersexception.md).

## Parameters

- `comp`: An enum constant that represents a TIFF data-compression scheme. Legal values for   can be found in  .
- `factor`: Currently only JPEG compression uses a compression factor. JPEG compression in TIFF files is not supported, and   is ignored.

## See Also

- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsimage/tiffrepresentation(using:factor:).md)
  Returns a data object that contains TIFF data with the specified compression settings for all of the image representations in the image.
- [func canBeCompressed(using: NSBitmapImageRep.TIFFCompression) -> Bool](nsbitmapimagerep/canbecompressed(using:).md)
  Tests whether the bitmap image representation can be compressed by the specified compression scheme.
- [var tiffRepresentation: Data?](nsimage/tiffrepresentation.md)
  A data object containing TIFF data for all of the image representations in the image.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep]) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:).md)
  Returns a TIFF representation of the specified images.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:using:factor:).md)
  Returns a TIFF representation of the specified images using the specified compression scheme and factor.
- [var tiffRepresentation: Data?](nsbitmapimagerep/tiffrepresentation.md)
  A TIFF representation of the bitmap image data.
- [class func representationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representationofimagereps(in:using:properties:).md)
  Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representation(using:properties:).md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func NSDrawBitmap(NSRect, Int, Int, Int, Int, Int, Int, Bool, Bool, NSColorSpaceName, UnsafePointer<UnsafePointer<UInt8>?>)](nsdrawbitmap(_:_:_:_:_:_:_:_:_:_:_:).md)
  Draws a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/tiffrepresentation(using:factor:))*