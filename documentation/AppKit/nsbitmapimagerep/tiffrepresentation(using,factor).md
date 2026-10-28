# tiffRepresentation(using:factor:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a TIFF representation of the image using the specified compression.

**Availability**:
- macOS

## Declaration

```swift
func tiffRepresentation(using comp: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?
```

```objc
- (NSData *) TIFFRepresentationUsingCompression:(NSTIFFCompression) comp factor:(float) factor;
```

## Discussion

If the compression type isn’t supported for writing TIFF data (for example, [`NSBitmapImageRep.TIFFCompression.next`](./tiffcompression/next.md)), the stored compression is changed to [`NSBitmapImageRep.TIFFCompression.none`](./tiffcompression/none.md) before the TIFF representation is generated.

If a problem is encountered during generation of the TIFF, [`tiffRepresentation(using:factor:)`](./tiffrepresentation%28using,factor%29.md) raises an [`NSTIFFException`](../nstiffexception.md) or an [`NSBadBitmapParametersException`](../nsbadbitmapparametersexception.md).

## Parameters

- `comp`: An enum constant that represents a TIFF data-compression scheme. Legal values for `compression` can be found in [`NSBitmapImageRep.TIFFCompression`](./tiffcompression.md).
- `factor`: A `float` value that provides a hint for those compression types that implement variable compression ratios.

  Currently only JPEG compression uses a compression factor. JPEG compression in TIFF files is not supported, and `factor` is ignored.

## See Also

### Related Documentation
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](../nsimage/tiffrepresentation%28using,factor%29.md)
  Returns a data object that contains TIFF data with the specified compression settings for all of the image representations in the image.
- [func canBeCompressed(using: NSBitmapImageRep.TIFFCompression) -> Bool](./canbecompressed%28using%29.md)
  Tests whether the bitmap image representation can be compressed by the specified compression scheme.
- [var tiffRepresentation: Data?](../nsimage/tiffrepresentation.md)
  A data object containing TIFF data for all of the image representations in the image.
### Producing Other Representations of Images
- [class func tiffRepresentationOfImageReps(in: [NSImageRep]) -> Data?](./tiffrepresentationofimagereps%28in%29.md)
  Returns a TIFF representation of the specified images.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](./tiffrepresentationofimagereps%28in,using,factor%29.md)
  Returns a TIFF representation of the specified images using the specified compression scheme and factor.
- [var tiffRepresentation: Data?](./tiffrepresentation.md)
  A TIFF representation of the bitmap image data.
- [class func representationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](./representationofimagereps%28in,using,properties%29.md)
  Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](./representation%28using,properties%29.md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func NSDrawBitmap(NSRect, Int, Int, Int, Int, Int, Int, Bool, Bool, NSColorSpaceName, UnsafePointer<UnsafePointer<UInt8>?>)](../nsdrawbitmap%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Draws a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/tiffrepresentation(using:factor:))*