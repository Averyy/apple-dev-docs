# getTIFFCompressionTypes(_:count:)

**Framework**: AppKit  
**Kind**: method

Returns by indirection an array of all available compression types that can be used when writing a TIFF image.

**Availability**:
- macOS ?+

## Declaration

```swift
class func getTIFFCompressionTypes(_ list: UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count numTypes: UnsafeMutablePointer<Int>)
```

#### Discussion

Note that not all compression types can be used for all images: [`NSBitmapImageRep.TIFFCompression.next`](nsbitmapimagerep/tiffcompression/next.md) can be used only to retrieve image data. Because future releases may include other compression types, always use this method to get the available compression types—for example, when you implement a user interface for selecting compression types.

## Parameters

- `list`: On return, a C array of   constants. This array belongs to the   class; it shouldn’t be freed or altered. See   for the supported TIFF compression types.
- `numTypes`: The number of constants in list.

## See Also

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
- [NSBitmapImageRep.TIFFCompression](nsbitmapimagerep/tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.
- [NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/gettiffcompressiontypes(_:count:))*