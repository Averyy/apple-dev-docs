# UIGraphicsImageRendererFormat.Range

**Framework**: UIKit  
**Kind**: enum

Constants that specify the color range of the image renderer context.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum Range
```

## Topics

### Constants
- [UIGraphicsImageRendererFormat.Range.automatic](uigraphicsimagerendererformat/range/automatic.md)
  The system automatically chooses the image renderer context’s pixel format according to the color range of its content.
- [UIGraphicsImageRendererFormat.Range.extended](uigraphicsimagerendererformat/range/extended.md)
  The image renderer context supports wide color.
- [UIGraphicsImageRendererFormat.Range.standard](uigraphicsimagerendererformat/range/standard.md)
  The image renderer context doesn’t support extended colors.
- [UIGraphicsImageRendererFormat.Range.unspecified](uigraphicsimagerendererformat/range/unspecified.md)
  The image renderer context doesn’t specify a color range.
### Initializers
- [init?(rawValue: Int)](uigraphicsimagerendererformat/range/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var opaque: Bool](uigraphicsimagerendererformat/opaque.md)
  A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [var scale: CGFloat](uigraphicsimagerendererformat/scale.md)
  The display scale of the image renderer context.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/preferredrange.md)
  The preferred color range of the image renderer context.
- [var prefersExtendedRange: Bool](uigraphicsimagerendererformat/prefersextendedrange.md)
  A Boolean value that specifies whether the bitmap context uses extended color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/range)*