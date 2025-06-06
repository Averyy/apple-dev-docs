# UIFont.TextStyle

**Framework**: UIKit  
**Kind**: struct

Constants that describe the preferred styles for fonts.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
struct TextStyle
```

#### Overview

Pass these constants to the [`preferredFont(forTextStyle:)`](uifont/preferredfont(fortextstyle:).md) method of [`UIFont`](uifont.md) or the [`preferredFontDescriptor(withTextStyle:)`](uifontdescriptor/preferredfontdescriptor(withtextstyle:).md) method of [`UIFontDescriptor`](uifontdescriptor.md) to retrieve the corresponding font information.

## Topics

### Constants
- [static let body: UIFont.TextStyle](uifont/textstyle/body.md)
  The font for body text.
- [static let callout: UIFont.TextStyle](uifont/textstyle/callout.md)
  The font for callouts.
- [static let caption1: UIFont.TextStyle](uifont/textstyle/caption1.md)
  The font for standard captions.
- [static let caption2: UIFont.TextStyle](uifont/textstyle/caption2.md)
  The font for alternate captions.
- [static let footnote: UIFont.TextStyle](uifont/textstyle/footnote.md)
  The font for footnotes.
- [static let headline: UIFont.TextStyle](uifont/textstyle/headline.md)
  The font for headings.
- [static let subheadline: UIFont.TextStyle](uifont/textstyle/subheadline.md)
  The font for subheadings.
- [static let largeTitle: UIFont.TextStyle](uifont/textstyle/largetitle.md)
  The font style for large titles.
- [static let extraLargeTitle: UIFont.TextStyle](uifont/textstyle/extralargetitle.md)
  The font style for extra large titles.
- [static let extraLargeTitle2: UIFont.TextStyle](uifont/textstyle/extralargetitle2.md)
  The font style for extra extra large titles.
- [static let title1: UIFont.TextStyle](uifont/textstyle/title1.md)
  The font for first-level hierarchical headings.
- [static let title2: UIFont.TextStyle](uifont/textstyle/title2.md)
  The font for second-level hierarchical headings.
- [static let title3: UIFont.TextStyle](uifont/textstyle/title3.md)
  The font for third-level hierarchical headings.
### Metrics
- [var metrics: UIFontMetrics](uifont/textstyle/metrics.md)
  The corresponding font metrics object for the text style.
### Initializers
- [init(rawValue: String)](uifont/textstyle/init(rawvalue:).md)
  Creates a text style with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [class func preferredFont(forTextStyle: UIFont.TextStyle) -> UIFont](uifont/preferredfont(fortextstyle:).md)
  Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [class func preferredFont(forTextStyle: UIFont.TextStyle, compatibleWith: UITraitCollection?) -> UIFont](uifont/preferredfont(fortextstyle:compatiblewith:).md)
  Returns an instance of the system font for the appropriate text style and traits.
- [init?(name: String, size: CGFloat)](uifont/init(name:size:).md)
  Creates and returns a font object for the specified font name and size.
- [init(descriptor: UIFontDescriptor, size: CGFloat)](uifont/init(descriptor:size:).md)
  Returns a font that matches the specified font descriptor.
- [func withSize(CGFloat) -> UIFont](uifont/withsize(_:).md)
  Returns a font object that is the same as the font, but has the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/textstyle)*