# replaceImage(with:)

**Framework**: PaperKit  
**Kind**: method

Replaces the contents of this image markup with a `CGImage`.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func replaceImage(with image: CGImage)
```

#### Discussion

Image content is shown scaled to fill.

## Parameters

- `image`: The new image to display.

## See Also

- [var image: CGImage?](imagemarkup/image.md)
  The image content displayed by this markup.
- [func replaceImage(with: URL) throws](imagemarkup/replaceimage(with:)-10qzi.md)
  Replaces the contents of this image markup with an image file.
- [var orientation: CGImagePropertyOrientation](imagemarkup/orientation.md)
  The orientation of the image content.
- [var contentsBounds: CGRect](imagemarkup/contentsbounds.md)
  The portion of the image to display, in normalized coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/imagemarkup/replaceimage(with:)-6eb53)*