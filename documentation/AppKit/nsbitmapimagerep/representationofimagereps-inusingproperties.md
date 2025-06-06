# representationOfImageReps(in:using:properties:)

**Framework**: AppKit  
**Kind**: method

Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.

**Availability**:
- macOS ?+

## Declaration

```swift
class func representationOfImageReps(in imageReps: [NSImageRep], using storageType: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?
```

#### Return Value

A data object containing the bitmap image data in the specified format. You can write this data to a file or use it to create a new [`NSBitmapImageRep`](nsbitmapimagerep.md) object.

## Parameters

- `imageReps`: An array of   objects.
- `storageType`: An   constant specifying a file type for bitmap images.
- `properties`: A dictionary that contains key-value pairs specifying image properties. These string constants used as keys and the valid values are described in  .

## See Also

- [class func tiffRepresentationOfImageReps(in: [NSImageRep]) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:).md)
  Returns a TIFF representation of the specified images.
- [class func tiffRepresentationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentationofimagereps(in:using:factor:).md)
  Returns a TIFF representation of the specified images using the specified compression scheme and factor.
- [var tiffRepresentation: Data?](nsbitmapimagerep/tiffrepresentation.md)
  A TIFF representation of the bitmap image data.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](nsbitmapimagerep/tiffrepresentation(using:factor:).md)
  Returns a TIFF representation of the image using the specified compression.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](nsbitmapimagerep/representation(using:properties:).md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func NSDrawBitmap(NSRect, Int, Int, Int, Int, Int, Int, Bool, Bool, NSColorSpaceName, UnsafePointer<UnsafePointer<UInt8>?>)](nsdrawbitmap(_:_:_:_:_:_:_:_:_:_:_:).md)
  Draws a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/representationofimagereps(in:using:properties:))*