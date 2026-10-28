# prefersExtendedRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether the bitmap context uses extended color.

**Availability**:
- iOS 10.0+ - Deprecated in 12.0
- iPadOS 10.0+ - Deprecated in 12.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS 10.0+ - Deprecated in 12.0

> **Deprecated**: Use [`preferredRange`](./preferredrange.md) instead.

## Declaration

```swift
var prefersExtendedRange: Bool { get set }
```

```objc
@property (nonatomic) BOOL prefersExtendedRange;
```

## Discussion

If [`true`](../../Swift/true.md), the underlying Core Graphics context is configured to support wide color; if [`false`](../../Swift/false.md), the context is not.

The default is [`true`](../../Swift/true.md) on devices that natively support wide color, and [`false`](../../Swift/false.md) on those that do not.

## See Also

### Configuring the renderer attributes
- [var opaque: Bool](./opaque.md)
  A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [var scale: CGFloat](./scale.md)
  The display scale of the image renderer context.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](./preferredrange.md)
  The preferred color range of the image renderer context.
- [UIGraphicsImageRendererFormat.Range](./range.md)
  Constants that specify the color range of the image renderer context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/prefersextendedrange)*