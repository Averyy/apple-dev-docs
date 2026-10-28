# opaque

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) BOOL opaque;
```

## Discussion

Setting the value of this property to [`false`](../../Swift/false.md) specifies that the underlying Core Graphics context has an alpha channel, whereas [`true`](../../Swift/true.md) indicates it does not. The default value is [`false`](../../Swift/false.md).

A Core Graphics context requires an alpha channel to express transparency. Without an alpha channel a Core Graphics context is said to be opaque, i.e. without transparency.

## See Also

### Configuring the renderer attributes
- [var scale: CGFloat](./scale.md)
  The display scale of the image renderer context.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](./preferredrange.md)
  The preferred color range of the image renderer context.
- [UIGraphicsImageRendererFormat.Range](./range.md)
  Constants that specify the color range of the image renderer context.
- [var prefersExtendedRange: Bool](./prefersextendedrange.md)
  A Boolean value that specifies whether the bitmap context uses extended color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/opaque)*