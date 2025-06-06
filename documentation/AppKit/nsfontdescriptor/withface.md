# withFace(_:)

**Framework**: AppKit  
**Kind**: method

Returns a new font descriptor based on the current object, but with the specified face.

**Availability**:
- macOS ?+

## Declaration

```swift
func withFace(_ newFace: String) -> NSFontDescriptor
```

#### Return Value

The new font descriptor.

## Parameters

- `newFace`: The replacement font face.

## See Also

- [func addingAttributes([NSFontDescriptor.AttributeName : Any]) -> NSFontDescriptor](nsfontdescriptor/addingattributes(_:).md)
  Returns a new font descriptor based on the current object, but with the specified attributes taking precedence over the existing ones.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/withface(_:))*