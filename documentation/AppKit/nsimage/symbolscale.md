# NSImage.SymbolScale

**Framework**: AppKit  
**Kind**: enum

Constants that specify which scale variant of a symbol image to use.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum SymbolScale
```

#### Overview

Specify a different scale variant for a symbol to change the emphasis of the symbol relative to its adjacent text. The default symbol scale is [`NSImage.SymbolScale.medium`](nsimage/symbolscale/medium.md).

## Topics

### Constants
- [NSImage.SymbolScale.small](nsimage/symbolscale/small.md)
  The symbol uses the small scale variant.
- [NSImage.SymbolScale.medium](nsimage/symbolscale/medium.md)
  The symbol uses the default medium scale variant.
- [NSImage.SymbolScale.large](nsimage/symbolscale/large.md)
  The symbol uses the large scale variant.
### Initializers
- [init?(rawValue: Int)](nsimage/symbolscale/init(rawvalue:).md)

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
- [NSImage.SymbolColorRenderingMode](nsimage/symbolcolorrenderingmode.md)
- [NSImage.SymbolVariableValueMode](nsimage/symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolscale)*