# NSFontDescriptor.SystemDesign

**Framework**: AppKit  
**Kind**: struct

Constants for font designs, such as monospace, rounded, and serif.

**Availability**:
- macOS ?+

## Declaration

```swift
struct SystemDesign
```

## Topics

### Designs
- [static let `default`: NSFontDescriptor.SystemDesign](nsfontdescriptor/systemdesign/default.md)
  The default font design.
- [static let monospaced: NSFontDescriptor.SystemDesign](nsfontdescriptor/systemdesign/monospaced.md)
  A font with a monospace appearance.
- [static let rounded: NSFontDescriptor.SystemDesign](nsfontdescriptor/systemdesign/rounded.md)
  A font with a rounded appearance.
- [static let serif: NSFontDescriptor.SystemDesign](nsfontdescriptor/systemdesign/serif.md)
  A font with a serif design.
### Initializers
- [init(rawValue: String)](nsfontdescriptor/systemdesign/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/systemdesign)*