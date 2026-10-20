# NSBitmapImageRep.TIFFCompression

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that represent the supported TIFF data-compression schemes.

**Availability**:
- macOS

## Declaration

```swift
enum TIFFCompression
```

```c
enum NSTIFFCompression : NSUInteger;
```

## Topics

### Constants
- [NSBitmapImageRep.TIFFCompression.none](./tiffcompression/none.md)
  No compression.
- [NSBitmapImageRep.TIFFCompression.ccittfax3](./tiffcompression/ccittfax3.md)
  CCITT Fax Group 3 compression.
- [NSBitmapImageRep.TIFFCompression.ccittfax4](./tiffcompression/ccittfax4.md)
  CCITT Fax Group 4 compression.
- [NSBitmapImageRep.TIFFCompression.lzw](./tiffcompression/lzw.md)
  LZW compression.
- [NSBitmapImageRep.TIFFCompression.jpeg](./tiffcompression/jpeg.md)
  JPEG compression. No longer supported for input or output.
- [NSBitmapImageRep.TIFFCompression.next](./tiffcompression/next.md)
  NeXT compressed. Supported for input only.
- [NSBitmapImageRep.TIFFCompression.packBits](./tiffcompression/packbits.md)
  PackBits compression.
- [NSBitmapImageRep.TIFFCompression.oldJPEG](./tiffcompression/oldjpeg.md)
  Old JPEG compression. No longer supported for input or output.
### Initializers
- [init?(rawValue: UInt)](./tiffcompression/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Compression Types
- [class func getTIFFCompressionTypes(UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count: UnsafeMutablePointer<Int>)](./gettiffcompressiontypes%28_,count%29.md)
  Returns by indirection an array of all available compression types that can be used when writing a TIFF image.
- [class func localizedName(forTIFFCompressionType: NSBitmapImageRep.TIFFCompression) -> String?](./localizedname%28fortiffcompressiontype%29.md)
  Returns an autoreleased string containing the localized name for the specified compression type.
- [func canBeCompressed(using: NSBitmapImageRep.TIFFCompression) -> Bool](./canbecompressed%28using%29.md)
  Tests whether the bitmap image representation can be compressed by the specified compression scheme.
- [func setCompression(NSBitmapImageRep.TIFFCompression, factor: Float)](./setcompression%28_,factor%29.md)
  Sets the bitmap image representation’s compression type and compression factor.
- [func getCompression(UnsafeMutablePointer<NSBitmapImageRep.TIFFCompression>?, factor: UnsafeMutablePointer<Float>?)](./getcompression%28_,factor%29.md)
  Returns by indirection the bitmap image representation’s compression type and compression factor.
- [func setProperty(NSBitmapImageRep.PropertyKey, withValue: Any?)](./setproperty%28_,withvalue%29.md)
  Sets the specified property of the bitmap image representation to the specified value.
- [func value(forProperty: NSBitmapImageRep.PropertyKey) -> Any?](./value%28forproperty%29.md)
  Returns the value for the specified property.
- [NSBitmapImageRep.PropertyKey](./propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/tiffcompression)*