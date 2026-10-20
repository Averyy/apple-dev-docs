# scale

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) CGFloat scale;
```

#### Discussion

The display scale determines the number of pixels per point.

The default value is equal to the [`scale`](../uiscreen/scale.md) of the main screen.

## See Also

### Configuring the renderer attributes
- [var opaque: Bool](./opaque.md)
  A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [var preferredRange: UIGraphicsImageRendererFormat.Range](./preferredrange.md)
  The preferred color range of the image renderer context.
- [UIGraphicsImageRendererFormat.Range](./range.md)
  Constants that specify the color range of the image renderer context.
- [var prefersExtendedRange: Bool](./prefersextendedrange.md)
  A Boolean value that specifies whether the bitmap context uses extended color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/scale)*