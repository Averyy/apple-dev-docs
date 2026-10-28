# listGroupedHeaderFooterConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a grouped list header or footer.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```objc
+ (instancetype) listGroupedHeaderFooterConfiguration;
```

## Return Value

The default configuration for a grouped list header or footer.

## Discussion

> **Deprecated**: Use [`listHeader()`](../uibackgroundconfiguration-swift.struct/listheader%28%29.md) or [`listFooter()`](../uibackgroundconfiguration-swift.struct/listfooter%28%29.md) instead.

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a grouped list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in these contexts:

- A table view that you configure with the [`UITableView.Style.grouped`](../uitableview/style-swift.enum/grouped.md) or [`UITableView.Style.insetGrouped`](../uitableview/style-swift.enum/insetgrouped.md) enumeration cases.
- A a collection view list that you configure with the [`UICollectionLayoutListAppearanceGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancegrouped.md) or [`UICollectionLayoutListAppearanceInsetGrouped`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearanceinsetgrouped.md) enumeration cases.

## See Also

### Deprecated methods
- [+ listPlainCellConfiguration](./listplaincellconfiguration.md)
  Creates the default configuration you use to style a cell in a plain list.
- [+ listGroupedCellConfiguration](./listgroupedcellconfiguration.md)
  Creates the default configuration you use to style a cell in a grouped list.
- [+ listSidebarCellConfiguration](./listsidebarcellconfiguration.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [+ listPlainHeaderFooterConfiguration](./listplainheaderfooterconfiguration.md)
  Creates the default configuration you use to style a plain list header or footer.
- [+ listSidebarHeaderConfiguration](./listsidebarheaderconfiguration.md)
  Creates the default configuration you use to style a sidebar list header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listgroupedheaderfooterconfiguration)*