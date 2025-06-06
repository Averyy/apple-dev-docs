# sidebarSubtitleCell()

**Framework**: UIKit  
**Kind**: method

Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
static func sidebarSubtitleCell() -> UIListContentConfiguration
```

#### Return Value

The default configuration for a cell that’s in a sidebar list and contains subtitle text.

#### Discussion

Create this configuration to update the content and styling of a cell in a sidebar collection view list. When you apply this configuration to a cell, the cell displays one primary label and one subtitle label below the primary label. Both labels resize automatically based on the length of the text you provide and the device’s Dynamic Type and accessibility settings.

For an appearance consistent with system defaults, display your cell in a sidebar collection view list that you configure with one of the following enumeration cases:

- [`UICollectionLayoutListConfiguration.Appearance.sidebar`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md)
- [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md)

Configure the background of your cell using one of the [`UIBackgroundConfiguration`](uibackgroundconfiguration-swift.struct.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listSidebarCell()`](uibackgroundconfiguration-swift.struct/listsidebarcell().md) | [`UICollectionLayoutListConfiguration.Appearance.sidebar`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md), [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) |

## See Also

- [static func cell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/cell.md)
  Creates the default configuration you use to style a cell in a list.
- [static func subtitleCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/subtitlecell.md)
  Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [static func valueCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/valuecell.md)
  Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [static func sidebarCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/sidebarcell.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [static func accompaniedSidebarCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/accompaniedsidebarcell.md)
  Creates the default configuration you use to style a cell in an accompanied sidebar list.
- [static func accompaniedSidebarSubtitleCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/accompaniedsidebarsubtitlecell.md)
  Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/sidebarsubtitlecell())*