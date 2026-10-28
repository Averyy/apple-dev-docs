# preferredRange

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The preferred color range of the image renderer context.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var preferredRange: UIGraphicsImageRendererFormat.Range { get set }
```

```objc
@property (nonatomic) UIGraphicsImageRendererFormatRange preferredRange;
```

## Discussion

This property affects the pixel format of the image that the renderer produces.

Different pixel formats can store different color ranges. The system chooses the precise pixel format, but you can set this property to exclude certain formats that support larger or narrower color ranges than you need.

## See Also

### Configuring the renderer attributes
- [var opaque: Bool](./opaque.md)
  A Boolean value that indicates whether the underlying Core Graphics context has an alpha channel.
- [var scale: CGFloat](./scale.md)
  The display scale of the image renderer context.
- [UIGraphicsImageRendererFormat.Range](./range.md)
  Constants that specify the color range of the image renderer context.
- [var prefersExtendedRange: Bool](./prefersextendedrange.md)
  A Boolean value that specifies whether the bitmap context uses extended color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsimagerendererformat/preferredrange)*