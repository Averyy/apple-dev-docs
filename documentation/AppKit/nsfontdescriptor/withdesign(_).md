# withDesign(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns a new font descriptor based on the current object, but with the specified design style.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func withDesign(_ design: NSFontDescriptor.SystemDesign) -> Self?
```

```objc
- (instancetype) fontDescriptorWithDesign:(NSFontDescriptorSystemDesign) design;
```

## Return Value

The new font descriptor.

## Parameters

- `design`: The replacement design style for the font. For a list of possible values, see `UIFontDescriptor.SystemDesign`.

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
- [NSFontDescriptor.SystemDesign](./systemdesign.md)
  Constants for font designs, such as monospace, rounded, and serif.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontdescriptor/withdesign(_:))*