# availablePreviewPhotoPixelFormatTypes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of pixel format types compatible with the photo settings for delivery of preview-sized images.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * availablePreviewPhotoPixelFormatTypes;
```

#### Discussion

To enable delivery of preview-sized images along with the main image captured by a photo output, set the [`previewPhotoFormat`](./previewphotoformat.md) property using one of the [`kCVPixelBufferPixelFormatTypeKey`](../../CoreVideo/kcvpixelbufferpixelformattypekey.md) values listed in this array.

The order of this array is such that the format requiring the least conversion is listed first.

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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/availablepreviewphotopixelformattypes-2vfwu)*