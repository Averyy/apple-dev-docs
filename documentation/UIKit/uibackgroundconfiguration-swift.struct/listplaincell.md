# listPlainCell()

**Framework**: UIKit  
**Kind**: method

Creates the default configuration you use to style a cell in a plain list.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func listPlainCell() -> UIBackgroundConfiguration
```

#### Return Value

The default configuration for a cell in a plain list.

#### Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a plain cell, including styling for highlighted and selected states.

For an appearance consistent with system defaults, use this background configuration for a cell in these contexts:

- A table view that you configure with the [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md) enumeration case.
- A collection view list that you configure with the [`UICollectionLayoutListConfiguration.Appearance.plain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) enumeration case.

## See Also

- [static func listGroupedCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listgroupedcell.md)
  Creates the default configuration you use to style a cell in a grouped list.
- [static func listSidebarCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listsidebarcell.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [static func listAccompaniedSidebarCell() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listaccompaniedsidebarcell.md)
  Creates the default configuration you use to style a cell in an accompanied sidebar list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listplaincell())*