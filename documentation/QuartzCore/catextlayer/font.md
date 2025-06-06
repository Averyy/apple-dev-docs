# font

**Framework**: Quartzcore  
**Kind**: property

The font used to render the receiver’s text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var font: CFTypeRef? { get set }
```

#### Discussion

May be either a [`CTFont`](https://developer.apple.com/documentation/CoreText/CTFont), a [`CGFont`](https://developer.apple.com/documentation/CoreGraphics/CGFont), an instance of `NSFont` (macOS only), or a string naming the font. In iOS, you cannot assign a [`UIFont`](https://developer.apple.com/documentation/UIKit/UIFont) object to this property. Defaults to Helvetica.

The `font` property is only used when the [`string`](catextlayer/string.md) property is not an `NSAttributedString`.

> **Note**:  If the font property is a `CTFontRef`, a `CGFontRef`, or an instance of `NSFont`, the font size of the property is ignored.

## See Also

- [var fontSize: CGFloat](catextlayer/fontsize.md)
  The font size used to render the receiver’s text. Animatable.
- [var foregroundColor: CGColor?](catextlayer/foregroundcolor.md)
  The color used to render the receiver’s text. Animatable.
- [var allowsFontSubpixelQuantization: Bool](catextlayer/allowsfontsubpixelquantization.md)
  Determines whether to allow subpixel quantization for the graphics context used for text rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/QuartzCore/catextlayer/font)*