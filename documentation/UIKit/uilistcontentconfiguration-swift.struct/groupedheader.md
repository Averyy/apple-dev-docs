# groupedHeader()

**Framework**: UIKit  
**Kind**: method

Creates the default configuration you use to style a header in a grouped list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func groupedHeader() -> UIListContentConfiguration
```

#### Return Value

The default configuration for a header in a grouped list.

#### Discussion

Create this configuration to update the content and styling of a header in a table view or collection view list.

For an appearance consistent with system defaults, display your header in a table view or collection view list that you configure with one of the following enumeration cases:

- [`UITableView.Style.grouped`](uitableview/style-swift.enum/grouped.md)
- [`UITableView.Style.insetGrouped`](uitableview/style-swift.enum/insetgrouped.md)
- [`UICollectionLayoutListConfiguration.Appearance.grouped`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/grouped.md)
- [`UICollectionLayoutListConfiguration.Appearance.insetGrouped`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md)

Configure the background of your header using one of the [`UIBackgroundConfiguration`](uibackgroundconfiguration-swift.struct.md) options below. Match the background of your header to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listGroupedHeaderFooter()`](uibackgroundconfiguration-swift.struct/listgroupedheaderfooter().md) | [`UITableView.Style.grouped`](uitableview/style-swift.enum/grouped.md), [`UITableView.Style.insetGrouped`](uitableview/style-swift.enum/insetgrouped.md), [`UICollectionLayoutListConfiguration.Appearance.grouped`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/grouped.md), [`UICollectionLayoutListConfiguration.Appearance.insetGrouped`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/insetgrouped.md) |

## See Also

- [static func plainHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/plainheader.md)
  Creates the default configuration you use to style a header in a plain list.
- [static func plainFooter() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/plainfooter.md)
  Creates the default configuration you use to style a footer in a plain list.
- [static func groupedFooter() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/groupedfooter.md)
  Creates the default configuration you use to style a footer in a grouped list.
- [static func prominentInsetGroupedHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/prominentinsetgroupedheader.md)
  Creates the default configuration you use to style a prominent header in an inset grouped list.
- [static func extraProminentInsetGroupedHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/extraprominentinsetgroupedheader.md)
  Creates the default configuration you use to style an extra prominent header in an inset grouped list.
- [static func sidebarHeader() -> UIListContentConfiguration](uilistcontentconfiguration-swift.struct/sidebarheader.md)
  Creates the default configuration you use to style a header in a sidebar list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/groupedheader())*