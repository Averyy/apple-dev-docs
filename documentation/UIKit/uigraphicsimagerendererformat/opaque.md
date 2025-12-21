# opaque

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var opaque: Bool { get set }
```

#### Discussion

Setting the value of this property to [`false`](https://developer.apple.com/documentation/Swift/false) specifies that the underlying Core Graphics context has an alpha channel, whereas [`true`](https://developer.apple.com/documentation/Swift/true) indicates it does not. The default value is [`false`](https://developer.apple.com/documentation/Swift/false).

A Core Graphics context requires an alpha channel to express transparency. Without an alpha channel a Core Graphics context is said to be opaque, i.e. without transparency.

## See Also

- [var scale: CGFloat](uigraphicsimagerendererformat/scale.md)
  The display scale of the image renderer context.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/preferredrange.md)
  The preferred color range of the image renderer context.
- [UIGraphicsImageRendererFormat.Range](uigraphicsimagerendererformat/range.md)
  Constants that specify the color range of the image renderer context.
- [var prefersExtendedRange: Bool](uigraphicsimagerendererformat/prefersextendedrange.md)
  A Boolean value that specifies whether the bitmap context uses extended color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/opaque)*