# UIImage.SymbolScale

**Framework**: UIKit  
**Kind**: enum

Constants that indicate which scale variant of a symbol image to use.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum SymbolScale
```

## Mentions

- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)

#### Overview

The definition of a symbol image includes multiple scale and weight variants. Scale variants offer a way to define the size of the image relative to layout guides in the symbol image’s definition file. The system chooses the appropriate size variant based on the available space and configuration options.

## Topics

### Symbol image scales
- [UIImage.SymbolScale.default](uiimage/symbolscale/default.md)
  The default scale variant that matches the system usage.
- [UIImage.SymbolScale.unspecified](uiimage/symbolscale/unspecified.md)
  An unspecified scale.
- [UIImage.SymbolScale.small](uiimage/symbolscale/small.md)
  The small variant of the symbol image.
- [UIImage.SymbolScale.medium](uiimage/symbolscale/medium.md)
  The medium variant of the symbol image
- [UIImage.SymbolScale.large](uiimage/symbolscale/large.md)
  The large variant of the symbol image.
### Initializers
- [init?(rawValue: Int)](uiimage/symbolscale/init(rawvalue:).md)

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
- [UIImage.SymbolWeight](uiimage/symbolweight.md)
  Constants that indicate which weight variant of a symbol image to use.
- [UIImage.SymbolColorRenderingMode](uiimage/symbolcolorrenderingmode.md)
- [UIImage.SymbolVariableValueMode](uiimage/symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolscale)*