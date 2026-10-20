# tiffRepresentationOfImageReps(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns a TIFF representation of the specified images.

**Availability**:
- macOS

## Declaration

```swift
class func tiffRepresentationOfImageReps(in array: [NSImageRep]) -> Data?
```

```objc
+ (NSData *) TIFFRepresentationOfImageRepsInArray:(NSArray<NSImageRep *> *) array;
```

#### Return Value

A data object containing a TIFF image representation.

#### Discussion

This method uses the compression returned by [`getCompression(_:factor:)`](./getcompression%28_,factor%29.md) (if applicable). If a problem is encountered during generation of the TIFF, this method raises an [`NSTIFFException`](../nstiffexception.md) or an [`NSBadBitmapParametersException`](../nsbadbitmapparametersexception.md).

## Parameters

- `array`: An array containing objects representing bitmap image representations.

## See Also

### Producing Other Representations of Images
- [class func tiffRepresentationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](./tiffrepresentationofimagereps%28in,using,factor%29.md)
  Returns a TIFF representation of the specified images using the specified compression scheme and factor.
- [var tiffRepresentation: Data?](./tiffrepresentation.md)
  A TIFF representation of the bitmap image data.
- [func tiffRepresentation(using: NSBitmapImageRep.TIFFCompression, factor: Float) -> Data?](./tiffrepresentation%28using,factor%29.md)
  Returns a TIFF representation of the image using the specified compression.
- [class func representationOfImageReps(in: [NSImageRep], using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](./representationofimagereps%28in,using,properties%29.md)
  Formats the specified bitmap images using the specified storage type and properties and returns them in a data object.
- [func representation(using: NSBitmapImageRep.FileType, properties: [NSBitmapImageRep.PropertyKey : Any]) -> Data?](./representation%28using,properties%29.md)
  Formats the bitmap representation’s image data using the specified storage type and properties and returns it in a data object.
- [func NSDrawBitmap(NSRect, Int, Int, Int, Int, Int, Int, Bool, Bool, NSColorSpaceName, UnsafePointer<UnsafePointer<UInt8>?>)](../nsdrawbitmap%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Draws a bitmap image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/tiffrepresentationofimagereps(in:))*