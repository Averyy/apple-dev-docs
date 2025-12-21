# UIImage.SymbolVariableValueMode

**Framework**: UIKit  
**Kind**: enum

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
enum SymbolVariableValueMode
```

## Topics

### Enumeration Cases
- [UIImage.SymbolVariableValueMode.automatic](uiimage/symbolvariablevaluemode/automatic.md)
  Automatically selects an appropriate variable value mode for the symbol.
- [UIImage.SymbolVariableValueMode.color](uiimage/symbolvariablevaluemode/color.md)
  The “color” variable value mode. Sets the opacity of each variable layer to either on or off depending on how its threshold compared to the current value.
- [UIImage.SymbolVariableValueMode.draw](uiimage/symbolvariablevaluemode/draw.md)
  The “draw” variable value mode. Changes the drawn length of each variable layer to either based on how its range relates to the current value.
### Initializers
- [init?(rawValue: Int)](uiimage/symbolvariablevaluemode/init(rawvalue:).md)

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
- [UIImage.SymbolWeight](uiimage/symbolweight.md)
  Constants that indicate which weight variant of a symbol image to use.
- [UIImage.SymbolColorRenderingMode](uiimage/symbolcolorrenderingmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolvariablevaluemode)*