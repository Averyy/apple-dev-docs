# availablePreviewPhotoPixelFormatTypes

**Framework**: AVFoundation  
**Kind**: property

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

- [var previewPhotoFormat: [String : Any]?](avcapturephotosettings/previewphotoformat.md)
  A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [var embeddedThumbnailPhotoFormat: [String : Any]?](avcapturephotosettings/embeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [var availableRawEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](avcapturephotosettings/availablerawembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [var rawEmbeddedThumbnailPhotoFormat: [String : Any]?](avcapturephotosettings/rawembeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
- [var availableEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](avcapturephotosettings/availableembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/availablepreviewphotopixelformattypes-30d9)*