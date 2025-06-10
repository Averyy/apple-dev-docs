# init(textStyle:scale:)

**Framework**: UIKit  
**Kind**: init

Creates a configuration object with the specified font text style and scale information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(textStyle: UIFont.TextStyle, scale: UIImage.SymbolScale)
```

#### Return Value

A new symbol configuration object with the specified information.

#### Discussion

Symbol images pick up the font styling information associated with the specified text style, causing them to match any text that uses the same style. Like it does for the text, UIKit scales the image to match the current Dynamic Type setting.

## Parameters

- `textStyle`: The system text styles that support Dynamic Type. For a list of possible values, see  .
- `scale`: The symbol image scale variant to select. Use this parameter to make the image appear bigger or smaller than text that uses the same text style. For a list of possible values, see  .

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
- [UIImage.SymbolVariableValueMode](uiimage/symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(textstyle:scale:))*