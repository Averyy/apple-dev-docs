# rawFileType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The container file format for eventual output of the RAW image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var rawFileType: AVFileType? { get }
```

```objc
@property (readonly, nullable) AVFileType rawFileType;
```

## Discussion

You specify a file format when creating capture settings with the [`init(rawPixelFormatType:rawFileType:processedFormat:processedFileType:)`](./init%28rawpixelformattype,rawfiletype,processedformat,processedfiletype%29.md) initializer. If you didn’t specify a file format, this value is `nil`, and the photo output automatically choosea a default file format appropriate to the [`rawPhotoPixelFormatType`](./rawphotopixelformattype.md) property.

## See Also

### Inspecting settings
- [var uniqueID: Int64](./uniqueid.md)
  A unique identifier for this photo settings instance.
- [var format: [String : Any]?](./format.md)
  A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [var processedFileType: AVFileType?](./processedfiletype.md)
  The container file format for eventual output of the processed image.
- [var rawPhotoPixelFormatType: OSType](./rawphotopixelformattype.md)
  An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/rawfiletype)*