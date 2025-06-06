# withDesign(_:)

**Framework**: UIKit  
**Kind**: method

Returns a new font descriptor that’s the same as the existing descriptor, but with the specified design.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 5.2+

## Declaration

```swift
func withDesign(_ design: UIFontDescriptor.SystemDesign) -> UIFontDescriptor?
```

#### Return Value

The new font descriptor, if the original font descriptor is from a system UI font; otherwise, `nil`.

#### Discussion

This method changes the design of an existing font descriptor that describes a system UI font — for example, a font descriptor created by methods such as [`systemFont(ofSize:)`](uifont/systemfont(ofsize:).md), [`preferredFont(forTextStyle:)`](uifont/preferredfont(fortextstyle:).md), or [`preferredFontDescriptor(withTextStyle:)`](uifontdescriptor/preferredfontdescriptor(withtextstyle:).md). If the original font descriptor doesn’t describe a system font, this method returns `nil`.

## Parameters

- `design`: The new system font design.

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/withdesign(_:))*