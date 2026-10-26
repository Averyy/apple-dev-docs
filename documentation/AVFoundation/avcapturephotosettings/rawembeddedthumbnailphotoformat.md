# rawEmbeddedThumbnailPhotoFormat

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var rawEmbeddedThumbnailPhotoFormat: [String : Any]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSDictionary<NSString *,id> * rawEmbeddedThumbnailPhotoFormat;
```

## Mentions

- [Capturing photos in RAW and Apple ProRAW formats](../capturing-photos-in-raw-and-apple-proraw-formats.md)

## See Also

### Enabling preview and thumbnail delivery
- [var previewPhotoFormat: [String : Any]?](./previewphotoformat.md)
  A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [var availablePreviewPhotoPixelFormatTypes: [OSType]](./availablepreviewphotopixelformattypes-30d9.md)
  An array of available of pixel format types available to specify a preview photo format.
- [var embeddedThumbnailPhotoFormat: [String : Any]?](./embeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [var availableRawEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](./availablerawembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [var availableEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](./availableembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.
- [availablePreviewPhotoPixelFormatTypes](./availablepreviewphotopixelformattypes-2vfwu.md)
  An array of pixel format types compatible with the photo settings for delivery of preview-sized images.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/rawembeddedthumbnailphotoformat)*