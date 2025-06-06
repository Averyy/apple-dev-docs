# tiffRepresentation(using:factor:)

**Framework**: AppKit  
**Kind**: method

Returns a data object that contains TIFF data with the specified compression settings for all of the image representations in the image.

**Availability**:
- macOS ?+

## Declaration

```swift
func tiffRepresentation(using comp: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?
```

#### Return Value

A data object containing the TIFF data, or `nil` if the TIFF data could not be created.

#### Discussion

You can use the returned data object to write the TIFF data to a file. If the specified compression isn’t applicable, no compression is used. If a problem is encountered during generation of the TIFF data, this method may raise an exception.

If one of the receiver’s image representations does not support the creation of TIFF data natively (PDF and EPS images, for example), this method creates the TIFF data from that representation’s cached content.

Additional image formats can be saved by using the `NSBitmapImageRep` method [`representation(using:properties:)`](nsbitmapimagerep/representation(using:properties:).md).

## Parameters

- `comp`: The type of compression to use. For a list of values, see the constants in  .
- `factor`: Provides a hint for compression types that implement variable compression ratios. Currently, only JPEG compression uses a compression factor.

## See Also

- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representation(using:properties:).md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentation(using:factor:).md)
  Returns a TIFF representation of the image using the specified compression.
- [var tiffRepresentation: Data?](nsbitmapimagerep/tiffrepresentation.md)
  A TIFF representation of the bitmap image data.
- [var tiffRepresentation: Data?](nsimage/tiffrepresentation.md)
  A data object containing TIFF data for all of the image representations in the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/tiffrepresentation(using:factor:))*