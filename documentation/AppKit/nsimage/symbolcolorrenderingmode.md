# NSImage.SymbolColorRenderingMode

**Framework**: AppKit  
**Kind**: enum

**Availability**:
- macOS 26.0+

## Declaration

```swift
enum SymbolColorRenderingMode
```

## Topics

### Enumeration Cases
- [NSImage.SymbolColorRenderingMode.automatic](nsimage/symbolcolorrenderingmode/automatic.md)
  Automatically uses an appropriate color rendering mode for the symbol’s color layers.
- [NSImage.SymbolColorRenderingMode.flat](nsimage/symbolcolorrenderingmode/flat.md)
  Renders the symbol’s color layers using flat colors.
- [NSImage.SymbolColorRenderingMode.gradient](nsimage/symbolcolorrenderingmode/gradient.md)
  Renders the symbol’s color layers using gradients.
### Initializers
- [init?(rawValue: Int)](nsimage/symbolcolorrenderingmode/init(rawvalue:).md)

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
- [NSImage.SymbolVariableValueMode](nsimage/symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolcolorrenderingmode)*