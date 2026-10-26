# withSize(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new font descriptor based on the current object, but with the specified point size.

**Availability**:
- macOS

## Declaration

```swift
func withSize(_ newPointSize: CGFloat) -> NSFontDescriptor
```

```objc
- (NSFontDescriptor *) fontDescriptorWithSize:(CGFloat) newPointSize;
```

#### Return Value

The new font descriptor.

## Parameters

- `newPointSize`: The replacement point size.

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
- [func withSymbolicTraits(NSFontDescriptor.SymbolicTraits) -> NSFontDescriptor](./withsymbolictraits%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified symbolic traits taking precedence over the existing ones.
- [func withDesign(NSFontDescriptor.SystemDesign) -> Self?](./withdesign%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified design style.
- [NSFontDescriptor.SystemDesign](./systemdesign.md)
  Constants for font designs, such as monospace, rounded, and serif.
### Related Documentation
- [+ fontDescriptorWithFontAttributes:](./fontdescriptorwithfontattributes_.md)
  Returns a font descriptor with a dictionary of attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/withsize(_:))*