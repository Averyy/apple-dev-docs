# init(hierarchicalColor:)

**Framework**: UIKit  
**Kind**: init

Creates a color configuration with a color scheme that originates from one color.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(hierarchicalColor: UIColor)
```

#### Discussion

When you create an image with this configuration, the system generates a color scheme according to the color you specify, creating secondary and tertiary colors by reducing the intensity of the base color. Typically, the system generates the secondary and tertiary colors by reducing the opacity of the primary color, but it may perform additional color adjustments.

The system renders all layers in your symbol with the primary, secondary, and tertiary colors according to the symbol layer hierarchy.

For this color configuration to have an effect, your symbol image must have the following:

- Its [`renderingMode`](uiimage/renderingmode-swift.property.md) set to [`UIImage.RenderingMode.alwaysTemplate`](uiimage/renderingmode-swift.enum/alwaystemplate.md) or [`UIImage.RenderingMode.automatic`](uiimage/renderingmode-swift.enum/automatic.md).
- Hierarchical layer annotations. If your symbol doesn’t have hierarchical layer annotations, the resulting image is a monochrome (template) symbol image.

This color configuration can’t combine with palette color configurations that you create with [`init(paletteColors:)`](uiimage/symbolconfiguration-swift.class/init(palettecolors:).md). If you attempt to combine this configuration with a palette color configuration, the last configuration that you specify takes precedence, overwriting the previous color configuration.

## Parameters

- `hierarchicalColor`: The colors to apply to the symbol.

## See Also

- [convenience init(paletteColors: [UIColor])](uiimage/symbolconfiguration-swift.class/init(palettecolors:).md)
  Creates a color configuration with a color scheme from a palette of multiple colors.
- [class func preferringMulticolor() -> Self](uiimage/symbolconfiguration-swift.class/preferringmulticolor.md)
  Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.
- [class func preferringMonochrome() -> Self](uiimage/symbolconfiguration-swift.class/preferringmonochrome.md)
  Creates a color configuration that specifies that the symbol image uses its monochrome variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class/init(hierarchicalcolor:))*