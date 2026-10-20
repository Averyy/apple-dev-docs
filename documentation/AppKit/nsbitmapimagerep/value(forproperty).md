# value(forProperty:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the value for the specified property.

**Availability**:
- macOS

## Declaration

```swift
func value(forProperty property: NSBitmapImageRep.PropertyKey) -> Any?
```

```objc
- (id) valueForProperty:(NSBitmapImageRepPropertyKey) property;
```

#### Return Value

A value specific to `property`, or `nil` if the property is not set for the bitmap.

#### Discussion

Image properties can affect how an image is read in and saved to file. When retrieving the bitmap image properties defined in [`NSBitmapImageRep.PropertyKey`](./propertykey.md), be sure to check the return value of this method for a `nil` value. If a particular value is not set for the image, this method may return `nil`.

## Parameters

- `property`: A string constant used as a key for an image property. These properties are described in [`NSBitmapImageRep.PropertyKey`](./propertykey.md).

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
- [NSBitmapImageRep.TIFFCompression](./tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.
- [NSBitmapImageRep.PropertyKey](./propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/value(forproperty:))*