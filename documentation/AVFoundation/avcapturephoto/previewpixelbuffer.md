# previewPixelBuffer

**Framework**: AVFoundation  
**Kind**: property

The pixel data for a preview-sized version of the photo, if requested.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var previewPixelBuffer: CVPixelBuffer? { get }
```

## Mentions

- [Capturing thumbnail and preview images](capturing-thumbnail-and-preview-images.md)

#### Discussion

If you requested a preview image by specifying the [`previewPhotoFormat`](avcapturephotosettings/previewphotoformat.md) property of your photo settings when requesting capture, this property offers access to the resulting preview image pixel data. The pixel buffer contains only the minimal attachments required for correct display. If you did not request a preview image, this property’s value is `nil`.

## See Also

- [var embeddedThumbnailPhotoFormat: [String : Any]?](avcapturephoto/embeddedthumbnailphotoformat.md)
  A dictionary describing the data format for a preview-sized image accompanying the captured photo.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/previewpixelbuffer)*