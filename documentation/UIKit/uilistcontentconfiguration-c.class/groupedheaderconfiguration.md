# groupedHeaderConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a header in a grouped list.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```objc
+ (instancetype) groupedHeaderConfiguration;
```

#### Return Value

The default configuration for a header in a grouped list.

#### Discussion

Create this configuration to update the content and styling of a header in a table view or collection view list.

For an appearance consistent with system defaults, display your header in a table view or collection view list that you configure with one of the following enumeration cases:

- [`UITableView.Style.grouped`](../uitableview/style-swift.enum/grouped.md)
- [`UITableView.Style.insetGrouped`](../uitableview/style-swift.enum/insetgrouped.md)
- [`UICollectionLayoutListAppearanceGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancegrouped.md)
- [`UICollectionLayoutListAppearanceInsetGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md)

Configure the background of your header using one of the [`UIBackgroundConfiguration`](../uibackgroundconfiguration-c.class.md) options below. Match the background of your header to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listGroupedHeaderFooterConfiguration`](../uibackgroundconfiguration-c.class/listgroupedheaderfooterconfiguration.md) | [`UITableView.Style.grouped`](../uitableview/style-swift.enum/grouped.md), [`UITableView.Style.insetGrouped`](../uitableview/style-swift.enum/insetgrouped.md), [`UICollectionLayoutListAppearanceGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancegrouped.md), [`UICollectionLayoutListAppearanceInsetGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md) |

## See Also

### Deprecated methods
- [+ sidebarCellConfiguration](./sidebarcellconfiguration.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [+ sidebarSubtitleCellConfiguration](./sidebarsubtitlecellconfiguration.md)
  Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.
- [+ plainHeaderConfiguration](./plainheaderconfiguration.md)
  Creates the default configuration you use to style a header in a plain list.
- [+ plainFooterConfiguration](./plainfooterconfiguration.md)
  Creates the default configuration you use to style a footer in a plain list.
- [+ groupedFooterConfiguration](./groupedfooterconfiguration.md)
  Creates the default configuration you use to style a footer in a grouped list.
- [+ sidebarHeaderConfiguration](./sidebarheaderconfiguration.md)
  Creates the default configuration you use to style a header in a sidebar list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/groupedheaderconfiguration)*