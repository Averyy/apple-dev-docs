# NSBitmapImageRep.PropertyKey

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants that identify bitmap image representation properties.

**Availability**:
- macOS

## Declaration

```swift
struct PropertyKey
```

```c
typedef NSString * NSBitmapImageRepPropertyKey;
```

## Discussion

Use these constants with [`representationOfImageReps(in:using:properties:)`](./representationofimagereps%28in,using,properties%29.md), [`representation(using:properties:)`](./representation%28using,properties%29.md), [`setPixel(_:atX:y:)`](./setpixel%28_,atx,y%29.md), and [`value(forProperty:)`](./value%28forproperty%29.md).

When using the [`value(forProperty:)`](./value%28forproperty%29.md) method to retrieve the the value for any of these keys, be sure to check that the returned value is non-`nil` before you attempt to use it. A bitmap image representation may return `nil` for any values that have not yet been set.

## Topics

### Bitmap Properties
- [static let colorSyncProfileData: NSBitmapImageRep.PropertyKey](./propertykey/colorsyncprofiledata.md)
  Identifies an `NSData` object containing the ColorSync profile data.
- [static let compressionFactor: NSBitmapImageRep.PropertyKey](./propertykey/compressionfactor.md)
  Identifies an `NSNumber` object containing the compression factor of the image.
- [static let compressionMethod: NSBitmapImageRep.PropertyKey](./propertykey/compressionmethod.md)
  Identifies an `NSNumber` object identifying the compression method of the image.
- [static let currentFrame: NSBitmapImageRep.PropertyKey](./propertykey/currentframe.md)
  Identifies an `NSNumber` object containing the current frame for an animated GIF file.
- [static let currentFrameDuration: NSBitmapImageRep.PropertyKey](./propertykey/currentframeduration.md)
  Identifies an `NSNumber` object containing the duration (in seconds) of the current frame for an animated GIF image.
- [static let ditherTransparency: NSBitmapImageRep.PropertyKey](./propertykey/dithertransparency.md)
  Identifies an `NSNumber` object containing a Boolean that indicates whether the image is dithered.
- [static let exifData: NSBitmapImageRep.PropertyKey](./propertykey/exifdata.md)
  Identifies an `NSDictionary` object containing the EXIF data for the image.
- [static let fallbackBackgroundColor: NSBitmapImageRep.PropertyKey](./propertykey/fallbackbackgroundcolor.md)
  Specifies the background color to use when writing to an image format (such as JPEG) that doesn’t support alpha.
- [static let frameCount: NSBitmapImageRep.PropertyKey](./propertykey/framecount.md)
  Identifies an `NSNumber` object containing the number of frames in an animated GIF file.
- [static let gamma: NSBitmapImageRep.PropertyKey](./propertykey/gamma.md)
  Identifies an `NSNumber` object containing the gamma value for the image.
- [static let interlaced: NSBitmapImageRep.PropertyKey](./propertykey/interlaced.md)
  Identifies an `NSNumber` object containing a Boolean value that indicates whether the image is interlaced.
- [static let loopCount: NSBitmapImageRep.PropertyKey](./propertykey/loopcount.md)
  Identifies an `NSNumber` object containing the number of loops to make when animating a GIF image.
- [static let progressive: NSBitmapImageRep.PropertyKey](./propertykey/progressive.md)
  Identifies an `NSNumber` object containing a Boolean that indicates whether the image uses progressive encoding.
- [static let rgbColorTable: NSBitmapImageRep.PropertyKey](./propertykey/rgbcolortable.md)
  Identifies an `NSData` object containing the RGB color table.
### Initializers
- [init(String)](./propertykey/init%28_%29.md)
- [init(rawValue: String)](./propertykey/init%28rawvalue%29.md)
### Type Properties
- [static let imageIPTCData: NSBitmapImageRep.PropertyKey](./propertykey/imageiptcdata.md)
- [static let imageIPTCData: NSBitmapImageRep.PropertyKey](./propertykey/imageiptcdata.md)

## Relationships

### Conforms To
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
- [NSBitmapImageRep.TIFFCompression](./tiffcompression.md)
  Constants that represent the supported TIFF data-compression schemes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/propertykey)*