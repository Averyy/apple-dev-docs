# listSidebarCellConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a cell in a sidebar list.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```objc
+ (instancetype) listSidebarCellConfiguration;
```

## Return Value

The default configuration for a cell in a sidebar list.

## Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a cell in a sidebar collection view list, including highlighted and selected states.

For an appearance consistent with system defaults, use this background configuration for a cell in a collection view list that you configure with the [`UICollectionLayoutListAppearanceSidebar`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md) or [`UICollectionLayoutListAppearanceSidebarPlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) enumeration case.

## See Also

### Deprecated methods
- [+ listPlainCellConfiguration](./listplaincellconfiguration.md)
  Creates the default configuration you use to style a cell in a plain list.
- [+ listGroupedCellConfiguration](./listgroupedcellconfiguration.md)
  Creates the default configuration you use to style a cell in a grouped list.
- [+ listPlainHeaderFooterConfiguration](./listplainheaderfooterconfiguration.md)
  Creates the default configuration you use to style a plain list header or footer.
- [+ listGroupedHeaderFooterConfiguration](./listgroupedheaderfooterconfiguration.md)
  Creates the default configuration you use to style a grouped list header or footer.
- [+ listSidebarHeaderConfiguration](./listsidebarheaderconfiguration.md)
  Creates the default configuration you use to style a sidebar list header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listsidebarcellconfiguration)*