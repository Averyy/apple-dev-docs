# tiffRepresentation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A TIFF representation of the bitmap image data.

**Availability**:
- macOS

## Declaration

```swift
var tiffRepresentation: Data? { get }
```

```objc
@property (copy, readonly, nullable) NSData * TIFFRepresentation;
```

#### Discussion

Accessing this property results in a call to the [`tiffRepresentation(using:factor:)`](./tiffrepresentation%28using,factor%29.md) method using the stored compression type and factor retrieved from the initial image data or changed using the [`setCompression(_:factor:)`](./setcompression%28_,factor%29.md) method. If the stored compression type isn’t supported for writing TIFF data (for example, [`NSBitmapImageRep.TIFFCompression.next`](./tiffcompression/next.md)), the stored compression is changed to [`NSBitmapImageRep.TIFFCompression.none`](./tiffcompression/none.md) before calling the [`tiffRepresentation(using:factor:)`](./tiffrepresentation%28using,factor%29.md) method using the compression that’s returned by [`getCompression(_:factor:)`](./getcompression%28_,factor%29.md) (if applicable).

If a problem is encountered during generation of the TIFF, an [`NSTIFFException`](../nstiffexception.md) or an [`NSBadBitmapParametersException`](../nsbadbitmapparametersexception.md) is raised.

## See Also

### Related Documentation
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](../nsimage/tiffrepresentation%28using,factor%29.md)
  Returns a data object that contains TIFF data with the specified compression settings for all of the image representations in the image.
- [var tiffRepresentation: Data?](../nsimage/tiffrepresentation.md)
  A data object containing TIFF data for all of the image representations in the image.
### Producing Other Representations of Images
- [class func tiffRepresentationOfImageReps(in: [NSImageRep]) -> Data?](./tiffrepresentationofimagereps%28in%29.md)
  Returns a TIFF representation of the specified images.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](./tiffrepresentationofimagereps%28in,using,factor%29.md)
  Returns a TIFF representation of the specified images using the specified compression scheme and factor.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](./tiffrepresentation%28using,factor%29.md)
  Returns a TIFF representation of the image using the specified compression.
- [class func representationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](./representationofimagereps%28in,using,properties%29.md)
  Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](./representation%28using,properties%29.md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func NSDrawBitmap(NSRect, Int, Int, Int, Int, Int, Int, Bool, Bool, NSColorSpaceName, UnsafePointer<UnsafePointer<UInt8>?>)](../nsdrawbitmap%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Draws a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/tiffrepresentation)*