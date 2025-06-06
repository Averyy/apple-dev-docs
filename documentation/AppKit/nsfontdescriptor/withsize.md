# withSize(_:)

**Framework**: AppKit  
**Kind**: method

Returns a new font descriptor based on the current object, but with the specified point size.

**Availability**:
- macOS ?+

## Declaration

```swift
func withSize(_ newPointSize: CGFloat) -> NSFontDescriptor
```

#### Return Value

The new font descriptor.

## Parameters

- `newPointSize`: The replacement point size.

## See Also

- [func addingAttributes([NSFontDescriptor.AttributeName : Any]) -> NSFontDescriptor](nsfontdescriptor/addingattributes(_:).md)
  Returns a new font descriptor based on the current object, but with the specified attributes taking precedence over the existing ones.
- [func withFace(String) -> NSFontDescriptor](nsfontdescriptor/withface(_:).md)
  Returns a new font descriptor based on the current object, but with the specified face.
- [func withFamily(String) -> NSFontDescriptor](nsfontdescriptor/withfamily(_:).md)
  Returns a new font descriptor based on the current object, but with the specified font family.
- [func withMatrix(AffineTransform) -> NSFontDescriptor](nsfontdescriptor/withmatrix(_:).md)
  Returns a new font descriptor based on the current object, but with the specified font matrix.
- [func withSymbolicTraits(NSFontDescriptor.SymbolicTraits) -> NSFontDescriptor](nsfontdescriptor/withsymbolictraits(_:).md)
  Returns a new font descriptor based on the current object, but with the specified symbolic traits taking precedence over the existing ones.
- [func withDesign(NSFontDescriptor.SystemDesign) -> Self?](nsfontdescriptor/withdesign(_:).md)
  Returns a new font descriptor based on the current object, but with the specified design style.
- [NSFontDescriptor.SystemDesign](nsfontdescriptor/systemdesign.md)
  Constants for font designs, such as monospace, rounded, and serif.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/withsize(_:))*