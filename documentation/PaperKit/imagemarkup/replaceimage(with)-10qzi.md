# replaceImage(with:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method

Replaces the contents of this image markup with an image file.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func replaceImage(with url: URL) throws
```

## Discussion

> **Throws**: An error if the image file cannot be loaded or is in an unsupported format.

Image content is shown scaled to fill.

## Parameters

- `url`: The URL of the image file to load and display.

## See Also

### Accessing image content
- [var image: CGImage?](./image.md)
  The image content displayed by this markup.
- [func replaceImage(with: CGImage)](./replaceimage%28with%29-6eb53.md)
  Replaces the contents of this image markup with a `CGImage`.
- [var orientation: CGImagePropertyOrientation](./orientation.md)
  The orientation of the image content.
- [var contentsBounds: CGRect](./contentsbounds.md)
  The portion of the image to display, in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/imagemarkup/replaceimage(with:)-10qzi)*