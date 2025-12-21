# pixelBuffer

**Framework**: AVFoundation  
**Kind**: property

The uncompressed or RAW image sample buffer for the photo, if requested.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+

## Declaration

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

## Mentions

- [Capturing uncompressed image data](capturing-uncompressed-image-data.md)

#### Discussion

If you requested photo capture in a RAW format, or in a processed format without compression such as TIFF, you can use this property to access the underlying sample buffer.

If you requested capture in a compressed format such as JPEG or HEVC/HEIF, this property’s value is `nil`. Use the [`fileDataRepresentation()`](avcapturephoto/filedatarepresentation().md) or [`cgImageRepresentation()`](avcapturephoto/cgimagerepresentation().md) method to obtain compressed image data.

## See Also

- [var isRawPhoto: Bool](avcapturephoto/israwphoto.md)
  A Boolean value indicating whether this photo object contains RAW format data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/pixelbuffer)*