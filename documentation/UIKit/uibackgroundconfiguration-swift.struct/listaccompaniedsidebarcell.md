# listAccompaniedSidebarCell()

**Framework**: UIKit  
**Kind**: method

Creates the default configuration you use to style a cell in an accompanied sidebar list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func listAccompaniedSidebarCell() -> UIBackgroundConfiguration
```

#### Return Value

The default configuration for a cell in an accompanied sidebar list.

#### Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a cell in an accompanied sidebar collection view list, including styling for highlighted and selected states. An accompanied sidebar collection view list is a list that’s in the primary column of a split view controller, accompanied by another list in the split view controller’s supplementary column.

For an appearance consistent with system defaults, use this background configuration for a cell in an accompanied sidebar collection view list that you configure with the [`UICollectionLayoutListConfiguration.Appearance.sidebar`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebar.md) or [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) enumeration case.

## See Also

- [static func listPlainCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listplaincell.md)
  Creates the default configuration you use to style a cell in a plain list.
- [static func listGroupedCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listgroupedcell.md)
  Creates the default configuration you use to style a cell in a grouped list.
- [static func listSidebarCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listsidebarcell.md)
  Creates the default configuration you use to style a cell in a sidebar list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listaccompaniedsidebarcell())*