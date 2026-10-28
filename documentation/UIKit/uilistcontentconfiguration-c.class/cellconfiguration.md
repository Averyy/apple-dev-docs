# cellConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a cell in a list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) cellConfiguration;
```

## Return Value

The default configuration for a cell in a list.

## Discussion

Create this configuration to update the content and styling of a cell. When you apply this configuration to a cell, the cell displays one label, which resizes automatically based on the length of the text you provide and the device’s Dynamic Type and accessibility settings.

For an appearance consistent with system defaults, display your cell in a table view or collection view list that you configure with one of the following enumeration cases:

- [`UITableView.Style.plain`](../uitableview/style-swift.enum/plain.md)
- [`UITableView.Style.grouped`](../uitableview/style-swift.enum/grouped.md)
- [`UITableView.Style.insetGrouped`](../uitableview/style-swift.enum/insetgrouped.md)
- [`UICollectionLayoutListAppearancePlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md)
- [`UICollectionLayoutListAppearanceGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancegrouped.md)
- [`UICollectionLayoutListAppearanceInsetGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md)

Configure the background of your cell using one of the [`UIBackgroundConfiguration`](../uibackgroundconfiguration-c.class.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listPlainCellConfiguration`](../uibackgroundconfiguration-c.class/listplaincellconfiguration.md) | [`UITableView.Style.plain`](../uitableview/style-swift.enum/plain.md), [`UICollectionLayoutListAppearancePlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceplain.md) |
| [`listGroupedCellConfiguration`](../uibackgroundconfiguration-c.class/listgroupedcellconfiguration.md) | [`UITableView.Style.grouped`](../uitableview/style-swift.enum/grouped.md), [`UITableView.Style.insetGrouped`](../uitableview/style-swift.enum/insetgrouped.md), [`UICollectionLayoutListAppearanceGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancegrouped.md), [`UICollectionLayoutListAppearanceInsetGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md) |

## See Also

### Creating default cell configurations
- [+ subtitleCellConfiguration](./subtitlecellconfiguration.md)
  Creates the default configuration you use to style a cell that’s in a list and contains subtitle text.
- [+ valueCellConfiguration](./valuecellconfiguration.md)
  Creates the default configuration you use to style a cell that’s in a list and contains side-by-side value text.
- [+ accompaniedSidebarCellConfiguration](./accompaniedsidebarcellconfiguration.md)
  Creates the default configuration you use to style a cell in an accompanied sidebar list.
- [+ accompaniedSidebarSubtitleCellConfiguration](./accompaniedsidebarsubtitlecellconfiguration.md)
  Creates the default configuration you use to style a cell that’s in an accompanied sidebar list and contains subtitle text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/cellconfiguration)*