# preferredFont(forTextStyle:compatibleWith:)

**Framework**: UIKit  
**Kind**: method

Returns an instance of the system font for the appropriate text style and traits.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class func preferredFont(forTextStyle style: UIFont.TextStyle, compatibleWith traitCollection: UITraitCollection?) -> UIFont
```

#### Return Value

The system font associated with the specified text style and traits.

#### Discussion

To create a styled font based on a custom font, use a [`UIFontMetrics`](uifontmetrics.md) object.

Because fonts are immutable, any element that adjusts for an updated content size category does not modify the font itself. Instead, the element replaces the assigned font with a new instance based on the original settings.

## Parameters

- `style`: The text style for which to return a font. See   for recognized values.
- `traitCollection`: The traits to use when determining which font to return.

## See Also

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [class func preferredFont(forTextStyle: UIFont.TextStyle) -> UIFont](uifont/preferredfont(fortextstyle:).md)
  Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [UIFont.TextStyle](uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
- [init?(name: String, size: CGFloat)](uifont/init(name:size:).md)
  Creates and returns a font object for the specified font name and size.
- [init(descriptor: UIFontDescriptor, size: CGFloat)](uifont/init(descriptor:size:).md)
  Returns a font that matches the specified font descriptor.
- [func withSize(CGFloat) -> UIFont](uifont/withsize(_:).md)
  Returns a font object that is the same as the font, but has the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/preferredfont(fortextstyle:compatiblewith:))*