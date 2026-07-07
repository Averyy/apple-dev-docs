# image

**Framework**: PaperKit  
**Kind**: property

The image content displayed by this markup.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var image: CGImage? { get async }
```

#### Discussion

Image content is shown scaled to fill.

This property is async because an in-memory `CGImage` is not always loaded from disk. The image property can be `nil` when streaming the data model and the image asset has not yet been received.

## See Also

- [func replaceImage(with: URL) throws](imagemarkup/replaceimage(with:)-10qzi.md)
  Replaces the contents of this image markup with an image file.
- [func replaceImage(with: CGImage)](imagemarkup/replaceimage(with:)-6eb53.md)
  Replaces the contents of this image markup with a `CGImage`.
- [var orientation: CGImagePropertyOrientation](imagemarkup/orientation.md)
  The orientation of the image content.
- [var contentsBounds: CGRect](imagemarkup/contentsbounds.md)
  The portion of the image to display, in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/imagemarkup/image)*