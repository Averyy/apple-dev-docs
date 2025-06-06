# embeddedThumbnailPhotoFormat

**Framework**: AVFoundation  
**Kind**: property

A dictionary describing the data format for a preview-sized image accompanying the captured photo.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var embeddedThumbnailPhotoFormat: [String : Any]? { get }
```

#### Discussion

See [`Video settings`](video-settings.md) for possible keys and values.

If you requested an embedded thumbnail image by specifying the [`embeddedThumbnailPhotoFormat`](avcapturephotosettings/embeddedthumbnailphotoformat.md) property of your photo settings when requesting capture, this property’s value is the resolved video settings dictionary for the embedded thumbnail image. If you did not request an embedded thumbnail image, this property’s value is `nil`.

## See Also

- [var previewPixelBuffer: CVPixelBuffer?](avcapturephoto/previewpixelbuffer.md)
  The pixel data for a preview-sized version of the photo, if requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/embeddedthumbnailphotoformat)*