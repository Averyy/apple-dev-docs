# NSImage.SymbolScale

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify which scale variant of a symbol image to use.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum SymbolScale
```

```c
enum NSImageSymbolScale : NSInteger;
```

#### Overview

Specify a different scale variant for a symbol to change the emphasis of the symbol relative to its adjacent text. The default symbol scale is [`NSImage.SymbolScale.medium`](./symbolscale/medium.md).

## Topics

### Constants
- [NSImage.SymbolScale.small](./symbolscale/small.md)
  The symbol uses the small scale variant.
- [NSImage.SymbolScale.medium](./symbolscale/medium.md)
  The symbol uses the default medium scale variant.
- [NSImage.SymbolScale.large](./symbolscale/large.md)
  The symbol uses the large scale variant.
### Initializers
- [init?(rawValue: Int)](./symbolscale/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating a Symbol Configuration
- [convenience init(pointSize: CGFloat, weight: NSFont.Weight)](./symbolconfiguration-swift.class/init%28pointsize,weight%29.md)
  Creates a symbol configuration with the specified point size and font weight.
- [convenience init(pointSize: CGFloat, weight: NSFont.Weight, scale: NSImage.SymbolScale)](./symbolconfiguration-swift.class/init%28pointsize,weight,scale%29.md)
  Creates a symbol configuration with the specified point size, font weight, and symbol scale.
- [convenience init(textStyle: NSFont.TextStyle)](./symbolconfiguration-swift.class/init%28textstyle%29.md)
  Creates a symbol configuration with the specified text style.
- [convenience init(textStyle: NSFont.TextStyle, scale: NSImage.SymbolScale)](./symbolconfiguration-swift.class/init%28textstyle,scale%29.md)
  Creates a symbol configuration with the specified text style and symbol scale.
- [convenience init(scale: NSImage.SymbolScale)](./symbolconfiguration-swift.class/init%28scale%29.md)
  Creates a symbol configuration using the scale you specify.
- [convenience init(colorRenderingMode: NSImage.SymbolColorRenderingMode)](./symbolconfiguration-swift.class/init%28colorrenderingmode%29.md)
  Create a configuration with a specific color rendering mode.
- [convenience init(variableValueMode: NSImage.SymbolVariableValueMode)](./symbolconfiguration-swift.class/init%28variablevaluemode%29.md)
  Create a configuration with a specified variable value mode.
- [NSFont.TextStyle](../nsfont/textstyle.md)
  Constants that specify the preferred text styles you use with fonts.
- [NSImage.SymbolColorRenderingMode](./symbolcolorrenderingmode.md)
- [NSImage.SymbolVariableValueMode](./symbolvariablevaluemode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolscale)*