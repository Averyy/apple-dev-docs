# NSImage.SymbolVariableValueMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS 26.0+

## Declaration

```swift
enum SymbolVariableValueMode
```

```c
enum NSImageSymbolVariableValueMode : NSInteger;
```

## Topics

### Enumeration Cases
- [NSImage.SymbolVariableValueMode.automatic](./symbolvariablevaluemode/automatic.md)
  Automatically selects an appropriate variable value mode for the symbol.
- [NSImage.SymbolVariableValueMode.color](./symbolvariablevaluemode/color.md)
  The “color” variable value mode. Sets the opacity of each variable layer to either on or off depending on how its threshold compared to the current value.
- [NSImage.SymbolVariableValueMode.draw](./symbolvariablevaluemode/draw.md)
  The “draw” variable value mode. Changes the drawn length of each variable layer to either based on how its range relates to the current value.
### Initializers
- [init?(rawValue: Int)](./symbolvariablevaluemode/init%28rawvalue%29.md)

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
- [NSImage.SymbolScale](./symbolscale.md)
  Constants that specify which scale variant of a symbol image to use.
- [NSImage.SymbolColorRenderingMode](./symbolcolorrenderingmode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolvariablevaluemode)*