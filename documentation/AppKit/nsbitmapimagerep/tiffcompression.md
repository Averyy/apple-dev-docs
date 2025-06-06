# NSBitmapImageRep.TIFFCompression

**Framework**: AppKit  
**Kind**: enum

Constants that represent the supported TIFF data-compression schemes.

**Availability**:
- macOS ?+

## Declaration

```swift
enum TIFFCompression
```

## Topics

### Constants
- [NSBitmapImageRep.TIFFCompression.none](nsbitmapimagerep/tiffcompression/none.md)
  No compression.
- [NSBitmapImageRep.TIFFCompression.ccittfax3](nsbitmapimagerep/tiffcompression/ccittfax3.md)
  CCITT Fax Group 3 compression.
- [NSBitmapImageRep.TIFFCompression.ccittfax4](nsbitmapimagerep/tiffcompression/ccittfax4.md)
  CCITT Fax Group 4 compression.
- [NSBitmapImageRep.TIFFCompression.lzw](nsbitmapimagerep/tiffcompression/lzw.md)
  LZW compression.
- [NSBitmapImageRep.TIFFCompression.jpeg](nsbitmapimagerep/tiffcompression/jpeg.md)
  JPEG compression. No longer supported for input or output.
- [NSBitmapImageRep.TIFFCompression.next](nsbitmapimagerep/tiffcompression/next.md)
  NeXT compressed. Supported for input only.
- [NSBitmapImageRep.TIFFCompression.packBits](nsbitmapimagerep/tiffcompression/packbits.md)
  PackBits compression.
- [NSBitmapImageRep.TIFFCompression.oldJPEG](nsbitmapimagerep/tiffcompression/oldjpeg.md)
  Old JPEG compression. No longer supported for input or output.
### Initializers
- [init?(rawValue: UInt)](nsbitmapimagerep/tiffcompression/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func getTIFFCompressionTypes(UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count: UnsafeMutablePointer<Int>)](nsbitmapimagerep/gettiffcompressiontypes(_:count:).md)
  Returns by indirection an array of all available compression types that can be used when writing a TIFF image.
- [class func localizedName(forTIFFCompressionType: NSBitmapImageRep.TIFFCompression) -> String?](nsbitmapimagerep/localizedname(fortiffcompressiontype:).md)
  Returns an autoreleased string containing the localized name for the specified compression type.
- [func canBeCompressed(using: NSBitmapImageRep.TIFFCompression) -> Bool](nsbitmapimagerep/canbecompressed(using:).md)
  Tests whether the bitmap image representation can be compressed by the specified compression scheme.
- [func setCompression(NSBitmapImageRep.TIFFCompression, factor: Float)](nsbitmapimagerep/setcompression(_:factor:).md)
  Sets the bitmap image representation’s compression type and compression factor.
- [func getCompression(UnsafeMutablePointer<NSBitmapImageRep.TIFFCompression>?, factor: UnsafeMutablePointer<Float>?)](nsbitmapimagerep/getcompression(_:factor:).md)
  Returns by indirection the bitmap image representation’s compression type and compression factor.
- [func setProperty(NSBitmapImageRep.PropertyKey, withValue: Any?)](nsbitmapimagerep/setproperty(_:withvalue:).md)
  Sets the specified property of the bitmap image representation to the specified value.
- [func value(forProperty: NSBitmapImageRep.PropertyKey) -> Any?](nsbitmapimagerep/value(forproperty:).md)
  Returns the value for the specified property.
- [NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/tiffcompression)*