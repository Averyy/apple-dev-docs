# setCompression(_:factor:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the bitmap image representation’s compression type and compression factor.

**Availability**:
- macOS

## Declaration

```swift
func setCompression(_ compression: NSBitmapImageRep.TIFFCompression, factor: Float)
```

```objc
- (void) setCompression:(NSTIFFCompression) compression factor:(float) factor;
```

#### Discussion

When an [`NSBitmapImageRep`](../nsbitmapimagerep.md) is created, the instance stores the compression type and factor for the source data. The [`tiffRepresentation`](./tiffrepresentation.md) property and [`tiffRepresentationOfImageReps(in:)`](./tiffrepresentationofimagereps%28in%29.md) class method try to use the stored compression type and factor. Use this method to change the compression type and factor.

## Parameters

- `compression`: An `enum` constant that identifies one of the supported compression types as described in [`NSBitmapImageRep.TIFFCompression`](./tiffcompression.md).
- `factor`: A floating point value that is specific to the compression type. Many types of compression don’t support varying degrees of compression and thus ignore `factor`. JPEG compression allows a compression factor ranging from 0.0 to 1.0, with 0.0 being the lowest and 1.0 being the highest.

## See Also

### Managing Compression Types
- [class func getTIFFCompressionTypes(UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count: UnsafeMutablePointer<Int>)](./gettiffcompressiontypes%28_,count%29.md)
  Returns by indirection an array of all available compression types that can be used when writing a TIFF image.
- [class func localizedName(forTIFFCompressionType: NSBitmapImageRep.TIFFCompression) -> String?](./localizedname%28fortiffcompressiontype%29.md)
  Returns an autoreleased string containing the localized name for the specified compression type.
- [func canBeCompressed(using: NSBitmapImageRep.TIFFCompression) -> Bool](./canbecompressed%28using%29.md)
  Tests whether the bitmap image representation can be compressed by the specified compression scheme.
- [func getCompression(UnsafeMutablePointer<NSBitmapImageRep.TIFFCompression>?, factor: UnsafeMutablePointer<Float>?)](./getcompression%28_,factor%29.md)
  Returns by indirection the bitmap image representation’s compression type and compression factor.
- [func setProperty(NSBitmapImageRep.PropertyKey, withValue: Any?)](./setproperty%28_,withvalue%29.md)
  Sets the specified property of the bitmap image representation to the specified value.
- [func value(forProperty: NSBitmapImageRep.PropertyKey) -> Any?](./value%28forproperty%29.md)
  Returns the value for the specified property.
- [NSBitmapImageRep.TIFFCompression](./tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.
- [NSBitmapImageRep.PropertyKey](./propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/setcompression(_:factor:))*