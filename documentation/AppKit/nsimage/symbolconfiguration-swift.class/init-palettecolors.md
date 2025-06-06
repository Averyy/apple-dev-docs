# init(paletteColors:)

**Framework**: AppKit  
**Kind**: init

Creates a color configuration by specifying a palette of colors.

**Availability**:
- macOS 12.0+

## Declaration

```swift
convenience init(paletteColors: [NSColor])
```

#### Return Value

A new configuration object that prefers its palette variant.

#### Discussion

The system applies the colors sequentially per layer — the first color for the first layer, and the second color for the second layer. This is independent of the hierarchy level of the layer.

When you combine this with another configuration to create a palette, the last configuration overrides any existing color configuration.

If the symbol doesn’t have a palette variant, this color configuration doesn’t have an effect, so the symbol uses the monochrome (templated) symbol.

## Parameters

- `paletteColors`: The colors to apply to the symbol.

## See Also

- [convenience init(hierarchicalColor: NSColor)](nsimage/symbolconfiguration-swift.class/init(hierarchicalcolor:).md)
  Creates a hierarchical color configuration using the color you specify.
- [class func preferringMulticolor() -> Self](nsimage/symbolconfiguration-swift.class/preferringmulticolor.md)
  Creates a configuration that specifies that the symbol should prefer its multicolor variant if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class/init(palettecolors:))*