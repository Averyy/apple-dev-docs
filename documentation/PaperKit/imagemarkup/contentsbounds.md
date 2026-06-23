# contentsBounds

**Framework**: PaperKit  
**Kind**: property

The portion of the image to display, in normalized coordinates.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var contentsBounds: CGRect { get set }
```

#### Discussion

Values are normalized from `0.0` to `1.0`, where `(0, 0)` is the top-left and `(1, 1)` is the bottom-right of the source image. Defaults to `CGRect(x: 0, y: 0, width: 1, height: 1)` (full image).

## See Also

- [var image: CGImage?](imagemarkup/image.md)
  The image content displayed by this markup.
- [func replaceImage(with: URL) throws](imagemarkup/replaceimage(with:)-10qzi.md)
  Replaces the contents of this image markup with an image file.
- [func replaceImage(with: CGImage)](imagemarkup/replaceimage(with:)-6eb53.md)
  Replaces the contents of this image markup with a `CGImage`.
- [var orientation: CGImagePropertyOrientation](imagemarkup/orientation.md)
  The orientation of the image content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/imagemarkup/contentsbounds)*