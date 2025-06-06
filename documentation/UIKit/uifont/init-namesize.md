# init(name:size:)

**Framework**: UIKit  
**Kind**: init

Creates and returns a font object for the specified font name and size.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(name fontName: String, size fontSize: CGFloat)
```

#### Return Value

A font object of the specified name and size.

#### Discussion

You can use the [`fontNames(forFamilyName:)`](uifont/fontnames(forfamilyname:).md) method to retrieve the specific font names for a given font family.

## Parameters

- `fontName`: The fully specified name of the font. This name incorporates both the font family name and the specific style information for the font.
- `fontSize`: The size (in points) to which the font is scaled. This value must be greater than 0.0.

## See Also

- [class var familyNames: [String]](uifont/familynames.md)
  Returns an array of font family names available on the system.
- [class func fontNames(forFamilyName: String) -> [String]](uifont/fontnames(forfamilyname:).md)
  Returns an array of font names available in a particular font family.
- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [class func preferredFont(forTextStyle: UIFont.TextStyle) -> UIFont](uifont/preferredfont(fortextstyle:).md)
  Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [class func preferredFont(forTextStyle: UIFont.TextStyle, compatibleWith: UITraitCollection?) -> UIFont](uifont/preferredfont(fortextstyle:compatiblewith:).md)
  Returns an instance of the system font for the appropriate text style and traits.
- [UIFont.TextStyle](uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
- [init(descriptor: UIFontDescriptor, size: CGFloat)](uifont/init(descriptor:size:).md)
  Returns a font that matches the specified font descriptor.
- [func withSize(CGFloat) -> UIFont](uifont/withsize(_:).md)
  Returns a font object that is the same as the font, but has the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/init(name:size:))*