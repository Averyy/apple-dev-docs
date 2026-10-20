# availableEmbeddedThumbnailPhotoCodecTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var availableEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * availableEmbeddedThumbnailPhotoCodecTypes;
```

#### Discussion

To enable embedding thumbnail images in photo file output, set the [`embeddedThumbnailPhotoFormat`](./embeddedthumbnailphotoformat.md) property using one of the codec types listed in this array.

The order of this array is such that the most backward-compatible codec is listed first.

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
- [var rawEmbeddedThumbnailPhotoFormat: [String : Any]?](./rawembeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/availableembeddedthumbnailphotocodectypes)*