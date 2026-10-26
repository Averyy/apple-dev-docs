# listAccompaniedSidebarCellConfiguration

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a cell in an accompanied sidebar list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) listAccompaniedSidebarCellConfiguration;
```

#### Return Value

The default configuration for a cell in an accompanied sidebar list.

#### Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a cell in an accompanied sidebar collection view list, including highlighted and selected states. An accompanied sidebar collection view list is a list that’s in the primary column of a split view controller, accompanied by another list in the split view controller’s supplementary column.

For an appearance consistent with system defaults, use this background configuration for a cell in an accompanied sidebar collection view list that you configure with the [`UICollectionLayoutListAppearanceSidebar`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebar.md) or [`UICollectionLayoutListAppearanceSidebarPlain`](../uicollectionlayoutlistappearance/uicollectionlayoutlistappearancesidebarplain.md) enumeration case.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-c.class/listaccompaniedsidebarcellconfiguration)*