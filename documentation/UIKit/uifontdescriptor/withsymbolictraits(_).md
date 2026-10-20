# withSymbolicTraits(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func withSymbolicTraits(_ symbolicTraits: UIFontDescriptor.SymbolicTraits) -> UIFontDescriptor?
```

```objc
- (UIFontDescriptor *) fontDescriptorWithSymbolicTraits:(UIFontDescriptorSymbolicTraits) symbolicTraits;
```

#### Return Value

The new font descriptor.

## Parameters

- `symbolicTraits`: The new symbolic traits.

## See Also

### Creating a font descriptor
- [class func preferredFontDescriptor(withTextStyle: UIFont.TextStyle) -> UIFontDescriptor](./preferredfontdescriptor%28withtextstyle%29.md)
  Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [class func preferredFontDescriptor(withTextStyle: UIFont.TextStyle, compatibleWith: UITraitCollection?) -> UIFontDescriptor](./preferredfontdescriptor%28withtextstyle,compatiblewith%29.md)
  Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.
- [init(name: String, matrix: CGAffineTransform)](./init%28name,matrix%29.md)
  Returns a font descriptor with the specified values for the name and matrix dictionary attributes.
- [init(name: String, size: CGFloat)](./init%28name,size%29.md)
  Returns a font descriptor with the specified values for the name and size dictionary attributes.
- [func addingAttributes([UIFontDescriptor.AttributeName : Any]) -> UIFontDescriptor](./addingattributes%28_%29.md)
  Returns a new font descriptor that’s the same as the existing descriptor, but with the specified attributes taking precedence over the existing ones.
- [func withDesign(UIFontDescriptor.SystemDesign) -> UIFontDescriptor?](./withdesign%28_%29.md)
  Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.
- [func withFamily(String) -> UIFontDescriptor](./withfamily%28_%29.md)
  Returns a new font descriptor whose attributes are the same as the existing font descriptor, but from the specified family.
- [func withFace(String) -> UIFontDescriptor](./withface%28_%29.md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified face.
- [func withMatrix(CGAffineTransform) -> UIFontDescriptor](./withmatrix%28_%29.md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified matrix.
- [func withSize(CGFloat) -> UIFontDescriptor](./withsize%28_%29.md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/withsymbolictraits(_:))*