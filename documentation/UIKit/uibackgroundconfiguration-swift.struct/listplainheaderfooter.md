# listPlainHeaderFooter()

**Framework**: UIKit  
**Kind**: method

Creates the default configuration you use to style a plain list header or footer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
static func listPlainHeaderFooter() -> UIBackgroundConfiguration
```

#### Return Value

The default configuration for a plain list header or footer.

#### Discussion

Create this configuration to update the styling for the background of a header or footer in a table view or collection view list. When you apply this configuration, the background of the header or footer matches the system default styling for a header or footer in a plain list.

For an appearance consistent with system defaults, use this background configuration for a header or footer in these contexts:

- A table view that you configure with the [`UITableView.Style.plain`](uitableview/style-swift.enum/plain.md) enumeration case.
- A collection view list that you configure with the [`UICollectionLayoutListConfiguration.Appearance.plain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/plain.md) or [`UICollectionLayoutListConfiguration.Appearance.sidebarPlain`](uicollectionlayoutlistconfiguration-swift.struct/appearance-swift.enum/sidebarplain.md) enumeration cases.

## See Also

- [static func listGroupedHeaderFooter() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listgroupedheaderfooter.md)
  Creates the default configuration you use to style a grouped list header or footer.
- [static func listSidebarHeader() -> UIBackgroundConfiguration](uibackgroundconfiguration-swift.struct/listsidebarheader.md)
  Creates the default configuration you use to style a sidebar list header.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundconfiguration-swift.struct/listplainheaderfooter())*