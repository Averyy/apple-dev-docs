# NSFontDescriptor.AttributeName

**Framework**: AppKit  
**Kind**: struct

Constants for the names of font attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
struct AttributeName
```

#### Discussion

You can retrieve the values for these attributes using [`object(forKey:)`](nsfontdescriptor/object(forkey:).md).

## Topics

### Font Attributes
- [static let family: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/family.md)
  An optional string object that specifies the font family.
- [static let name: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/name.md)
  An optional string object that specifies the font name.
- [static let face: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/face.md)
  An optional string object that specifies the font face.
- [static let size: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/size.md)
  An optional floating-point number that specifies the font size.
- [static let visibleName: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/visiblename.md)
  An optional string object that specifies the font’s visible name.
- [static let matrix: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/matrix.md)
  An affine transform that specifies the font’s transformation matrix.
- [static let variation: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/variation.md)
  A dictionary that describes the font’s variation axis.
- [static let characterSet: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/characterset.md)
  The set of Unicode characters covered by the font.
- [static let cascadeList: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/cascadelist.md)
  An array, each member of which is a sub-descriptor.
- [static let traits: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/traits.md)
  A dictionary that fully describes the font traits.
- [static let fixedAdvance: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/fixedadvance.md)
  A floating-point value that overrides the glyph advancement specified by the font.
- [static let featureSettings: NSFontDescriptor.AttributeName](nsfontdescriptor/attributename/featuresettings.md)
  An array of dictionaries representing non-default font feature settings.
### Initializers
- [init(String)](nsfontdescriptor/attributename/init(_:).md)
- [init(rawValue: String)](nsfontdescriptor/attributename/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var fontAttributes: [NSFontDescriptor.AttributeName : Any]](nsfontdescriptor/fontattributes.md)
  The receiver’s dictionary of attributes.
- [func object(forKey: NSFontDescriptor.AttributeName) -> Any?](nsfontdescriptor/object(forkey:).md)
  Returns the font attribute specified by the given key.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/attributename)*