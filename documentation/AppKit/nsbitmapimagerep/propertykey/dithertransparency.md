# ditherTransparency

**Framework**: AppKit  
**Kind**: property

Identifies an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing a Boolean that indicates whether the image is dithered.

**Availability**:
- macOS ?+

## Declaration

```swift
static let ditherTransparency: NSBitmapImageRep.PropertyKey
```

#### Discussion

Used only when writing GIF files.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/propertykey/dithertransparency)*