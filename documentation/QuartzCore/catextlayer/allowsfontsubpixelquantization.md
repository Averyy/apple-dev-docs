# allowsFontSubpixelQuantization

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Determines whether to allow subpixel quantization for the graphics context used for text rendering.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allowsFontSubpixelQuantization: Bool { get set }
```

```objc
@property BOOL allowsFontSubpixelQuantization;
```

#### Discussion

When enabled, the graphics context used for text rendering may quantize the subpixel positions of glyphs.

## See Also

### Text Visual Properties
- [var font: CFTypeRef?](./font.md)
  The font used to render the receiver’s text.
- [var fontSize: CGFloat](./fontsize.md)
  The font size used to render the receiver’s text. Animatable.
- [var foregroundColor: CGColor?](./foregroundcolor.md)
  The color used to render the receiver’s text. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catextlayer/allowsfontsubpixelquantization)*