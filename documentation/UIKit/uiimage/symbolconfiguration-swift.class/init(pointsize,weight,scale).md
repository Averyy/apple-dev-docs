# init(pointSize:weight:scale:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a configuration object with the specified point-size, weight, and scale information.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight, scale: UIImage.SymbolScale)
```

```objc
+ (instancetype) configurationWithPointSize:(CGFloat) pointSize weight:(UIImageSymbolWeight) weight scale:(UIImageSymbolScale) scale;
```

#### Return Value

A new symbol configuration object with the specified information.

## Parameters

- `pointSize`: The system font point size to use for the configuration.
- `weight`: The symbol image weight variant to select. Use this parameter to match the weight of the symbol image to your other content. For a list of possible values, see [`UIImage.SymbolWeight`](../symbolweight.md).
- `scale`: The symbol image scale variant to select. Use this parameter to make the image appear bigger or smaller than text that uses the same point size. For a list of possible values, see [`UIImage.SymbolScale`](../symbolscale.md).

## See Also

### Creating a symbol configuration
- [convenience init(pointSize: CGFloat)](./init%28pointsize%29.md)
  Creates a configuration object with the specified point-size information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight)](./init%28pointsize,weight%29.md)
  Creates a configuration object with the specified point-size and weight information.
- [convenience init(scale: UIImage.SymbolScale)](./init%28scale%29.md)
  Creates a configuration object with the specified scale information.
- [convenience init(textStyle: UIFont.TextStyle)](./init%28textstyle%29.md)
  Creates a configuration object with the specified font text style information.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(pointsize:weight:scale:))*