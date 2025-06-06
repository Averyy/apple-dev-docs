# UIGraphicsImageRendererFormat.Range.unspecified

**Framework**: UIKit  
**Kind**: case

The image renderer context doesn’t specify a color range.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case unspecified
```

#### Discussion

In general, avoid specifying this value for an image renderer format. Some color spaces that you access using the [`imageRendererFormat`](uiimage/imagerendererformat.md) property of [`UIImage`](uiimage.md) may use this value.

## See Also

- [UIGraphicsImageRendererFormat.Range.automatic](uigraphicsimagerendererformat/range/automatic.md)
  The system automatically chooses the image renderer context’s pixel format according to the color range of its content.
- [UIGraphicsImageRendererFormat.Range.extended](uigraphicsimagerendererformat/range/extended.md)
  The image renderer context supports wide color.
- [UIGraphicsImageRendererFormat.Range.standard](uigraphicsimagerendererformat/range/standard.md)
  The image renderer context doesn’t support extended colors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/range/unspecified)*