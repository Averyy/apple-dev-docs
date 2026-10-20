# availablePreviewPhotoPixelFormatTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of available of pixel format types available to specify a preview photo format.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 17.0+

## Declaration

```swift
@nonobjc
var availablePreviewPhotoPixelFormatTypes: [OSType] { get }
```

#### Discussion

The array is sorted so that preview formats requiring fewer conversions come first.

## See Also

### Enabling preview and thumbnail delivery
- [var previewPhotoFormat: [String : Any]?](./previewphotoformat.md)
  A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [var embeddedThumbnailPhotoFormat: [String : Any]?](./embeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [var availableRawEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](./availablerawembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [var rawEmbeddedThumbnailPhotoFormat: [String : Any]?](./rawembeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
- [var availableEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](./availableembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/availablepreviewphotopixelformattypes-30d9)*