# valueCell()

**Framework**: UIKit  
**Kind**: method

Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func valueCell() -> UIListContentConfiguration
```

#### Return Value

The default configuration for a cell that’s in a list and contains side-by-side value text.

#### Discussion

Create this configuration to update the content and styling of a cell in a list. When you apply this configuration to a cell, the cell displays one primary label and one value label next to the main label in the trailing direction. Both labels resize automatically based on the length of the text you provide and the device’s Dynamic Type and accessibility settings.

For an appearance consistent with system defaults, display your cell in a table view or collection view list that you configure with one of the following enumeration cases:

- [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md)
- [`UITableView.Style.grouped`](uitableview/style-swift.enum/grouped.md)
- [`UITableView.Style.insetGrouped`](uitableview/style-swift.enum/insetgrouped.md)
- [`UICollectionLayoutListConfiguration.Appearance.plain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md)
- [`UICollectionLayoutListConfiguration.Appearance.grouped`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/grouped.md)
- [`UICollectionLayoutListConfiguration.Appearance.insetGrouped`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md)

Configure the background of your cell using one of the [`UIBackgroundConfiguration`](uibackgroundconfiguration-swift.struct.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listPlainCell()`](uibackgroundconfiguration-swift.struct/listplaincell().md) | [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md), [`UICollectionLayoutListConfiguration.Appearance.plain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) |
| [`listGroupedCell()`](uibackgroundconfiguration-swift.struct/listgroupedcell().md) | [`UITableView.Style.grouped`](uitableview/style-swift.enum/grouped.md), [`UITableView.Style.insetGrouped`](uitableview/style-swift.enum/insetgrouped.md), [`UICollectionLayoutListConfiguration.Appearance.grouped`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/grouped.md), [`UICollectionLayoutListConfiguration.Appearance.insetGrouped`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md) |

## See Also

- [static func cell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/cell.md)
  Creates the default configuration you use to style a cell in a list.
- [static func subtitleCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/subtitlecell.md)
  Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [static func sidebarCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/sidebarcell.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [static func sidebarSubtitleCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/sidebarsubtitlecell.md)
  Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.
- [static func accompaniedSidebarCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/accompaniedsidebarcell.md)
  Creates the default configuration you use to style a cell in an accompanied sidebar list.
- [static func accompaniedSidebarSubtitleCell() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/accompaniedsidebarsubtitlecell.md)
  Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/valuecell())*