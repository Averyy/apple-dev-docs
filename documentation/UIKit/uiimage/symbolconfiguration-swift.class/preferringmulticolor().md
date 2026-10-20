# preferringMulticolor()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class func preferringMulticolor() -> Self
```

```objc
+ (instancetype) configurationPreferringMulticolor;
```

#### Return Value

A symbol configuration that acquires the multicolor variant of a symbol.

#### Discussion

Use this method to acquire the multicolor variant of a symbol, if one exists. This method is the primary approach to retrieving multicolor symbols.

For this color configuration to have an effect, your symbol image must have the following:

- Its [`renderingMode`](../renderingmode-swift.property.md) set to [`UIImage.RenderingMode.alwaysTemplate`](../renderingmode-swift.enum/alwaystemplate.md) or [`UIImage.RenderingMode.automatic`](../renderingmode-swift.enum/automatic.md).
- Multicolor annotations. If your symbol doesn’t have multicolor annotations, the resulting image is a monochrome (template) symbol image. If you combine this configuration with a hierarchical or palette color configuration using [`applying(_:)`](../configuration-swift.class/applying%28_%29.md), the resulting symbol uses the multicolor variant, if one exists, and defaults to the hierarchical or palette variant otherwise.

## See Also

### Creating a color configuration
- [convenience init(hierarchicalColor: UIColor)](./init%28hierarchicalcolor%29.md)
  Creates a color configuration with a color scheme that originates from one color.
- [convenience init(paletteColors: [UIColor])](./init%28palettecolors%29.md)
  Creates a color configuration with a color scheme from a palette of multiple colors.
- [class func preferringMonochrome() -> Self](./preferringmonochrome%28%29.md)
  Creates a color configuration that specifies that the symbol image uses its monochrome variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/preferringmulticolor())*