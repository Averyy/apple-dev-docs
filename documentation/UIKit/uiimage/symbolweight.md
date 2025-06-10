# UIImage.SymbolWeight

**Framework**: UIKit  
**Kind**: enum

Constants that indicate which weight variant of a symbol image to use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum SymbolWeight
```

#### Overview

The definition of a symbol image includes multiple scale and weight variants. The weight variants offer a way to progressively thicken some or all of the image’s lines. Weights do not correspond to a specific line thickness.

## Topics

### Symbol image weights
- [UIImage.SymbolWeight.unspecified](uiimage/symbolweight/unspecified.md)
  An unspecified symbol image weight.
- [UIImage.SymbolWeight.ultraLight](uiimage/symbolweight/ultralight.md)
  An ultralight weight.
- [UIImage.SymbolWeight.thin](uiimage/symbolweight/thin.md)
  A thin weight
- [UIImage.SymbolWeight.light](uiimage/symbolweight/light.md)
  A light weight.
- [UIImage.SymbolWeight.regular](uiimage/symbolweight/regular.md)
  A regular weight.
- [UIImage.SymbolWeight.medium](uiimage/symbolweight/medium.md)
  A medium weight.
- [UIImage.SymbolWeight.semibold](uiimage/symbolweight/semibold.md)
  A semibold weight.
- [UIImage.SymbolWeight.bold](uiimage/symbolweight/bold.md)
  A bold weight.
- [UIImage.SymbolWeight.heavy](uiimage/symbolweight/heavy.md)
  A heavy weight.
- [UIImage.SymbolWeight.black](uiimage/symbolweight/black.md)
  An ultra-heavy weight.
### Getting the font weight
- [func fontWeight() -> UIFont.Weight](uiimage/symbolweight/fontweight.md)
  The font weight for the specified symbol weight.
### Initializers
- [init?(rawValue: Int)](uiimage/symbolweight/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(pointSize: CGFloat)](uiimage/symbolconfiguration-swift.class/init(pointsize:).md)
  Creates a configuration object with the specified point-size information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight)](uiimage/symbolconfiguration-swift.class/init(pointsize:weight:).md)
  Creates a configuration object with the specified point-size and weight information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight, scale: UIImage.SymbolScale)](uiimage/symbolconfiguration-swift.class/init(pointsize:weight:scale:).md)
  Creates a configuration object with the specified point-size, weight, and scale information.
- [convenience init(scale: UIImage.SymbolScale)](uiimage/symbolconfiguration-swift.class/init(scale:).md)
  Creates a configuration object with the specified scale information.
- [convenience init(textStyle: UIFont.TextStyle)](uiimage/symbolconfiguration-swift.class/init(textstyle:).md)
  Creates a configuration object with the specified font text style information.
- [convenience init(textStyle: UIFont.TextStyle, scale: UIImage.SymbolScale)](uiimage/symbolconfiguration-swift.class/init(textstyle:scale:).md)
  Creates a configuration object with the specified font text style and scale information.
- [convenience init(weight: UIImage.SymbolWeight)](uiimage/symbolconfiguration-swift.class/init(weight:).md)
  Creates a configuration object with the specified weight information.
- [convenience init(font: UIFont)](uiimage/symbolconfiguration-swift.class/init(font:).md)
  Creates a configuration object with the specified font information.
- [convenience init(font: UIFont, scale: UIImage.SymbolScale)](uiimage/symbolconfiguration-swift.class/init(font:scale:).md)
  Creates a configuration object with the specified font and scale information.
- [UIImage.SymbolScale](uiimage/symbolscale.md)
  Constants that indicate which scale variant of a symbol image to use.
- [UIImage.SymbolColorRenderingMode](uiimage/symbolcolorrenderingmode.md)
- [UIImage.SymbolVariableValueMode](uiimage/symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolweight)*