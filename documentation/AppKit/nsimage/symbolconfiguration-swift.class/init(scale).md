# init(scale:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a symbol configuration using the scale you specify.

**Availability**:
- macOS 11.0+

## Declaration

```swift
convenience init(scale: NSImage.SymbolScale)
```

```objc
+ (instancetype) configurationWithScale:(NSImageSymbolScale) scale;
```

## Return Value

A new configuration object.

## Parameters

- `scale`: The symbol scale.

## See Also

### Creating a Symbol Configuration
- [convenience init(pointSize: CGFloat, weight: NSFont.Weight)](./init%28pointsize,weight%29.md)
  Creates a symbol configuration with the specified point size and font weight.
- [convenience init(pointSize: CGFloat, weight: NSFont.Weight, scale: NSImage.SymbolScale)](./init%28pointsize,weight,scale%29.md)
  Creates a symbol configuration with the specified point size, font weight, and symbol scale.
- [convenience init(textStyle: NSFont.TextStyle)](./init%28textstyle%29.md)
  Creates a symbol configuration with the specified text style.
- [convenience init(textStyle: NSFont.TextStyle, scale: NSImage.SymbolScale)](./init%28textstyle,scale%29.md)
  Creates a symbol configuration with the specified text style and symbol scale.
- [convenience init(colorRenderingMode: NSImage.SymbolColorRenderingMode)](./init%28colorrenderingmode%29.md)
  Create a configuration with a specific color rendering mode.
- [convenience init(variableValueMode: NSImage.SymbolVariableValueMode)](./init%28variablevaluemode%29.md)
  Create a configuration with a specified variable value mode.
- [NSFont.TextStyle](../../nsfont/textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSImage.SymbolScale](../symbolscale.md)
  Constants that specify which scale variant of a symbol image to use.
- [NSImage.SymbolColorRenderingMode](../symbolcolorrenderingmode.md)
- [NSImage.SymbolVariableValueMode](../symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class/init(scale:))*