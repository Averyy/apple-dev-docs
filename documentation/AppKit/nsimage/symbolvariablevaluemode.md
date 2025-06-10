# NSImage.SymbolVariableValueMode

**Framework**: AppKit  
**Kind**: enum

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
enum SymbolVariableValueMode
```

## Topics

### Enumeration Cases
- [NSImage.SymbolVariableValueMode.automatic](nsimage/symbolvariablevaluemode/automatic.md)
  Automatically selects an appropriate variable value mode for the symbol.
- [NSImage.SymbolVariableValueMode.color](nsimage/symbolvariablevaluemode/color.md)
  The “color” variable value mode. Sets the opacity of each variable layer to either on or off depending on how its threshold compared to the current value.
- [NSImage.SymbolVariableValueMode.draw](nsimage/symbolvariablevaluemode/draw.md)
  The “draw” variable value mode. Changes the drawn length of each variable layer to either based on how its range relates to the current value.
### Initializers
- [init?(rawValue: Int)](nsimage/symbolvariablevaluemode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(pointSize: CGFloat, weight: NSFont.Weight)](nsimage/symbolconfiguration-swift.class/init(pointsize:weight:).md)
  Creates a symbol configuration with the specified point size and font weight.
- [convenience init(pointSize: CGFloat, weight: NSFont.Weight, scale: NSImage.SymbolScale)](nsimage/symbolconfiguration-swift.class/init(pointsize:weight:scale:).md)
  Creates a symbol configuration with the specified point size, font weight, and symbol scale.
- [convenience init(textStyle: NSFont.TextStyle)](nsimage/symbolconfiguration-swift.class/init(textstyle:).md)
  Creates a symbol configuration with the specified text style.
- [convenience init(textStyle: NSFont.TextStyle, scale: NSImage.SymbolScale)](nsimage/symbolconfiguration-swift.class/init(textstyle:scale:).md)
  Creates a symbol configuration with the specified text style and symbol scale.
- [convenience init(scale: NSImage.SymbolScale)](nsimage/symbolconfiguration-swift.class/init(scale:).md)
  Creates a symbol configuration using the scale you specify.
- [convenience init(colorRenderingMode: NSImage.SymbolColorRenderingMode)](nsimage/symbolconfiguration-swift.class/init(colorrenderingmode:).md)
  Create a configuration with a specific color rendering mode.
- [convenience init(variableValueMode: NSImage.SymbolVariableValueMode)](nsimage/symbolconfiguration-swift.class/init(variablevaluemode:).md)
  Create a configuration with a specified variable value mode.
- [NSFont.TextStyle](nsfont/textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSImage.SymbolScale](nsimage/symbolscale.md)
  Constants that specify which scale variant of a symbol image to use.
- [NSImage.SymbolColorRenderingMode](nsimage/symbolcolorrenderingmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolvariablevaluemode)*