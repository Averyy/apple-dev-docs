# getTIFFCompressionTypes(_:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns by indirection an array of all available compression types that can be used when writing a TIFF image.

**Availability**:
- macOS

## Declaration

```swift
class func getTIFFCompressionTypes(_ list: UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count numTypes: UnsafeMutablePointer<Int>)
```

```objc
+ (void) getTIFFCompressionTypes:(const NSTIFFCompression **) list count:(NSInteger *) numTypes;
```

#### Discussion

Note that not all compression types can be used for all images: [`NSBitmapImageRep.TIFFCompression.next`](./tiffcompression/next.md) can be used only to retrieve image data. Because future releases may include other compression types, always use this method to get the available compression types—for example, when you implement a user interface for selecting compression types.

## Parameters

- `list`: On return, a C array of [`NSBitmapImageRep.TIFFCompression`](./tiffcompression.md) constants. This array belongs to the [`NSBitmapImageRep`](../nsbitmapimagerep.md) class; it shouldn’t be freed or altered. See [`NSBitmapImageRep.TIFFCompression`](./tiffcompression.md) for the supported TIFF compression types.
- `numTypes`: The number of constants in list.

## See Also

### Managing Compression Types
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
- [NSBitmapImageRep.TIFFCompression](./tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.
- [NSBitmapImageRep.PropertyKey](./propertykey.md)
  Constants that identify bitmap image representation properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/gettiffcompressiontypes(_:count:))*