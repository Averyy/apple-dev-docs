# preferredFontDescriptor(withTextStyle:compatibleWith:)

**Framework**: UIKit  
**Kind**: method

Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func preferredFontDescriptor(withTextStyle style: UIFont.TextStyle, compatibleWith traitCollection: UITraitCollection?) -> UIFontDescriptor
```

#### Return Value

The new font descriptor.

## Parameters

- `style`: The text style for which to return a font descriptor.
- `traitCollection`: The trait collection containing the content size category information.

## See Also

- [class func preferredFontDescriptor(withTextStyle: UIFont.TextStyle) -> UIFontDescriptor](uifontdescriptor/preferredfontdescriptor(withtextstyle:).md)
  Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [init(name: String, matrix: CGAffineTransform)](uifontdescriptor/init(name:matrix:).md)
  Returns a font descriptor with the specified values for the name and matrix dictionary attributes.
- [init(name: String, size: CGFloat)](uifontdescriptor/init(name:size:).md)
  Returns a font descriptor with the specified values for the name and size dictionary attributes.
- [func addingAttributes([UIFontDescriptor.AttributeName : Any]) -> UIFontDescriptor](uifontdescriptor/addingattributes(_:).md)
  Returns a new font descriptor that’s the same as the existing descriptor, but with the specified attributes taking precedence over the existing ones.
- [func withDesign(UIFontDescriptor.SystemDesign) -> UIFontDescriptor?](uifontdescriptor/withdesign(_:).md)
  Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.
- [func withFamily(String) -> UIFontDescriptor](uifontdescriptor/withfamily(_:).md)
  Returns a new font descriptor whose attributes are the same as the existing font descriptor, but from the specified family.
- [func withFace(String) -> UIFontDescriptor](uifontdescriptor/withface(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified face.
- [func withMatrix(CGAffineTransform) -> UIFontDescriptor](uifontdescriptor/withmatrix(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified matrix.
- [func withSize(CGFloat) -> UIFontDescriptor](uifontdescriptor/withsize(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.
- [func withSymbolicTraits(UIFontDescriptor.SymbolicTraits) -> UIFontDescriptor?](uifontdescriptor/withsymbolictraits(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/preferredfontdescriptor(withtextstyle:compatiblewith:))*