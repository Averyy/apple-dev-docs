# rawPhotoPixelFormatType

**Framework**: AVFoundation  
**Kind**: property

An identifier for the Bayer RAW pixel format to deliver captured RAW photos in.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var rawPhotoPixelFormatType: OSType { get }
```

#### Discussion

This property is read-only—you specify a RAW pixel format when creating a settings object with the [`init(rawPixelFormatType:)`](avcapturephotosettings/init(rawpixelformattype:).md), [`init(rawPixelFormatType:processedFormat:)`](avcapturephotosettings/init(rawpixelformattype:processedformat:).md) initializer.

When capturing RAW images, the following requirements apply:

- The [`isAutoStillImageStabilizationEnabled`](avcapturephotosettings/isautostillimagestabilizationenabled.md) setting must be [`false`](https://developer.apple.com/documentation/swift/false).
- Your delegate object must implement the [`photoOutput(_:didFinishProcessingRawPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)`](avcapturephotocapturedelegate/photooutput(_:didfinishprocessingrawphoto:previewphoto:resolvedsettings:bracketsettings:error:).md) method.
- The [`isHighResolutionPhotoEnabled`](avcapturephotosettings/ishighresolutionphotoenabled.md) setting may be [`true`](https://developer.apple.com/documentation/swift/true) or [`false`](https://developer.apple.com/documentation/swift/false), but that setting applies only to the separate processed image.

(You request separate processed images with the [`init(rawPixelFormatType:processedFormat:)`](avcapturephotosettings/init(rawpixelformattype:processedformat:).md) initializer. This restriction does not apply when you request RAW-only capture with the [`init(rawPixelFormatType:)`](avcapturephotosettings/init(rawpixelformattype:).md) initializer).

The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method. If your settings and delegate do not meet these requirements, that method raises an exception.

## See Also

- [var uniqueID: Int64](avcapturephotosettings/uniqueid.md)
  A unique identifier for this photo settings instance.
- [var format: [String : Any]?](avcapturephotosettings/format.md)
  A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [var processedFileType: AVFileType?](avcapturephotosettings/processedfiletype.md)
  The container file format for eventual output of the processed image.
- [var rawFileType: AVFileType?](avcapturephotosettings/rawfiletype.md)
  The container file format for eventual output of the RAW image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/rawphotopixelformattype)*