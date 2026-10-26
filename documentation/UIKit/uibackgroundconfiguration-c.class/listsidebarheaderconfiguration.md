# listSidebarHeaderConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a sidebar list header.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```objc
+ (instancetype) listSidebarHeaderConfiguration;
```

#### Return Value

The default configuration for a sidebar list header.

#### Discussion

> **Deprecated**: Use [`listHeader()`](../uibackgroundconfiguration-swift.struct/listheader%28%29.md) or [`listFooter()`](../uibackgroundconfiguration-swift.struct/listfooter%28%29.md) instead.

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a sidebar list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in a collection view list that you configure with the [`UICollectionLayoutListAppearanceSidebar`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md) enumeration case.

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
- [+ listGroupedHeaderFooterConfiguration](./listgroupedheaderfooterconfiguration.md)
  Creates the default configuration you use to style a grouped list header or footer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listsidebarheaderconfiguration)*