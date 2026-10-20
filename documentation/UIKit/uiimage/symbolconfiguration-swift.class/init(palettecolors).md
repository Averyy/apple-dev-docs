# init(paletteColors:)

**Framework**: UIKit  
**Kind**: init

Creates a color configuration with a color scheme from a palette of multiple colors.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(paletteColors: [UIColor])
```

#### Discussion

When you create an image with this configuration, the system applies each color to the corresponding layer in the symbol layer hierarchy.

If the symbol has only two nonconsecutive layers (primary and tertiary), specifying two colors applies the second color to the tertiary layer. Specifying three colors ignores the second color and applies the third color to the tertiary layer.

For this color configuration to have an effect, your symbol image must have the following:

- Its [`renderingMode`](uiimage/renderingmode-swift.property.md) set to [`UIImage.RenderingMode.alwaysTemplate`](uiimage/renderingmode-swift.enum/alwaystemplate.md) or [`UIImage.RenderingMode.automatic`](uiimage/renderingmode-swift.enum/automatic.md).
- Hierarchical layer annotations. If your symbol doesn’t have hierarchical layer annotations, the resulting image is a monochrome (template) symbol image.

This color configuration can’t combine with hierarchical color configurations that you create with [`init(hierarchicalColor:)`](uiimage/symbolconfiguration-swift.class/init(hierarchicalcolor:).md). If you attempt to combine this configuration with a hierarchical color configuration, the last configuration that you specify takes precedence, overwriting the previous color configuration.

## Parameters

- `paletteColors`: The colors to apply to the symbol.

## See Also

- [convenience init(hierarchicalColor: UIColor)](uiimage/symbolconfiguration-swift.class/init(hierarchicalcolor:).md)
  Creates a color configuration with a color scheme that originates from one color.
- [class func preferringMulticolor() -> Self](uiimage/symbolconfiguration-swift.class/preferringmulticolor.md)
  Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.
- [class func preferringMonochrome() -> Self](uiimage/symbolconfiguration-swift.class/preferringmonochrome.md)
  Creates a color configuration that specifies that the symbol image uses its monochrome variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(palettecolors:))*