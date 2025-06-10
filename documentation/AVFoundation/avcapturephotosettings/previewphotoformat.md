# previewPhotoFormat

**Framework**: AVFoundation  
**Kind**: property

A dictionary describing the format for delivery of preview-sized images alongside the main photo.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var previewPhotoFormat: [String : Any]? { get set }
```

## Mentions

- [Capturing Thumbnail and Preview Images](capturing-thumbnail-and-preview-images.md)

#### Discussion

By default, this property is `nil`, specifying that the photo output should return only the main image requested. To also receive a preview-sized image, set this property to a dictionary describing the format for that image, containing the following keys and values:

The dictionary must contain the [`kCVPixelBufferPixelFormatTypeKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferPixelFormatTypeKey) key, whose corresponding value must be one of the pixel format types listed in the [`availablePreviewPhotoPixelFormatTypes`](avcapturephotosettings/availablepreviewphotopixelformattypes-2vfwu.md) array.

Optionally, you can also include the [`kCVPixelBufferWidthKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferWidthKey) and [`kCVPixelBufferHeightKey`](https://developer.apple.com/documentation/CoreVideo/kCVPixelBufferHeightKey) keys to specify the size of the preview image. (If you specify either width or height, you must specify both.) If the size you specify does not match the aspect ratio of the primary photo, the photo output provides a preview image whose size matches the longer of the two specified dimensions, preserving the original aspect ratio.

> **Note**:  The photo capture system supports both  and  images as companions to the full-size primary image in a photo capture. A preview image is intended for immediate display (as seen when taking photos in the iOS Camera app), and as such is sized for full-screen presentation on the current device. A thumbnail image is intended for embedding in the output image file and can be used by other software (such as Quick Look in a file browser) to allow users to quickly review the image without loading the entire image file; the size of thumbnail images may be limited depending on the output file format.

## See Also

- [var availablePreviewPhotoPixelFormatTypes: [OSType]](avcapturephotosettings/availablepreviewphotopixelformattypes-30d9.md)
  An array of available of pixel format types available to specify a preview photo format.
- [var embeddedThumbnailPhotoFormat: [String : Any]?](avcapturephotosettings/embeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [var availableRawEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](avcapturephotosettings/availablerawembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [var rawEmbeddedThumbnailPhotoFormat: [String : Any]?](avcapturephotosettings/rawembeddedthumbnailphotoformat.md)
  A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
- [var availableEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType]](avcapturephotosettings/availableembeddedthumbnailphotocodectypes.md)
  An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/previewphotoformat)*