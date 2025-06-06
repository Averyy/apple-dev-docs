# fontSize

**Framework**: Core Animation  
**Kind**: property

The font size used to render the receiver’s text. Animatable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var fontSize: CGFloat { get set }
```

#### Discussion

Defaults to 36.0.

The `fontSize` property is only used when the [`string`](catextlayer/string.md) property is not an `NSAttributedString`.

> **Note**:  Implicit animation of this property is only enabled in applications compiled for macOS 10.6 and later.

 Implicit animation of this property is only enabled in applications compiled for macOS 10.6 and later.

## See Also

- [var font: CFTypeRef?](catextlayer/font.md)
  The font used to render the receiver’s text.
- [var foregroundColor: CGColor?](catextlayer/foregroundcolor.md)
  The color used to render the receiver’s text. Animatable.
- [var allowsFontSubpixelQuantization: Bool](catextlayer/allowsfontsubpixelquantization.md)
  Determines whether to allow subpixel quantization for the graphics context used for text rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catextlayer/fontsize)*