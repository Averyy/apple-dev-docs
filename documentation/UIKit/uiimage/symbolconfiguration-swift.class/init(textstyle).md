# init(textStyle:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a configuration object with the specified font text style information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(textStyle: UIFont.TextStyle)
```

```objc
+ (instancetype) configurationWithTextStyle:(UIFontTextStyle) textStyle;
```

## Return Value

A new symbol configuration object with the specified information.

## Discussion

Symbol images pick up the font styling information associated with the specified text style, causing them to match any text that uses the same style. Like it does for the text, UIKit scales the image to match the current Dynamic Type setting.

## Parameters

- `textStyle`: A system text style that determines the initial appearance of your symbol image. For a list of possible values, see [`UIFont.TextStyle`](../../uifont/textstyle.md).

## See Also

### Creating a symbol configuration
- [convenience init(pointSize: CGFloat)](./init%28pointsize%29.md)
  Creates a configuration object with the specified point-size information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight)](./init%28pointsize,weight%29.md)
  Creates a configuration object with the specified point-size and weight information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight, scale: UIImage.SymbolScale)](./init%28pointsize,weight,scale%29.md)
  Creates a configuration object with the specified point-size, weight, and scale information.
- [convenience init(scale: UIImage.SymbolScale)](./init%28scale%29.md)
  Creates a configuration object with the specified scale information.
- [convenience init(textStyle: UIFont.TextStyle, scale: UIImage.SymbolScale)](./init%28textstyle,scale%29.md)
  Creates a configuration object with the specified font text style and scale information.
- [convenience init(weight: UIImage.SymbolWeight)](./init%28weight%29.md)
  Creates a configuration object with the specified weight information.
- [convenience init(font: UIFont)](./init%28font%29.md)
  Creates a configuration object with the specified font information.
- [convenience init(font: UIFont, scale: UIImage.SymbolScale)](./init%28font,scale%29.md)
  Creates a configuration object with the specified font and scale information.
- [UIImage.SymbolScale](../symbolscale.md)
  Constants that indicate which scale variant of a symbol image to use.
- [UIImage.SymbolWeight](../symbolweight.md)
  Constants that indicate which weight variant of a symbol image to use.
- [UIImage.SymbolColorRenderingMode](../symbolcolorrenderingmode.md)
- [UIImage.SymbolVariableValueMode](../symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(textstyle:))*