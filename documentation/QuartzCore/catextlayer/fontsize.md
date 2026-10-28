# fontSize

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property CGFloat fontSize;
```

## Discussion

Defaults to 36.0.

The `fontSize` property is only used when the [`string`](./string.md) property is not an `NSAttributedString`.

> **Note**:  Implicit animation of this property is only enabled in applications compiled for macOS 10.6 and later.

## See Also

### Text Visual Properties
- [var font: CFTypeRef?](./font.md)
  The font used to render the receiver’s text.
- [var foregroundColor: CGColor?](./foregroundcolor.md)
  The color used to render the receiver’s text. Animatable.
- [var allowsFontSubpixelQuantization: Bool](./allowsfontsubpixelquantization.md)
  Determines whether to allow subpixel quantization for the graphics context used for text rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catextlayer/fontsize)*