# rawPhotoPixelFormatType

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) OSType rawPhotoPixelFormatType;
```

## Discussion

This property is read-only—you specify a RAW pixel format when creating a settings object with the [`init(rawPixelFormatType:)`](./init%28rawpixelformattype%29.md), [`init(rawPixelFormatType:processedFormat:)`](./init%28rawpixelformattype,processedformat%29.md) initializer.

When capturing RAW images, the following requirements apply:

- The [`isAutoStillImageStabilizationEnabled`](./isautostillimagestabilizationenabled.md) setting must be [`false`](../../Swift/false.md).
- Your delegate object must implement the [`photoOutput(_:didFinishProcessingRawPhoto:previewPhoto:resolvedSettings:bracketSettings:error:)`](../avcapturephotocapturedelegate/photooutput%28_,didfinishprocessingrawphoto,previewphoto,resolvedsettings,bracketsettings,error%29.md) method.
- The [`isHighResolutionPhotoEnabled`](./ishighresolutionphotoenabled.md) setting may be [`true`](../../Swift/true.md) or [`false`](../../Swift/false.md), but that setting applies only to the separate processed image.

(You request separate processed images with the [`init(rawPixelFormatType:processedFormat:)`](./init%28rawpixelformattype,processedformat%29.md) initializer. This restriction does not apply when you request RAW-only capture with the [`init(rawPixelFormatType:)`](./init%28rawpixelformattype%29.md) initializer).

The capture output validates these requirements when you call the [`capturePhoto(with:delegate:)`](../avcapturephotooutput/capturephoto%28with,delegate%29.md) method. If your settings and delegate do not meet these requirements, that method raises an exception.

## See Also

### Inspecting settings
- [var uniqueID: Int64](./uniqueid.md)
  A unique identifier for this photo settings instance.
- [var format: [String : Any]?](./format.md)
  A dictionary describing the processed format (for example, JPEG) to deliver captured photos in.
- [var processedFileType: AVFileType?](./processedfiletype.md)
  The container file format for eventual output of the processed image.
- [var rawFileType: AVFileType?](./rawfiletype.md)
  The container file format for eventual output of the RAW image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/rawphotopixelformattype)*