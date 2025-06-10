# UIImage.SymbolConfiguration

**Framework**: UIKit  
**Kind**: class

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

## Mentions

- [Configuring and displaying symbol images in your UI](configuring-and-displaying-symbol-images-in-your-ui.md)

#### Overview

Symbol image configuration objects include details such as the point size, scale, text style, weight, and font to apply to your symbol image. The system uses these details to determine which variant of the image to use and how to scale or style the image.

[`UIImage.SymbolConfiguration`](uiimage/symbolconfiguration-swift.class.md) objects are immutable after you create them. If you use the [`applying(_:)`](uiimage/configuration-swift.class/applying(_:).md) method on the object, the new image attributes replace any previous attributes you supplied. After creating a symbol configuration object, assign it to the [`preferredSymbolConfiguration`](uiimageview/preferredsymbolconfiguration.md) property of the [`UIImageView`](uiimageview.md) object you use to display the image. If you draw the image directly, use the [`withConfiguration(_:)`](uiimage/withconfiguration(_:).md) method to create a new image that contains the new attributes.

## Topics

### Creating a symbol configuration
- [convenience init(pointSize: CGFloat)](uiimage/symbolconfiguration-swift.class/init(pointsize:).md)
  Creates a configuration object with the specified point-size information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight)](uiimage/symbolconfiguration-swift.class/init(pointsize:weight:).md)
  Creates a configuration object with the specified point-size and weight information.
- [convenience init(pointSize: CGFloat, weight: UIImage.SymbolWeight, scale: UIImage.SymbolScale)](uiimage/symbolconfiguration-swift.class/init(pointsize:weight:scale:).md)
  Creates a configuration object with the specified point-size, weight, and scale information.
- [convenience init(scale: UIImage.SymbolScale)](uiimage/symbolconfiguration-swift.class/init(scale:).md)
  Creates a configuration object with the specified scale information.
- [convenience init(textStyle: UIFont.TextStyle)](uiimage/symbolconfiguration-swift.class/init(textstyle:).md)
  Creates a configuration object with the specified font text style information.
- [convenience init(textStyle: UIFont.TextStyle, scale: UIImage.SymbolScale)](uiimage/symbolconfiguration-swift.class/init(textstyle:scale:).md)
  Creates a configuration object with the specified font text style and scale information.
- [convenience init(weight: UIImage.SymbolWeight)](uiimage/symbolconfiguration-swift.class/init(weight:).md)
  Creates a configuration object with the specified weight information.
- [convenience init(font: UIFont)](uiimage/symbolconfiguration-swift.class/init(font:).md)
  Creates a configuration object with the specified font information.
- [convenience init(font: UIFont, scale: UIImage.SymbolScale)](uiimage/symbolconfiguration-swift.class/init(font:scale:).md)
  Creates a configuration object with the specified font and scale information.
- [UIImage.SymbolScale](uiimage/symbolscale.md)
  Constants that indicate which scale variant of a symbol image to use.
- [UIImage.SymbolWeight](uiimage/symbolweight.md)
  Constants that indicate which weight variant of a symbol image to use.
- [UIImage.SymbolColorRenderingMode](uiimage/symbolcolorrenderingmode.md)
- [UIImage.SymbolVariableValueMode](uiimage/symbolvariablevaluemode.md)
### Creating a color configuration
- [convenience init(hierarchicalColor: UIColor)](uiimage/symbolconfiguration-swift.class/init(hierarchicalcolor:).md)
  Creates a color configuration with a color scheme that originates from one color.
- [convenience init(paletteColors: [UIColor])](uiimage/symbolconfiguration-swift.class/init(palettecolors:).md)
  Creates a color configuration with a color scheme from a palette of multiple colors.
- [class func preferringMulticolor() -> Self](uiimage/symbolconfiguration-swift.class/preferringmulticolor.md)
  Creates a color configuration that specifies that the symbol image uses its multicolor variant, if one exists.
- [class func preferringMonochrome() -> Self](uiimage/symbolconfiguration-swift.class/preferringmonochrome.md)
  Creates a color configuration that specifies that the symbol image uses its monochrome variant.
### Getting an unspecified configuration
- [class var unspecified: UIImage.SymbolConfiguration](uiimage/symbolconfiguration-swift.class/unspecified.md)
  A symbol configuration object that contains unspecified values for all attributes.
### Removing configuration attributes
- [func configurationWithoutPointSizeAndWeight() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithoutpointsizeandweight.md)
  Returns a copy of the current symbol configuration object without point-size and weight information.
- [func configurationWithoutScale() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithoutscale.md)
  Returns a copy of the current symbol configuration object without scale information.
- [func configurationWithoutTextStyle() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithouttextstyle.md)
  Returns a copy of the current symbol configuration object without font text style information.
- [func configurationWithoutWeight() -> Self](uiimage/symbolconfiguration-swift.class/configurationwithoutweight.md)
  Returns a copy of the current symbol configuration object without weight information.
### Comparing symbol image configurations
- [func isEqual(to: UIImage.SymbolConfiguration?) -> Bool](uiimage/symbolconfiguration-swift.class/isequal(to:).md)
  Returns a Boolean value that indicates whether the configuration objects are equivalent.
### Initializers
- [convenience init(colorRenderingMode: UIImage.SymbolColorRenderingMode)](uiimage/symbolconfiguration-swift.class/init(colorrenderingmode:).md)
  Initializes a symbol configuration with a preferred color rendering mode.
- [convenience init(variableValueMode: UIImage.SymbolVariableValueMode)](uiimage/symbolconfiguration-swift.class/init(variablevaluemode:).md)
  Initializes a symbol configuration with a preferred variable value mode.

## Relationships

### Inherits From
- [UIImage.Configuration](uiimage/configuration-swift.class.md)
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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class UIImage](uiimage.md)
  An object that manages image data in your app.
- [UIImage.Configuration](uiimage/configuration-swift.class.md)
  A configuration object that contains the traits that the system uses when selecting the current image variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimage/symbolconfiguration-swift.class)*