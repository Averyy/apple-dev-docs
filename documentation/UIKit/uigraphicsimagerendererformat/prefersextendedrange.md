# prefersExtendedRange

**Framework**: UIKit  
**Kind**: property

A Boolean value that specifies whether the bitmap context uses extended color.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+

## Declaration

```swift
var prefersExtendedRange: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the underlying Core Graphics context is configured to support wide color; if [`false`](https://developer.apple.com/documentation/Swift/false), the context is not.

The default is [`true`](https://developer.apple.com/documentation/Swift/true) on devices that natively support wide color, and [`false`](https://developer.apple.com/documentation/Swift/false) on those that do not.

## See Also

- [var opaque: Bool](uigraphicsimagerendererformat/opaque.md)
  A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [var scale: CGFloat](uigraphicsimagerendererformat/scale.md)
  The display scale of the image renderer context.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/preferredrange.md)
  The preferred color range of the image renderer context.
- [UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/range.md)
  Constants that specify the color range of the image renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/prefersextendedrange)*