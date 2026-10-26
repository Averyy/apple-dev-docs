# withFace(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new font descriptor based on the current object, but with the specified face.

**Availability**:
- macOS

## Declaration

```swift
func withFace(_ newFace: String) -> NSFontDescriptor
```

```objc
- (NSFontDescriptor *) fontDescriptorWithFace:(NSString *) newFace;
```

#### Return Value

The new font descriptor.

## Parameters

- `newFace`: The replacement font face.

## See Also

### Modifying an Existing Font Descriptor
- [func addingAttributes([NSFontDescriptor.AttributeName : Any]) -> NSFontDescriptor](./addingattributes%28_%29.md)
  Returns a new font descriptor based on the current object, but with the specified attributes taking precedence over the existing ones.
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
- [NSFontDescriptor.SystemDesign](./systemdesign.md)
  Constants for font designs, such as monospace, rounded, and serif.
### Related Documentation
- [+ fontDescriptorWithFontAttributes:](./fontdescriptorwithfontattributes_.md)
  Returns a font descriptor with a dictionary of attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/withface(_:))*