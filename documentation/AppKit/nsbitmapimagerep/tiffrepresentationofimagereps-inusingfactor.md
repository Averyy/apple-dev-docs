# tiffRepresentationOfImageReps(in:using:factor:)

**Framework**: AppKit  
**Kind**: method

Returns a TIFF representation of the specified images using the specified compression scheme and factor.

**Availability**:
- macOS ?+

## Declaration

```swift
class func tiffRepresentationOfImageReps(in array: [NSImageRep], using comp: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?
```

#### Return Value

A data object containing a TIFF image representation.

#### Discussion

If the specified compression isn’t applicable, no compression is used. If a problem is encountered during generation of the TIFF, the method raises an [`NSTIFFException`](nstiffexception.md) or an [`NSBadBitmapParametersException`](nsbadbitmapparametersexception.md).

## Parameters

- `array`: An array containing objects representing bitmap image representations.
- `comp`: An enum constant that represents a TIFF data-compression scheme. Legal values for   can be found in  .
- `factor`: Currently only JPEG compression uses a compression factor. JPEG compression in TIFF files is not supported, and   is ignored.

## See Also

- [class func tiffRepresentationOfImageReps(in: [NSImageRep]) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:).md)
  Returns a TIFF representation of the specified images.
- [var tiffRepresentation: Data?](nsbitmapimagerep/tiffrepresentation.md)
  A TIFF representation of the bitmap image data.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentation(using:factor:).md)
  Returns a TIFF representation of the image using the specified compression.
- [class func representationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representationofimagereps(in:using:properties:).md)
  Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representation(using:properties:).md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func NSDrawBitmap(NSRect, Int, Int, Int, Int, Int, Int, Bool, Bool, NSColorSpaceName, UnsafePointer<UnsafePointer<UInt8>?>)](nsdrawbitmap(_:_:_:_:_:_:_:_:_:_:_:).md)
  Draws a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/tiffrepresentationofimagereps(in:using:factor:))*