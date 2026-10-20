# NSFontDescriptor.SystemDesign

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

Constants for font designs, such as monospace, rounded, and serif.

**Availability**:
- macOS

## Declaration

```swift
struct SystemDesign
```

```c
typedef NSString * NSFontDescriptorSystemDesign;
```

## Topics

### Designs
- [static let `default`: NSFontDescriptor.SystemDesign](./systemdesign/default.md)
  The default font design.
- [static let monospaced: NSFontDescriptor.SystemDesign](./systemdesign/monospaced.md)
  A font with a monospace appearance.
- [static let rounded: NSFontDescriptor.SystemDesign](./systemdesign/rounded.md)
  A font with a rounded appearance.
- [static let serif: NSFontDescriptor.SystemDesign](./systemdesign/serif.md)
  A font with a serif design.
### Initializers
- [init(rawValue: String)](./systemdesign/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Modifying an Existing Font Descriptor
- [func addingAttributes([NSFontDescriptor.AttributeName : Any]) -> NSFontDescriptor](./addingattributes%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified attributes taking precedence over the existing ones.
- [func withFace(String) -> NSFontDescriptor](./withface%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified face.
- [func withFamily(String) -> NSFontDescriptor](./withfamily%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified font family.
- [func withMatrix(AffineTransform) -> NSFontDescriptor](./withmatrix%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified font matrix.
- [func withSize(CGFloat) -> NSFontDescriptor](./withsize%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified point size.
- [func withSymbolicTraits(NSFontDescriptor.SymbolicTraits) -> NSFontDescriptor](./withsymbolictraits%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified symbolic traits taking precedence over the existing ones.
- [func withDesign(NSFontDescriptor.SystemDesign) -> Self?](./withdesign%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified design style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/systemdesign)*