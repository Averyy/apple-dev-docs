# compressionFactor

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Identifies an `NSNumber` object containing the compression factor of the image.

**Availability**:
- macOS

## Declaration

```swift
static let compressionFactor: NSBitmapImageRep.PropertyKey
```

```c
extern NSBitmapImageRepPropertyKey NSImageCompressionFactor;
```

#### Discussion

Used only for JPEG files. JPEG compression in TIFF files is not supported, and the factor is ignored. The value is a float between 0.0 and 1.0, with 1.0 resulting in no compression and 0.0 resulting in the maximum compression possible. It’s set when reading in and used when writing out the image.

## See Also

### Bitmap Properties
- [static let colorSyncProfileData: NSBitmapImageRep.PropertyKey](./colorsyncprofiledata.md)
  Identifies an `NSData` object containing the ColorSync profile data.
- [static let compressionMethod: NSBitmapImageRep.PropertyKey](./compressionmethod.md)
  Identifies an `NSNumber` object identifying the compression method of the image.
- [static let currentFrame: NSBitmapImageRep.PropertyKey](./currentframe.md)
  Identifies an `NSNumber` object containing the current frame for an animated GIF file.
- [static let currentFrameDuration: NSBitmapImageRep.PropertyKey](./currentframeduration.md)
  Identifies an `NSNumber` object containing the duration (in seconds) of the current frame for an animated GIF image.
- [static let ditherTransparency: NSBitmapImageRep.PropertyKey](./dithertransparency.md)
  Identifies an `NSNumber` object containing a Boolean that indicates whether the image is dithered.
- [static let exifData: NSBitmapImageRep.PropertyKey](./exifdata.md)
  Identifies an `NSDictionary` object containing the EXIF data for the image.
- [static let fallbackBackgroundColor: NSBitmapImageRep.PropertyKey](./fallbackbackgroundcolor.md)
  Specifies the background color to use when writing to an image format (such as JPEG) that doesn’t support alpha.
- [static let frameCount: NSBitmapImageRep.PropertyKey](./framecount.md)
  Identifies an `NSNumber` object containing the number of frames in an animated GIF file.
- [static let gamma: NSBitmapImageRep.PropertyKey](./gamma.md)
  Identifies an `NSNumber` object containing the gamma value for the image.
- [static let interlaced: NSBitmapImageRep.PropertyKey](./interlaced.md)
  Identifies an `NSNumber` object containing a Boolean value that indicates whether the image is interlaced.
- [static let loopCount: NSBitmapImageRep.PropertyKey](./loopcount.md)
  Identifies an `NSNumber` object containing the number of loops to make when animating a GIF image.
- [static let progressive: NSBitmapImageRep.PropertyKey](./progressive.md)
  Identifies an `NSNumber` object containing a Boolean that indicates whether the image uses progressive encoding.
- [static let rgbColorTable: NSBitmapImageRep.PropertyKey](./rgbcolortable.md)
  Identifies an `NSData` object containing the RGB color table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsbitmapimagerep/propertykey/compressionfactor)*