# setProperty(_:withValue:)

**Framework**: AppKit  
**Kind**: method

Sets the specified property of the bitmap image representation to the specified value.

**Availability**:
- macOS ?+

## Declaration

```swift
func setProperty(_ property: NSBitmapImageRep.PropertyKey, withValue value: Any?)
```

#### Discussion

The properties can affect how the image is read in and saved to file.

## Parameters

- `property`: A string constant used as a key for an image property. These properties are described in  .
- `value`: A value specific to  . If   is  , the value of the property is cleared.

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
- [func value(forProperty: NSBitmapImageRep.PropertyKey) -> Any?](nsbitmapimagerep/value(forproperty:).md)
  Returns the value for the specified property.
- [NSBitmapImageRep.TIFFCompression](nsbitmapimagerep/tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.
- [NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/setproperty(_:withvalue:))*