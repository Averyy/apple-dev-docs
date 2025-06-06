# localizedName(forTIFFCompressionType:)

**Framework**: AppKit  
**Kind**: method

Returns an autoreleased string containing the localized name for the specified compression type.

**Availability**:
- macOS ?+

## Declaration

```swift
class func localizedName(forTIFFCompressionType compression: NSBitmapImageRep.TIFFCompression) -> String?
```

#### Return Value

A localized name for `compression` or `nil` if `compression` is unrecognized.

#### Discussion

When implementing a user interface for selecting TIFF compression types, use [`getTIFFCompressionTypes(_:count:)`](nsbitmapimagerep/gettiffcompressiontypes(_:count:).md) to get the list of supported compression types, then use this method to get the localized names for each compression type.

## Parameters

- `compression`: A TIFF compression type. For more information, see the constants in  .

## See Also

- [class func getTIFFCompressionTypes(UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count: UnsafeMutablePointer<Int>)](nsbitmapimagerep/gettiffcompressiontypes(_:count:).md)
  Returns by indirection an array of all available compression types that can be used when writing a TIFF image.
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
- [NSBitmapImageRep.TIFFCompression](nsbitmapimagerep/tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.
- [NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/localizedname(fortiffcompressiontype:))*