# withSize(_:)

**Framework**: UIKit  
**Kind**: method

Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified point size.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func withSize(_ newPointSize: CGFloat) -> UIFontDescriptor
```

#### Return Value

The new font descriptor.

## Parameters

- `newPointSize`: The new point size.

## See Also

- [class func preferredFontDescriptor(withTextStyle: UIFont.TextStyle) -> UIFontDescriptor](uifontdescriptor/preferredfontdescriptor(withtextstyle:).md)
  Returns a font descriptor that contains the specified text style and the user’s selected content size category.
- [class func preferredFontDescriptor(withTextStyle: UIFont.TextStyle, compatibleWith: UITraitCollection?) -> UIFontDescriptor](uifontdescriptor/preferredfontdescriptor(withtextstyle:compatiblewith:).md)
  Returns a font descriptor that contains the text style and the content size category that the provided trait collection specifies.
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
- [func withSymbolicTraits(UIFontDescriptor.SymbolicTraits) -> UIFontDescriptor?](uifontdescriptor/withsymbolictraits(_:).md)
  Returns a new font descriptor that’s the same as the existing font descriptor, but with the specified symbolic traits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/withsize(_:))*