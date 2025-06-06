# init(hierarchicalColor:)

**Framework**: AppKit  
**Kind**: init

Creates a hierarchical color configuration using the color you specify.

**Availability**:
- macOS 12.0+

## Declaration

```swift
convenience init(hierarchicalColor: NSColor)
```

#### Return Value

A new configuration object that creates a palette from a primary color.

#### Discussion

This method creates a color scheme based on a single color. The system reduces the intensity of the base color to create the secondary and tertiary colors.

When combining this with another configuration, the last configuration overrides existing values.

If the symbol doesn’t have a palette variant, this color configuration doesn’t have an effect, so the symbol uses the monochrome (templated) symbol.

## Parameters

- `hierarchicalColor`: The primary color for the symbol.

## See Also

- [convenience init(paletteColors: [NSColor])](nsimage/symbolconfiguration-swift.class/init(palettecolors:).md)
  Creates a color configuration by specifying a palette of colors.
- [class func preferringMulticolor() -> Self](nsimage/symbolconfiguration-swift.class/preferringmulticolor.md)
  Creates a configuration that specifies that the symbol should prefer its multicolor variant if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class/init(hierarchicalcolor:))*