# sidebarSubtitleCellConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a cell that’s in a sidebar list and contains subtitle text.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```objc
+ (instancetype) sidebarSubtitleCellConfiguration;
```

## Return Value

The default configuration for a cell that’s in a sidebar list and contains subtitle text.

## Discussion

Create this configuration to update the content and styling of a cell in a sidebar collection view list. When you apply this configuration to a cell, the cell displays one primary label and one subtitle label below the primary label. Both labels resize automatically based on the length of the text you provide and the device’s Dynamic Type and accessibility settings.

For an appearance consistent with system defaults, display your cell in a sidebar collection view list that you configure with one of the following enumeration cases:

- [`UICollectionLayoutListAppearanceSidebar`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md)
- [`UICollectionLayoutListAppearanceSidebarPlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md)

Configure the background of your cell using one of the [`UIBackgroundConfiguration`](../uibackgroundconfiguration-c.class.md) options below. Match the background of your cell to the corresponding table view or collection view styles as follows:

| Background configuration option | Matching table view or collection view styles |
| --- | --- |
| [`listSidebarCellConfiguration`](../uibackgroundconfiguration-c.class/listsidebarcellconfiguration.md) | [`UICollectionLayoutListAppearanceSidebar`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md), [`UICollectionLayoutListAppearanceSidebarPlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) |

## See Also

### Deprecated methods
- [+ sidebarCellConfiguration](./sidebarcellconfiguration.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [+ plainHeaderConfiguration](./plainheaderconfiguration.md)
  Creates the default configuration you use to style a header in a plain list.
- [+ plainFooterConfiguration](./plainfooterconfiguration.md)
  Creates the default configuration you use to style a footer in a plain list.
- [+ groupedHeaderConfiguration](./groupedheaderconfiguration.md)
  Creates the default configuration you use to style a header in a grouped list.
- [+ groupedFooterConfiguration](./groupedfooterconfiguration.md)
  Creates the default configuration you use to style a footer in a grouped list.
- [+ sidebarHeaderConfiguration](./sidebarheaderconfiguration.md)
  Creates the default configuration you use to style a header in a sidebar list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-c.class/sidebarsubtitlecellconfiguration)*