# scale

**Framework**: UIKit  
**Kind**: property

The display scale of the image renderer context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var scale: CGFloat { get set }
```

#### Discussion

The display scale determines the number of pixels per point.

The default value is equal to the [`scale`](uiscreen/scale.md) of the main screen.

## See Also

- [var opaque: Bool](uigraphicsimagerendererformat/opaque.md)
  A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/preferredrange.md)
  The preferred color range of the image renderer context.
- [UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/range.md)
  Constants that specify the color range of the image renderer context.
- [var prefersExtendedRange: Bool](uigraphicsimagerendererformat/prefersextendedrange.md)
  A Boolean value that specifies whether the bitmap context uses extended color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/scale)*