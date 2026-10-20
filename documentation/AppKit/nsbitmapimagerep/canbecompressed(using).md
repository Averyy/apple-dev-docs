# canBeCompressed(using:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Tests whether the bitmap image representation can be compressed by the specified compression scheme.

**Availability**:
- macOS

## Declaration

```swift
func canBeCompressed(using compression: NSBitmapImageRep.TIFFCompression) -> Bool
```

```objc
- (BOOL) canBeCompressedUsing:(NSTIFFCompression) compression;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver’s data matches `compression` with this type, [`false`](../../Swift/false.md) if the data doesn’t match `compression` or if `compression` is unsupported.

#### Discussion

This method returns [`true`](../../Swift/true.md) if the receiver’s data matches `compression`; for example, if `compression` is [`NSBitmapImageRep.TIFFCompression.ccittfax3`](./tiffcompression/ccittfax3.md), then the data must be 1 bit per sample and 1 sample per pixel.

## Parameters

- `compression`: A TIFF compression type. For more information, see the constants in [`NSBitmapImageRep.TIFFCompression`](./tiffcompression.md).

## See Also

### Managing Compression Types
- [class func getTIFFCompressionTypes(UnsafeMutablePointer<UnsafePointer<NSBitmapImageRep.TIFFCompression>?>, count: UnsafeMutablePointer<Int>)](./gettiffcompressiontypes%28_,count%29.md)
  Returns by indirection an array of all available compression types that can be used when writing a TIFF image.
- [class func localizedName(forTIFFCompressionType: NSBitmapImageRep.TIFFCompression) -> String?](./localizedname%28fortiffcompressiontype%29.md)
  Returns an autoreleased string containing the localized name for the specified compression type.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/canbecompressed(using:))*