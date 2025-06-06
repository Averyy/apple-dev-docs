# NSFontDescriptor

**Framework**: AppKit  
**Kind**: class

A dictionary of attributes that describe a font.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSFontDescriptor
```

#### Overview

A font descriptor can be used to create or modify an [`NSFont`](nsfont.md) object. The system provides a font matching capability, so that you can partially describe a font by creating a font descriptor with, for example, just a family name. You can then find all the available fonts on the system with a matching family name using [`matchingFontDescriptors(withMandatoryKeys:)`](nsfontdescriptor/matchingfontdescriptors(withmandatorykeys:).md).

There are several ways to create a new [`NSFontDescriptor`](nsfontdescriptor.md) object. You can use `alloc` and  [`init(fontAttributes:)`](nsfontdescriptor/init(fontattributes:).md), [`fontDescriptorWithFontAttributes:`](nsfontdescriptor/fontdescriptorwithfontattributes:.md), [`init(name:matrix:)`](nsfontdescriptor/init(name:matrix:).md), or [`init(name:size:)`](nsfontdescriptor/init(name:size:).md). to create a font descriptor based on either your custom attributes dictionary or on a specific font’s name and size. Alternatively you can use one of the `fontDescriptor…` instance methods (such as [`withFace(_:)`](nsfontdescriptor/withface(_:).md)) to create a modified version of an existing descriptor. The latter methods are useful if you have an existing descriptor and simply want to change one aspect.

All attributes in the attributes dictionary are optional.

## Topics

### Creating a Font Descriptor
- [class func preferredFontDescriptor(forTextStyle: NSFont.TextStyle, options: [NSFont.TextStyleOptionKey : Any]) -> NSFontDescriptor](nsfontdescriptor/preferredfontdescriptor(fortextstyle:options:).md)
  Returns a font descriptor that contains the text style.
- [init(name: String, matrix: AffineTransform)](nsfontdescriptor/init(name:matrix:).md)
  Returns a font descriptor with the name and matrix attributes set to the given values.
- [init(name: String, size: CGFloat)](nsfontdescriptor/init(name:size:).md)
  Returns a font descriptor with the name and size attributes set to the given values.
- [init(fontAttributes: [NSFontDescriptor.AttributeName : Any]?)](nsfontdescriptor/init(fontattributes:).md)
  Initializes and returns a new font descriptor with the specified attributes.
### Modifying an Existing Font Descriptor
- [func addingAttributes([NSFontDescriptor.AttributeName : Any]) -> NSFontDescriptor](nsfontdescriptor/addingattributes(_:).md)
  Returns a new font descriptor based on the current object, but with the specified attributes taking precedence over the existing ones.
- [func withFace(String) -> NSFontDescriptor](nsfontdescriptor/withface(_:).md)
  Returns a new font descriptor based on the current object, but with the specified face.
- [func withFamily(String) -> NSFontDescriptor](nsfontdescriptor/withfamily(_:).md)
  Returns a new font descriptor based on the current object, but with the specified font family.
- [func withMatrix(AffineTransform) -> NSFontDescriptor](nsfontdescriptor/withmatrix(_:).md)
  Returns a new font descriptor based on the current object, but with the specified font matrix.
- [func withSize(CGFloat) -> NSFontDescriptor](nsfontdescriptor/withsize(_:).md)
  Returns a new font descriptor based on the current object, but with the specified point size.
- [func withSymbolicTraits(NSFontDescriptor.SymbolicTraits) -> NSFontDescriptor](nsfontdescriptor/withsymbolictraits(_:).md)
  Returns a new font descriptor based on the current object, but with the specified symbolic traits taking precedence over the existing ones.
- [func withDesign(NSFontDescriptor.SystemDesign) -> Self?](nsfontdescriptor/withdesign(_:).md)
  Returns a new font descriptor based on the current object, but with the specified design style.
- [NSFontDescriptor.SystemDesign](nsfontdescriptor/systemdesign.md)
  Constants for font designs, such as monospace, rounded, and serif.
### Finding Fonts
- [func matchingFontDescriptors(withMandatoryKeys: Set<NSFontDescriptor.AttributeName>?) -> [NSFontDescriptor]](nsfontdescriptor/matchingfontdescriptors(withmandatorykeys:).md)
  Returns all the fonts available on the system whose specified attributes match those of the receiver.
- [func matchingFontDescriptor(withMandatoryKeys: Set<NSFontDescriptor.AttributeName>?) -> NSFontDescriptor?](nsfontdescriptor/matchingfontdescriptor(withmandatorykeys:).md)
  Returns a normalized font descriptor whose specified attributes match those of the receiver.
### Getting the Font Attributes
- [var fontAttributes: [NSFontDescriptor.AttributeName : Any]](nsfontdescriptor/fontattributes.md)
  The receiver’s dictionary of attributes.
- [func object(forKey: NSFontDescriptor.AttributeName) -> Any?](nsfontdescriptor/object(forkey:).md)
  Returns the font attribute specified by the given key.
- [NSFontDescriptor.AttributeName](nsfontdescriptor/attributename.md)
  Constants for the names of font attributes.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [var matrix: AffineTransform?](nsfontdescriptor/matrix.md)
  The current transform matrix of the receiver.
- [var pointSize: CGFloat](nsfontdescriptor/pointsize.md)
  The point size of the receiver.
- [var postscriptName: String?](nsfontdescriptor/postscriptname.md)
  The PostScript name of the receiver.
- [NSFontDescriptor.FeatureKey](nsfontdescriptor/featurekey.md)
  Constants to use as keys to retrieve information about a font descriptor from its feature dictionary.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [var NSFontFamilyClassMask: UInt32](nsfontfamilyclassmask.md)
  Constant you use to access `NSFontFamilyClass` values in the upper four bits of `NSFontSymbolicTraits`.
- [Typeface Information](typeface-information.md)
  Constants for type faces such as italic or bold.
- [NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its variation axis dictionary.
### Getting the Font Traits
- [var symbolicTraits: NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.property.md)
  A bit mask that describes the traits of the receiver.
- [typealias NSFontSymbolicTraits](nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.
- [NSFontDescriptor.TraitKey](nsfontdescriptor/traitkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its trait dictionary.
### Requiring Font Assets
- [var requiresFontAssetRequest: Bool](nsfontdescriptor/requiresfontassetrequest.md)

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

- [class NSFont](nsfont.md)
  The representation of a font in an app.
- [struct NSFontTraitMask](nsfonttraitmask.md)
  Constants for isolating specific traits of a font.
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [NSFontDescriptor.SymbolicTraits](nsfontdescriptor/symbolictraits-swift.struct.md)
  A symbolic description of the stylistic aspects of a font.
- [class NSFontAssetRequest](nsfontassetrequest.md)
- [typealias NSFontSymbolicTraits](nsfontsymbolictraits.md)
  A symbolic description of stylistic aspects of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor)*