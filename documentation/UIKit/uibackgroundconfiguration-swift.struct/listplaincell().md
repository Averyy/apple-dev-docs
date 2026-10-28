# listPlainCell()

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Creates the default configuration you use to style a cell in a plain list.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0 (renamed: listCell)
- iPadOS 14.0+ - Deprecated in 18.0 (renamed: listCell)
- Mac Catalyst 14.0+ - Deprecated in 18.0 (renamed: listCell)
- tvOS 14.0+ - Deprecated in 18.0 (renamed: listCell)
- visionOS

## Declaration

```swift
static func listPlainCell() -> UIBackgroundConfiguration
```

## Return Value

The default configuration for a cell in a plain list.

## Discussion

Create this configuration to update the styling for the background of a cell in a list. When you apply this configuration to a cell, the background of the cell matches the system default styling for a plain cell, including styling for highlighted and selected states.

For an appearance consistent with system defaults, use this background configuration for a cell in these contexts:

- A table view that you configure with the [`UITableView.Style.plain`](../uitableview/style-swift.enum/plain.md) enumeration case.
- A collection view list that you configure with the [`UICollectionLayoutListConfiguration.Appearance.plain`](../uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) enumeration case.

## See Also

### Creating cell background configurations
- [static func listGroupedCell() -> UIBackgroundConfiguration](./listgroupedcell%28%29.md)
  Creates the default configuration you use to style a cell in a grouped list.
- [static func listSidebarCell() -> UIBackgroundConfiguration](./listsidebarcell%28%29.md)
  Creates the default configuration you use to style a cell in a sidebar list.
- [static func listAccompaniedSidebarCell() -> UIBackgroundConfiguration](./listaccompaniedsidebarcell%28%29.md)
  Creates the default configuration you use to style a cell in an accompanied sidebar list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listplaincell())*