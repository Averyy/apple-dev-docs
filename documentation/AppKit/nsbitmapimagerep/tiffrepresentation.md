# tiffRepresentation

**Framework**: AppKit  
**Kind**: property

A TIFF representation of the bitmap image data.

**Availability**:
- macOS ?+

## Declaration

```swift
var tiffRepresentation: Data? { get }
```

#### Discussion

Accessing this property results in a call to the [`tiffRepresentation(using:factor:)`](nsbitmapimagerep/tiffrepresentation(using:factor:).md) method using the stored compression type and factor retrieved from the initial image data or changed using the [`setCompression(_:factor:)`](nsbitmapimagerep/setcompression(_:factor:).md) method. If the stored compression type isn’t supported for writing TIFF data (for example, [`NSBitmapImageRep.TIFFCompression.next`](nsbitmapimagerep/tiffcompression/next.md)), the stored compression is changed to [`NSBitmapImageRep.TIFFCompression.none`](nsbitmapimagerep/tiffcompression/none.md) before calling the [`tiffRepresentation(using:factor:)`](nsbitmapimagerep/tiffrepresentation(using:factor:).md) method using the compression that’s returned by [`getCompression(_:factor:)`](nsbitmapimagerep/getcompression(_:factor:).md) (if applicable).

If a problem is encountered during generation of the TIFF, an [`NSTIFFException`](nstiffexception.md) or an [`NSBadBitmapParametersException`](nsbadbitmapparametersexception.md) is raised.

## See Also

- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsimage/tiffrepresentation(using:factor:).md)
  Returns a data object that contains TIFF data with the specified compression settings for all of the image representations in the image.
- [var tiffRepresentation: Data?](nsimage/tiffrepresentation.md)
  A data object containing TIFF data for all of the image representations in the image.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep]) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:).md)
  Returns a TIFF representation of the specified images.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:using:factor:).md)
  Returns a TIFF representation of the specified images using the specified compression scheme and factor.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentation(using:factor:).md)
  Returns a TIFF representation of the image using the specified compression.
- [class func representationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representationofimagereps(in:using:properties:).md)
  Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representation(using:properties:).md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func NSDrawBitmap(NSRect, Int, Int, Int, Int, Int, Int, Bool, Bool, NSColorSpaceName, UnsafePointer<UnsafePointer<UInt8>?>)](nsdrawbitmap(_:_:_:_:_:_:_:_:_:_:_:).md)
  Draws a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/tiffrepresentation)*