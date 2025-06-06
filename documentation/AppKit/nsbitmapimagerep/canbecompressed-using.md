# canBeCompressed(using:)

**Framework**: AppKit  
**Kind**: method

Tests whether the bitmap image representation can be compressed by the specified compression scheme.

**Availability**:
- macOS ?+

## Declaration

```swift
func canBeCompressed(using compression: NSBitmapImageRep.TIFFCompression) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver’s data matches `compression` with this type, [`false`](https://developer.apple.com/documentation/swift/false) if the data doesn’t match `compression` or if `compression` is unsupported.

#### Discussion

This method returns [`true`](https://developer.apple.com/documentation/swift/true) if the receiver’s data matches `compression`; for example, if `compression` is [`NSBitmapImageRep.TIFFCompression.ccittfax3`](nsbitmapimagerep/tiffcompression/ccittfax3.md), then the data must be 1 bit per sample and 1 sample per pixel.

## Parameters

- `compression`: A TIFF compression type. For more information, see the constants in  .

## See Also

- [class func getTIFFCompressionTypes(UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count: UnsafeMutablePointer<Int>)](nsbitmapimagerep/gettiffcompressiontypes(_:count:).md)
  Returns by indirection an array of all available compression types that can be used when writing a TIFF image.
- [class func localizedName(forTIFFCompressionType: NSBitmapImageRep.TIFFCompression) -> String?](nsbitmapimagerep/localizedname(fortiffcompressiontype:).md)
  Returns an autoreleased string containing the localized name for the specified compression type.
- [func setCompression(NSBitmapImageRep.TIFFCompression, factor: Float)](nsbitmapimagerep/setcompression(_:factor:).md)
  Sets the bitmap image representation’s compression type and compression factor.
- [func getCompression(UnsafeMutablePointer<NSBitmapImageRep.TIFFCompression>?, factor: UnsafeMutablePointer<Float>?)](nsbitmapimagerep/getcompression(_:factor:).md)
  Returns by indirection the bitmap image representation’s compression type and compression factor.
- [func setProperty(NSBitmapImageRep.PropertyKey, withValue: Any?)](nsbitmapimagerep/setproperty(_:withvalue:).md)
  Sets the specified property of the bitmap image representation to the specified value.
- [func value(forProperty: NSBitmapImageRep.PropertyKey) -> Any?](nsbitmapimagerep/value(forproperty:).md)
  Returns the value for the specified property.
- [NSBitmapImageRep.TIFFCompression](nsbitmapimagerep/tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.
- [NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/canbecompressed(using:))*