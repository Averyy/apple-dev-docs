# NSBitmapImageRep.PropertyKey

**Framework**: AppKit  
**Kind**: struct

Constants that identify bitmap image representation properties.

**Availability**:
- macOS ?+

## Declaration

```swift
struct PropertyKey
```

#### Discussion

Use these constants with [`representationOfImageReps(in:using:properties:)`](nsbitmapimagerep/representationofimagereps(in:using:properties:).md), [`representation(using:properties:)`](nsbitmapimagerep/representation(using:properties:).md), [`setPixel(_:atX:y:)`](nsbitmapimagerep/setpixel(_:atx:y:).md), and [`value(forProperty:)`](nsbitmapimagerep/value(forproperty:).md).

When using the [`value(forProperty:)`](nsbitmapimagerep/value(forproperty:).md) method to retrieve the the value for any of these keys, be sure to check that the returned value is non-`nil` before you attempt to use it. A bitmap image representation may return `nil` for any values that have not yet been set.

## Topics

### Bitmap Properties
- [static let colorSyncProfileData: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/colorsyncprofiledata.md)
  Identifies an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing the ColorSync profile data.
- [static let compressionFactor: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/compressionfactor.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the compression factor of the image.
- [static let compressionMethod: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/compressionmethod.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object identifying the compression method of the image.
- [static let currentFrame: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/currentframe.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the current frame for an animated GIF file.
- [static let currentFrameDuration: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/currentframeduration.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the duration (in seconds) of the current frame for an animated GIF image.
- [static let ditherTransparency: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/dithertransparency.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean that indicates whether the image is dithered.
- [static let exifData: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/exifdata.md)
  Identifies an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) object containing the EXIF data for the image.
- [static let fallbackBackgroundColor: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/fallbackbackgroundcolor.md)
  Specifies the background color to use when writing to an image format (such as JPEG) that doesn’t support alpha. The color’s alpha value is ignored. The default background color, when this property is not specified, is white. The value of the property should be an [`NSColor`](nscolor.md) object. This constant corresponds to the kCGImageDestinationBackgroundColor constant in Quartz.
- [static let frameCount: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/framecount.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the number of frames in an animated GIF file.
- [static let gamma: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/gamma.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the gamma value for the image.
- [static let interlaced: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/interlaced.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean value that indicates whether the image is interlaced.
- [static let loopCount: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/loopcount.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the number of loops to make when animating a GIF image.
- [static let progressive: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/progressive.md)
  Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean that indicates whether the image uses progressive encoding.
- [static let rgbColorTable: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/rgbcolortable.md)
  Identifies an [`NSData`](https://developer.apple.com/documentation/Foundation/NSData) object containing the RGB color table.
### Initializers
- [init(String)](nsbitmapimagerep/propertykey/init(_:).md)
- [init(rawValue: String)](nsbitmapimagerep/propertykey/init(rawvalue:).md)
### Type Properties
- [static let imageIPTCData: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/imageiptcdata.md)
- [static let imageIPTCData: NSBitmapImageRep.PropertyKey](nsbitmapimagerep/propertykey/imageiptcdata.md)

## Relationships

### Conforms To
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
- [NSBitmapImageRep.TIFFCompression](nsbitmapimagerep/tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/propertykey)*