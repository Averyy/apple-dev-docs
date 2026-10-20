# UIImage.SymbolConfiguration

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

An object that contains the specific font, size, style, and weight attributes to apply to a symbol image.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class SymbolConfiguration
```

```objc
@interface UIImageSymbolConfiguration : UIImageConfiguration
```

## Mentions

- [Configuring and displaying symbol images in your UI](../configuring-and-displaying-symbol-images-in-your-ui.md)

#### Overview

Symbol image configuration objects include details such as the point size, scale, text style, weight, and font to apply to your symbol image. The system uses these details to determine which variant of the image to use and how to scale or style the image.

[`UIImage.SymbolConfiguration`](./symbolconfiguration-swift.class.md) objects are immutable after you create them. If you use the [`applying(_:)`](./configuration-swift.class/applying%28_%29.md) method on the object, the new image attributes replace any previous attributes you supplied. After creating a symbol configuration object, assign it to the [`preferredSymbolConfiguration`](../uiimageview/preferredsymbolconfiguration.md) property of the [`UIImageView`](../uiimageview.md) object you use to display the image. If you draw the image directly, use the [`withConfiguration(_:)`](./withconfiguration%28_%29.md) method to create a new image that contains the new attributes.

## Topics

### Creating a symbol configuration
- [convenience init(pointSize: CGFloat)](./symbolconfiguration-swift.class/init%28pointsize%29.md)
  Creates a configuration object with the specified point-size information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight)](./symbolconfiguration-swift.class/init%28pointsize,weight%29.md)
  Creates a configuration object with the specified point-size and weight information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight, scale: UIImage.SymbolScale)](./symbolconfiguration-swift.class/init%28pointsize,weight,scale%29.md)
  Creates a configuration object with the specified point-size, weight, and scale information.
- [convenience init(scale: UIImage.SymbolScale)](./symbolconfiguration-swift.class/init%28scale%29.md)
  Creates a configuration object with the specified scale information.
- [convenience init(textStyle: UIFont.TextStyle)](./symbolconfiguration-swift.class/init%28textstyle%29.md)
  Creates a configuration object with the specified font text style information.
- [convenience init(textStyle: UIFont.TextStyle, scale: UIImage.SymbolScale)](./symbolconfiguration-swift.class/init%28textstyle,scale%29.md)
  Creates a configuration object with the specified font text style and scale information.
- [convenience init(weight: UIImage.SymbolWeight)](./symbolconfiguration-swift.class/init%28weight%29.md)
  Creates a configuration object with the specified weight information.
- [convenience init(font: UIFont)](./symbolconfiguration-swift.class/init%28font%29.md)
  Creates a configuration object with the specified font information.
- [convenience init(font: UIFont, scale: UIImage.SymbolScale)](./symbolconfiguration-swift.class/init%28font,scale%29.md)
  Creates a configuration object with the specified font and scale information.
- [UIImage.SymbolScale](./symbolscale.md)
  Constants that indicate which scale variant of a symbol image to use.
- [UIImage.SymbolWeight](./symbolweight.md)
  Constants that indicate which weight variant of a symbol image to use.
- [UIImage.SymbolColorRenderingMode](./symbolcolorrenderingmode.md)
- [UIImage.SymbolVariableValueMode](./symbolvariablevaluemode.md)
### Creating a color configuration
- [convenience init(hierarchicalColor: UIColor)](./symbolconfiguration-swift.class/init%28hierarchicalcolor%29.md)
  Creates a color configuration with a color scheme that originates from one color.
- [convenience init(paletteColors: [UIColor])](./symbolconfiguration-swift.class/init%28palettecolors%29.md)
  Creates a color configuration with a color scheme from a palette of multiple colors.
- [class func preferringMulticolor() -> Self](./symbolconfiguration-swift.class/preferringmulticolor%28%29.md)
  Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.
- [class func preferringMonochrome() -> Self](./symbolconfiguration-swift.class/preferringmonochrome%28%29.md)
  Creates a color configuration that specifies that the symbol image uses its monochrome variant.
### Getting an unspecified configuration
- [class var unspecified: UIImage.SymbolConfiguration](./symbolconfiguration-swift.class/unspecified.md)
  A symbol configuration object that contains unspecified values for all attributes.
### Removing configuration attributes
- [func configurationWithoutPointSizeAndWeight() -> Self](./symbolconfiguration-swift.class/configurationwithoutpointsizeandweight%28%29.md)
  Returns a copy of the current symbol configuration object without point-size and weight information.
- [func configurationWithoutScale() -> Self](./symbolconfiguration-swift.class/configurationwithoutscale%28%29.md)
  Returns a copy of the current symbol configuration object without scale information.
- [func configurationWithoutTextStyle() -> Self](./symbolconfiguration-swift.class/configurationwithouttextstyle%28%29.md)
  Returns a copy of the current symbol configuration object without font text style information.
- [func configurationWithoutWeight() -> Self](./symbolconfiguration-swift.class/configurationwithoutweight%28%29.md)
  Returns a copy of the current symbol configuration object without weight information.
### Comparing symbol image configurations
- [func isEqual(to: UIImage.SymbolConfiguration?) -> Bool](./symbolconfiguration-swift.class/isequal%28to%29.md)
  Returns a Boolean value that indicates whether the configuration objects are equivalent.
### Initializers
- [convenience init(colorRenderingMode: UIImage.SymbolColorRenderingMode)](./symbolconfiguration-swift.class/init%28colorrenderingmode%29.md)
  Initializes a symbol configuration with a preferred color rendering mode.
- [convenience init(variableValueMode: UIImage.SymbolVariableValueMode)](./symbolconfiguration-swift.class/init%28variablevaluemode%29.md)
  Initializes a symbol configuration with a preferred variable value mode.

## Relationships

### Inherits From
- [UIImage.Configuration](./configuration-swift.class.md)
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
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Representations
- [class UIImage](../uiimage.md)
  An object that manages image data in your app.
- [UIImage.Configuration](./configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class)*