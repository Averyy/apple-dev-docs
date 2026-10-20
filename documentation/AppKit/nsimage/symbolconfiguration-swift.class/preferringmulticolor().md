# preferringMulticolor()

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates a configuration that specifies that the symbol should prefer its multicolor variant if one exists.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class func preferringMulticolor() -> Self
```

```objc
+ (instancetype) configurationPreferringMulticolor;
```

#### Return Value

A new configuration object that prefers its multicolor variant.

#### Discussion

You can combine this configuration with one of the palette-based configurations. In that case, the symbol uses the multicolor variant if one exists; otherwise the symbol uses the palette version.

If the symbol supports neither, the symbol uses the monochrome (templated) symbol.

## See Also

### Creating a Color Configuration
- [convenience init(paletteColors: [NSColor])](./init%28palettecolors%29.md)
  Creates a color configuration by specifying a palette of colors.
- [convenience init(hierarchicalColor: NSColor)](./init%28hierarchicalcolor%29.md)
  Creates a hierarchical color configuration using the color you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class/preferringmulticolor())*