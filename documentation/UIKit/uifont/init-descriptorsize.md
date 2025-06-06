# init(descriptor:size:)

**Framework**: UIKit  
**Kind**: init

Returns a font that matches the specified font descriptor.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(descriptor: UIFontDescriptor, size pointSize: CGFloat)
```

#### Return Value

A font object for the specified descriptor and size.

#### Discussion

In most cases, you can simply use [`init(name:size:)`](uifont/init(name:size:).md) to create standard scaled fonts.

## Parameters

- `descriptor`: The font descriptor to match.
- `pointSize`: The size in points to which the font is scaled. If greater than 0.0, it has precedence over   in  .

## See Also

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
- [init?(name: String, size: CGFloat)](uifont/init(name:size:).md)
  Creates and returns a font object for the specified font name and size.
- [func withSize(CGFloat) -> UIFont](uifont/withsize(_:).md)
  Returns a font object that is the same as the font, but has the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/init(descriptor:size:))*