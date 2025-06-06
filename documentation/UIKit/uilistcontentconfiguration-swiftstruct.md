# UIListContentConfiguration

**Framework**: UIKit  
**Kind**: struct

A content configuration for a list-based content view.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
struct UIListContentConfiguration
```

#### Overview

A list content configuration describes the styling and content for an individual element that might appear in a list, like a cell, header, or footer. Using a list content configuration, you can obtain system default styling for a variety of different view states. You fill the configuration with your content, and then assign it directly to cells, headers, and footers in [`UICollectionView`](uicollectionview.md) and [`UITableView`](uitableview.md), or to your own custom list content view ([`UIListContentView`](uilistcontentview.md)).

For views like cells, headers, and footers, use their [`defaultContentConfiguration()`](uicollectionviewlistcell/defaultcontentconfiguration().md) to get a list content configuration that has preconfigured default styling. Alternatively, you can create a list content configuration from one of the system default styles. After you get the configuration, you assign your content to it, customize any other properties, and assign it to your view as the current content configuration.

```swift
var content = cell.defaultContentConfiguration()

// Configure content.
content.image = UIImage(systemName: "star")
content.text = "Favorites"

// Customize appearance.
content.imageProperties.tintColor = .purple

cell.contentConfiguration = content
```

## Topics

### Creating default cell configurations
- [static func cell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/cell.md)
  Creates the default configuration you use to style a cell in a list.
- [static func subtitleCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/subtitlecell.md)
  Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [static func valueCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/valuecell.md)
  Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [static func sidebarCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/sidebarcell.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [static func sidebarSubtitleCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/sidebarsubtitlecell.md)
  Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.
- [static func accompaniedSidebarCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/accompaniedsidebarcell.md)
  Creates the default configuration you use to style a cell in an accompanied sidebar list.
- [static func accompaniedSidebarSubtitleCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/accompaniedsidebarsubtitlecell.md)
  Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.
### Creating header and footer configurations
- [static func plainHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/plainheader.md)
  Creates the default configuration you use to style a header in a plain list.
- [static func plainFooter() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/plainfooter.md)
  Creates the default configuration you use to style a footer in a plain list.
- [static func groupedHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/groupedheader.md)
  Creates the default configuration you use to style a header in a grouped list.
- [static func groupedFooter() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/groupedfooter.md)
  Creates the default configuration you use to style a footer in a grouped list.
- [static func prominentInsetGroupedHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/prominentinsetgroupedheader.md)
  Creates the default configuration you use to style a prominent header in an inset grouped list.
- [static func extraProminentInsetGroupedHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/extraprominentinsetgroupedheader.md)
  Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [static func sidebarHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/sidebarheader.md)
  Creates the default configuration you use to style a header in a sidebar list.
### Customizing content
- [var image: UIImage?](uilistcontentconfiguration-swift.struct/image.md)
  The image to display.
- [var text: String?](uilistcontentconfiguration-swift.struct/text.md)
  The primary text.
- [var attributedText: NSAttributedString?](uilistcontentconfiguration-swift.struct/attributedtext.md)
  An attributed variant of the primary text.
- [var secondaryText: String?](uilistcontentconfiguration-swift.struct/secondarytext.md)
  The secondary text.
- [var secondaryAttributedText: NSAttributedString?](uilistcontentconfiguration-swift.struct/secondaryattributedtext.md)
  An attributed variant of the secondary text.
### Customizing appearance
- [var imageProperties: UIListContentConfiguration.ImageProperties](uilistcontentconfiguration-swift.struct/imageproperties-swift.property.md)
  Properties for configuring the image.
- [var textProperties: UIListContentConfiguration.TextProperties](uilistcontentconfiguration-swift.struct/textproperties-swift.property.md)
  Properties for configuring the primary text.
- [var secondaryTextProperties: UIListContentConfiguration.TextProperties](uilistcontentconfiguration-swift.struct/secondarytextproperties.md)
  Properties for configuring the secondary text.
- [UIListContentConfiguration.ImageProperties](uilistcontentconfiguration-swift.struct/imageproperties-swift.struct.md)
  Properties that affect the list content configuration’s image.
- [UIListContentConfiguration.TextProperties](uilistcontentconfiguration-swift.struct/textproperties-swift.struct.md)
  Properties that affect the list content configuration’s text.
### Customizing layout
- [var axesPreservingSuperviewLayoutMargins: UIAxis](uilistcontentconfiguration-swift.struct/axespreservingsuperviewlayoutmargins.md)
  A Boolean value that determines whether the content view preserves the layout margins that it inherits from its superview on the horizontal or vertical axes.
- [var directionalLayoutMargins: NSDirectionalEdgeInsets](uilistcontentconfiguration-swift.struct/directionallayoutmargins.md)
  The margins between the content and the edges of the content view.
- [var prefersSideBySideTextAndSecondaryText: Bool](uilistcontentconfiguration-swift.struct/preferssidebysidetextandsecondarytext.md)
  A Boolean value that determines whether the configuration positions the text and secondary text side by side.
- [var imageToTextPadding: CGFloat](uilistcontentconfiguration-swift.struct/imagetotextpadding.md)
  The padding between the image and text.
- [var textToSecondaryTextHorizontalPadding: CGFloat](uilistcontentconfiguration-swift.struct/texttosecondarytexthorizontalpadding.md)
  The minimum horizontal padding between the text and secondary text.
- [var textToSecondaryTextVerticalPadding: CGFloat](uilistcontentconfiguration-swift.struct/texttosecondarytextverticalpadding.md)
  The vertical padding between the text and secondary text.
### Instance Properties
- [var alpha: CGFloat](uilistcontentconfiguration-swift.struct/alpha.md)
### Type Methods
- [static func footer() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/footer.md)
- [static func header() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/header.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomReflectable](../Swift/CustomReflectable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [UIContentConfiguration](uicontentconfiguration-9eib5.md)

## See Also

- [class UIListContentView](uilistcontentview.md)
  A content view for displaying list-based content.
- [protocol UIContentConfiguration](uicontentconfiguration-9eib5.md)
  The requirements for an object that provides the configuration for a content view.
- [protocol UIContentView](uicontentview-5fh3z.md)
  The requirements for a content view that you create using a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct)*