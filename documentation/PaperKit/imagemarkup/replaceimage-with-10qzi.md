# replaceImage(with:)

**Framework**: PaperKit  
**Kind**: method

Replaces the contents of this image markup with an image file.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func replaceImage(with url: URL) throws
```

#### Discussion

> **Note**: An error if the image file cannot be loaded or is in an unsupported format.

Image content is shown scaled to fill.

## Parameters

- `url`: The URL of the image file to load and display.

## See Also

- [var image: CGImage?](imagemarkup/image.md)
  The image content displayed by this markup.
- [func replaceImage(with: CGImage)](imagemarkup/replaceimage(with:)-6eb53.md)
  Replaces the contents of this image markup with a `CGImage`.
- [var orientation: CGImagePropertyOrientation](imagemarkup/orientation.md)
  The orientation of the image content.
- [var contentsBounds: CGRect](imagemarkup/contentsbounds.md)
  The portion of the image to display, in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/imagemarkup/replaceimage(with:)-10qzi)*