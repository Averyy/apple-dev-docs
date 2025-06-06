# processedFileType

**Framework**: AVFoundation  
**Kind**: property

The container file format for eventual output of the processed image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var processedFileType: AVFileType? { get }
```

#### Discussion

You specify a file format when creating capture settings with the [`init(rawPixelFormatType:rawFileType:processedFormat:processedFileType:)`](avcapturephotosettings/init(rawpixelformattype:rawfiletype:processedformat:processedfiletype:).md) initializer. If you didn’t specify a file format, this value is `nil`, and the photo output automatically chooses a default file format appropriate to the [`format`](avcapturephotosettings/format.md) property.

## See Also

- [var uniqueID: Int64](avcapturephotosettings/uniqueid.md)
  A unique identifier for this photo settings instance.
- [var format: [String : Any]?](avcapturephotosettings/format.md)
  A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [var rawFileType: AVFileType?](avcapturephotosettings/rawfiletype.md)
  The container file format for eventual output of the RAW image.
- [var rawPhotoPixelFormatType: OSType](avcapturephotosettings/rawphotopixelformattype.md)
  An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/processedfiletype)*