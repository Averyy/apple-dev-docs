# NSFontDescriptor.FeatureKey

**Framework**: AppKit  
**Kind**: struct

Constants to use as keys to retrieve information about a font descriptor from its feature dictionary.

**Availability**:
- macOS ?+

## Declaration

```swift
struct FeatureKey
```

#### Discussion

These keys are used with [`featureSettings`](nsfontdescriptor/attributename/featuresettings.md).

## Topics

### Feature Keys
- [static let typeIdentifier: NSFontDescriptor.FeatureKey](nsfontdescriptor/featurekey/typeidentifier.md)
  A key that indicates the type of the font feature.
- [static let selectorIdentifier: NSFontDescriptor.FeatureKey](nsfontdescriptor/featurekey/selectoridentifier.md)
  A key that indicates the selector of the font feature.
### Initializers
- [init(String)](nsfontdescriptor/featurekey/init(_:).md)
- [init(rawValue: String)](nsfontdescriptor/featurekey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [typealias NSFontFamilyClass](nsfontfamilyclass.md)
  Constants that classify certain stylistic qualities of the font.
- [var NSFontFamilyClassMask: UInt32](nsfontfamilyclassmask.md)
  Constant you use to access `NSFontFamilyClass` values in the upper four bits of `NSFontSymbolicTraits`.
- [Typeface Information](typeface-information.md)
  Constants for type faces such as italic or bold.
- [NSFontDescriptor.VariationKey](nsfontdescriptor/variationkey.md)
  Constants that can be used as keys to retrieve information about a font descriptor from its variation axis dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/featurekey)*