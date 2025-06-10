# UIFontDescriptor

**Framework**: UIKit  
**Kind**: class

A collection of attributes that describes a font.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class UIFontDescriptor
```

#### Overview

A font descriptor can be used to create or modify a [`UIFont`](uifont.md) object. Font descriptors have a font matching capability, so that you can partially describe a font by creating a font descriptor with, for example, just a family name. You can use [`matchingFontDescriptors(withMandatoryKeys:)`](uifontdescriptor/matchingfontdescriptors(withmandatorykeys:).md) to find all the available fonts in the system with a matching family name. Font descriptors can also be archived and unarchived.

There are several ways to create a new [`UIFontDescriptor`](uifontdescriptor.md) object. To take advantage of text styles and respect the user’s current content size category, use [`preferredFontDescriptor(withTextStyle:)`](uifontdescriptor/preferredfontdescriptor(withtextstyle:).md). You can also use `alloc` and [`init(fontAttributes:)`](uifontdescriptor/init(fontattributes:).md), [`fontDescriptorWithFontAttributes:`](uifontdescriptor/fontdescriptorwithfontattributes:.md), [`init(name:matrix:)`](uifontdescriptor/init(name:matrix:).md), or [`init(name:size:)`](uifontdescriptor/init(name:size:).md) to create a font descriptor based on your custom attributes dictionary or on a specific font’s name and size. Alternatively you can use one of the `fontDescriptor…` instance methods (such as [`withFace(_:)`](uifontdescriptor/withface(_:).md)) to create a modified version of an existing descriptor. The latter methods are useful if you have an existing descriptor and simply want to change one aspect.

All attributes in the attributes dictionary are optional.

For design guidance, see [`Human Interface Guidelines`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/visual-design/typography/).

## Topics

### Creating a font descriptor
- [class func preferredFontDescriptor(withTextStyle: UIFont.TextStyle) -> UIFontDescriptor](uifontdescriptor/preferredfontdescriptor(withtextstyle:).md)
  Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [class func preferredFontDescriptor(withTextStyle: UIFont.TextStyle, compatibleWith: UITraitCollection?) -> UIFontDescriptor](uifontdescriptor/preferredfontdescriptor(withtextstyle:compatiblewith:).md)
  Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.
- [init(name: String, matrix: CGAffineTransform)](uifontdescriptor/init(name:matrix:).md)
  Returns a font descriptor with the specified values for the name and matrix dictionary attributes.
- [init(name: String, size: CGFloat)](uifontdescriptor/init(name:size:).md)
  Returns a font descriptor with the specified values for the name and size dictionary attributes.
- [func addingAttributes([UIFontDescriptor.AttributeName : Any]) -> UIFontDescriptor](uifontdescriptor/addingattributes(_:).md)
  Returns a new font descriptor that’s the same as the existing descriptor, but with the specified attributes taking precedence over the existing ones.
- [func withDesign(UIFontDescriptor.SystemDesign) -> UIFontDescriptor?](uifontdescriptor/withdesign(_:).md)
  Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.
- [func withFamily(String) -> UIFontDescriptor](uifontdescriptor/withfamily(_:).md)
  Returns a new font descriptor whose attributes are the same as the existing font descriptor, but from the specified family.
- [func withFace(String) -> UIFontDescriptor](uifontdescriptor/withface(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified face.
- [func withMatrix(CGAffineTransform) -> UIFontDescriptor](uifontdescriptor/withmatrix(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified matrix.
- [func withSize(CGFloat) -> UIFontDescriptor](uifontdescriptor/withsize(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.
- [func withSymbolicTraits(UIFontDescriptor.SymbolicTraits) -> UIFontDescriptor?](uifontdescriptor/withsymbolictraits(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.
### Initializing a font descriptor
- [init(fontAttributes: [UIFontDescriptor.AttributeName : Any])](uifontdescriptor/init(fontattributes:).md)
  Creates a font descriptor with the specified attributes.
- [convenience init()](uifontdescriptor/init.md)
  Creates a font descriptor.
- [init?(coder: NSCoder)](uifontdescriptor/init(coder:).md)
  Creates a font descriptor from data in an unarchiver.
### Finding fonts
- [func matchingFontDescriptors(withMandatoryKeys: Set<UIFontDescriptor.AttributeName>?) -> [UIFontDescriptor]](uifontdescriptor/matchingfontdescriptors(withmandatorykeys:).md)
  Returns all the fonts available in the system with specified attributes that match those of the font.
### Querying a font descriptor
- [var fontAttributes: [UIFontDescriptor.AttributeName : Any]](uifontdescriptor/fontattributes.md)
  The font descriptor’s dictionary of attributes.
- [var matrix: CGAffineTransform](uifontdescriptor/matrix.md)
  The current transform matrix of the font descriptor.
- [func object(forKey: UIFontDescriptor.AttributeName) -> Any?](uifontdescriptor/object(forkey:).md)
  Returns the font attribute that the corresponding key specifies.
- [var pointSize: CGFloat](uifontdescriptor/pointsize.md)
  The point size of the font descriptor.
- [var postscriptName: String](uifontdescriptor/postscriptname.md)
  The PostScript name of the font descriptor.
- [var symbolicTraits: UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.property.md)
  The traits of the font descriptor.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
### Constants
- [UIFont.TextStyle](uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
- [UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign.md)
  Constants that describe the system-defined typeface designs.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [UIFontDescriptor.Class](uifontdescriptor/class.md)
  Constants that classify certain stylistic qualities of the font.
- [UIFontDescriptor.AttributeName](uifontdescriptor/attributename.md)
  Constants that describe font attributes.
- [UIFontDescriptor.FeatureKey](uifontdescriptor/featurekey.md)
  Keys for retrieving feature settings.
- [UIFontDescriptor.TraitKey](uifontdescriptor/traitkey.md)
  Keys for retrieving the font descriptor’s trait information.
- [UIFont.Weight](uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](uifont/width.md)

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Adding a Custom Font to Your App](adding-a-custom-font-to-your-app.md)
  Add a custom font to your app and use it in your app’s interface.
- [class UIFont](uifont.md)
  An object that provides access to the font’s characteristics.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [class UIFontMetrics](uifontmetrics.md)
  A utility object for obtaining custom fonts that scale to support Dynamic Type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor)*