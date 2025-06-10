# NSImage.SymbolConfiguration

**Framework**: AppKit  
**Kind**: class

An object that contains the specific font, style, and weight attributes to apply to a symbol image.

**Availability**:
- macOS 11.0+

## Declaration

```swift
class SymbolConfiguration
```

#### Overview

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

[`NSImage.SymbolConfiguration`](nsimage/symbolconfiguration-swift.class.md) objects are immutable after you create them. If you use the [`applying(_:)`](nsimage/symbolconfiguration-swift.class/applying(_:).md) method on the object, the new image attributes replace any previous attributes you supplied. After creating a symbol configuration object, assign it to the [`symbolConfiguration`](nsimageview/symbolconfiguration.md) property of the [`NSImageView`](nsimageview.md) object you use to display the image. If you draw the image directly, use the [`withSymbolConfiguration(_:)`](nsimage/withsymbolconfiguration(_:).md) method to create a new image that contains the new attributes.

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/sf-symbols/overview/).

## Topics

### Creating a Symbol Configuration
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
- [NSImage.SymbolVariableValueMode](nsimage/symbolvariablevaluemode.md)
### Applying a Configuration
- [func applying(NSImage.SymbolConfiguration) -> Self](nsimage/symbolconfiguration-swift.class/applying(_:).md)
  Creates a configuration object by applying the values from the configuration you specify.
### Creating a Color Configuration
- [convenience init(paletteColors: [NSColor])](nsimage/symbolconfiguration-swift.class/init(palettecolors:).md)
  Creates a color configuration by specifying a palette of colors.
- [convenience init(hierarchicalColor: NSColor)](nsimage/symbolconfiguration-swift.class/init(hierarchicalcolor:).md)
  Creates a hierarchical color configuration using the color you specify.
- [class func preferringMulticolor() -> Self](nsimage/symbolconfiguration-swift.class/preferringmulticolor.md)
  Creates a configuration that specifies that the symbol should prefer its multicolor variant if one exists.
### Type Methods
- [class func preferringHierarchical() -> Self](nsimage/symbolconfiguration-swift.class/preferringhierarchical.md)
- [class func preferringMonochrome() -> Self](nsimage/symbolconfiguration-swift.class/preferringmonochrome.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func withSymbolConfiguration(NSImage.SymbolConfiguration) -> NSImage?](nsimage/withsymbolconfiguration(_:).md)
  Creates a new symbol image with the specified configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/symbolconfiguration-swift.class)*