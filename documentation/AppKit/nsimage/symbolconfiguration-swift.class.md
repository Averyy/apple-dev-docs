# NSImage.SymbolConfiguration

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that contains the specific font, style, and weight attributes to apply to a symbol image.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class SymbolConfiguration
```

```objc
@interface NSImageSymbolConfiguration : NSObject
```

## Overview

Symbol image configuration objects include details such as the point size, scale, text style, and weight to apply to your symbol image. The system uses these details to determine which variant of the image to use and how to scale or style the image.

```swift
if let image = NSImage(systemSymbolName: "multiply.circle.fill",
                       accessibilityDescription: "A multiply symbol inside a filled circle.") {
        
    var config = NSImage.SymbolConfiguration(textStyle: .body,
                                                     scale: .large)
    config = config.applying(.init(paletteColors: [.systemTeal, .systemGray]))
    imageView.image = image.withSymbolConfiguration(config)
}
```

[`NSImage.SymbolConfiguration`](./symbolconfiguration-swift.class.md) objects are immutable after you create them. If you use the [`applying(_:)`](./symbolconfiguration-swift.class/applying%28_%29.md) method on the object, the new image attributes replace any previous attributes you supplied. After creating a symbol configuration object, assign it to the [`symbolConfiguration`](../nsimageview/symbolconfiguration.md) property of the [`NSImageView`](../nsimageview.md) object you use to display the image. If you draw the image directly, use the [`withSymbolConfiguration(_:)`](./withsymbolconfiguration%28_%29.md) method to create a new image that contains the new attributes.

For design guidance, see [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/).

## Topics

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
- [NSImage.SymbolVariableValueMode](./symbolvariablevaluemode.md)
### Applying a Configuration
- [func applying(NSImage.SymbolConfiguration) -> Self](./symbolconfiguration-swift.class/applying%28_%29.md)
  Creates a configuration object by applying the values from the configuration you specify.
### Creating a Color Configuration
- [convenience init(paletteColors: [NSColor])](./symbolconfiguration-swift.class/init%28palettecolors%29.md)
  Creates a color configuration by specifying a palette of colors.
- [convenience init(hierarchicalColor: NSColor)](./symbolconfiguration-swift.class/init%28hierarchicalcolor%29.md)
  Creates a hierarchical color configuration using the color you specify.
- [class func preferringMulticolor() -> Self](./symbolconfiguration-swift.class/preferringmulticolor%28%29.md)
  Creates a configuration that specifies that the symbol should prefer its multicolor variant if one exists.
### Type Methods
- [class func preferringHierarchical() -> Self](./symbolconfiguration-swift.class/preferringhierarchical%28%29.md)
  Creates a configuration that specifies that the symbol should prefer its hierarchical variant, if one exists.
- [class func preferringMonochrome() -> Self](./symbolconfiguration-swift.class/preferringmonochrome%28%29.md)
  Creates a configuration that specifies that the symbol should prefer its monochrome variant.
### Initializers
- [init?(coder: NSCoder)](./symbolconfiguration-swift.class/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSCoding](../../Foundation/nscoding.md)
- [NSCopying](../../Foundation/nscopying.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../../Foundation/nssecurecoding.md)

## See Also

### Creating Symbol Images
- [func withSymbolConfiguration(NSImage.SymbolConfiguration) -> NSImage?](./withsymbolconfiguration%28_%29.md)
  Creates a new symbol image with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class)*