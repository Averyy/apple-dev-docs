# NSFontDescriptor.VariationKey

**Framework**: AppKit  
**Kind**: struct

Constants that can be used as keys to retrieve information about a font descriptor from its variation axis dictionary.

**Availability**:
- macOS ?+

## Declaration

```swift
struct VariationKey
```

#### Discussion

These keys are used with [`variation`](nsfontdescriptor/attributename/variation.md).

## Topics

### Variation Keys
- [static let identifier: NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey/identifier.md)
  The axis identifier value as a number object.
- [static let minimumValue: NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey/minimumvalue.md)
  The minimum axis value as a number object.
- [static let maximumValue: NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey/maximumvalue.md)
  The maximum axis value as a number object.
- [static let defaultValue: NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey/defaultvalue.md)
  The default axis value as a number object.
- [static let name: NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey/name.md)
  The localized variation axis name.
### Initializers
- [init(rawValue: String)](nsfontdescriptor/variationkey/init(rawvalue:).md)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/variationkey)*